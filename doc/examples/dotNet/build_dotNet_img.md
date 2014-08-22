#### Build the Image

For this project, we'll need .NET 4.0. The Spoonium team has published a suite of .NET images in the **spoonbrew** user account. To pull the .NET 4 image, run the following command: 

	C:\Users\SpoonUser>spoon pull spoonbrew/dotNet:4.0

To build the image, we'll construct a Spoon script. The script should take the compiled Server executable, along with any DLLs, copy them into a new container, and build an image from this container. Below is the **spoon.me** file for the example project used in this tutorial. 

Begin by creating an empty text file named **spoon.me** in the project's root directory.

	#should use the relevant version of .NET
	FROM spoonbrew/dotNet:4.0.3

	#make a new directory in the container for build outputs
	cmd mkdir C:\server

	#copy files from build output 
	cmd robocopy %CD%\bin\Release C:\server

	#set the startup file for the image to the executable
	boot file %CD%\OwinHelloWorld.exe

#### Integrate with MSBuild

The Spoon CLI is accessible from any command prompt on the installed system and can be integrated into MSBuild or any other build system just like a native Windows utility. 

In this section, we'll show you how you can set up Spoon to automatically rebuild a project's image each time your project is rebuilt. In this tutorial, we'll be using Visual Studio/MSBuild, though similar principles could be applied to any other IDE or build system. 

The easiest way to integrate with Visual Studio/MSBuild is to add a **Post-build event** to your build. 

To add a Post-build event, right-click on your project in Visual Studio and select **Build Events** from the left-hand menu. 

In the **Post-build event command line** box, add the line: 

	spoon build -n=$(SolutionName) $(SolutionDir)\spoon.me

**Note**: For solutions with multiple projects, we recommend only triggering a post-build event for the last project in the build chain. This may require customizing your Spoon script to also pull in the build outputs from these other projects. 