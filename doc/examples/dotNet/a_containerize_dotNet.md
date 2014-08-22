## Automating .NET Application Deployment

In this tutorial, we'll cover how to containerize a .NET application so that it can run on any Windows computer, regardless of the natively-installed version of .NET. We'll then walk through how to integrate Spoonium into MSBuild to create an image as part of a standard build process. 

We'll be containerizing a simple [OWIN](http://owin.org/) server using a Spoonscript. 

All source code for this example is available on [Github](https://github.com/matt-black2/SimpleOwinServer). 

#### Topics Covered

- Automated image creation
- Integrating Spoon Script into MSBuild
- Managing containerized processes

## Pull Dependencies

For this project, we'll need .NET 4.0. The Spoonium team has published a suite of .NET images in the **spoonbrew** user account. To pull the .NET 4 image, run the following command: 

	C:\Users\SpoonUser>spoon pull spoonbrew/dotNet:4.0
