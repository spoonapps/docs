# Containerizing a .NET Server Application

In this tutorial, we'll cover how to containerize a .NET application so that it can run on any Windows computer, regardless of the natively-installed version of .NET. 

We'll be containerizing a simple [OWIN](http://owin.org/) server using a `*.me` script. 

All source code for this example is available on [Github](https://github.com/matt-black2/SimpleOwinServer). 

#### Topics Covered

- Automated image creation with Spoon.me scripts
- Integrating Spoon.me into MSBuild
- Managing containerized processes

## Pull Dependencies

For this project, we'll need .NET 4.0. The Spoonium team has published a suite of .NET images in the **spoonbrew** user account. To pull the .NET 4 image, run the following command: 

	C:\Users\SpoonUser>spoon pull spoonbrew/dotNet:4.0

## Build the Image

To build the image, we'll construct a basic `spoon.me` script. The script should take the compiled Server executable, along with any DLLs, copy them into a new container, and build an image from this container. 

In this example, we'll also set the startup file for the image to the Server executable. 

#### Create the Spoon.me Script

Begin by creating an empty text file named **spoon.me** in the project's root directory. 

All valid build scripts must start with the base image to be used. In this case, we'll use the `spoonbrew/dotNet:4.0` image. 

	FROM spoonbrew/dotNet:4.0

We're going to create a new folder in the container for the server's files. We'll put this in a new **C:\server** folder. 

	CMD mkdir C:\server

Now for a little Spoon trickery! In the near-future, we'll copy files into this newly-created folder. Environment variables are expanded within the VM so we'll capture a reference to the project's root directory before we change the working directory. 

	ENV projectroot %CD%

Before copying the files to the **C:\server** directory, we'll change the working directory in the container. 

	WORKDIR C:\server

Now, copy the files from the **bin\Release** folder of the solution into the container. To copy the contents of one directory to another, we'll use Windows' `robocopy` utility. 

	CMD robocopy %projectroot%\OwinHelloWorld\bin\Release %CD%

Lastly, set the startup file for the image to the Server executable. For this project, that is OwinHelloWorld.exe 

	STARTUP %CD%\OwinHelloWorld.exe

That's it! You should now have a functioning build script in the root directory of the project. 

See the bottom of this tutorial for a copy of the above-created script.

#### Manually Build the Image

The image can now be built with the `spoon build` command. 

	spoon build <project root>\spoon.me

The `build` command has a `-n` or `--name` flag that can be specified to name the build. Let's name this build `SimpleOwinServer`. 

	spoon build -n=SimpleOwinServer <project root>\spoon.me

#### Integrate with MSBuild



## Run the Image



## Spoon.me File

	FROM spoonbrew/dotNet:4.0
	CMD mkdir C:\server
	ENV projectroot %CD%
	WORKDIR C:\server
	CMD robocopy %projectroot%\OwinHelloWorld\bin\Release %CD%
	STARTUP %CD%\OwinHelloWorld.exe