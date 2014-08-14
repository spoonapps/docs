# Containerizing .NET

In this tutorial, we'll cover how to containerize a .NET application so that it can run on any Windows computer, regardless of the natively-installed version of .NET. 

We'll be containerizing a simple [OWIN](http://owin.org/) server by compiling the source code inside a container. We'll also take you through some of the more advanced commands for managing files, registry keys, and processes within a container. 

#### Topics Covered

- Automated image creation with Spoon.me scripts
- Working with containerized .NET
- Managing containerized processes

## Pull Dependencies

For this project, we'll need .NET 4.0, as well as Git and NuGet. All of these dependencies are available on the Spoonium Hub via the **spoonbrew** user. To pull these dependencies, run the following commands in your local command prompt. 

	C:\Users\SpoonUser>spoon pull spoonbrew/dotNet4
	C:\Users\SpoonUser>spoon pull spoonbrew/git
	C:\Users\SpoonUser>spoon pull spoonbrew/nuget

## Build the Image

We want to automate the builds of 

