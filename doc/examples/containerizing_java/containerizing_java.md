In this tutorial, we'll cover how to containerize a Java project and how to effectively use and configure Java within a Spoon container. 

#### Topics Covered

- The basic image creation workflow
- Configuring environment variables within a container
- Using git within a container

## Pull Required Dependencies

Before beginning, we'll get all of the dependencies we'll need to run and containerize the Java project. In this case, that means we'll need both `Java` and `Git` inside our container. Luckily, both of these images can be found in the `spoonbrew` account on the Spoonium hub. 

We'll start by issuing a `spoon pull` command for each of these dependencies. This will create local copies of these images for later use. 

	>spoon pull spoonbrew/jdk7
	>spoon pull spoonbrew/git

When both of these commands have completed, you can verify that they are indeed on your local system by running `spoon images`. 

	>spoon images

	NAME			SIZE		CREATED
	spoonbrew/git	32.1MB 		8/08/2014 5:09:11 PM
	spoonbrew/jdk7	43.2MB 		8/10/2014 10:00:32 AM


## Start a Container

Since we'll be pulling the sources into our container using `git`, let's start the container and do all of our work in there. 

In this case, however, a little foresight goes a long way. We'll want to add our project's directory to the Java classpath -- this should make developing new features on top of this server much simpler. To do this, we can use the `--env` flag of the `spoon run` command. 

We're going to clone the project into a `C:\java` folder in the container, so we'll add this path to the `classpath` variable upon initial container creation. 

To start the container, issue a `spoon run` command with both the `spoonbrew/java` and `spoonbrew/git` images specified as base images. We'll also add a `--env` flag for the Java classpath variable. 

	spoon run --env=CLASSPATH=%CLASSPATH%;C:\java spoonbrew/git;spoonbrew/jdk7 cmd.exe

A new command prompt should appear on your screen. This command prompt is running inside our new container, and can be used to manipulate the container's environment. 

## Clone the Project

For this example, we'll clone a small, standalone web server from this Github repository: [https://github.com/rafaelsteil/simple-webserver](https://github.com/rafaelsteil/simple-webserver). 

In the containerized command prompt, `cd` to the root `C:\` folder and create a new `java` folder, if one does not already exist. 

	(08dd45e3) C:\Users\SpoonUser>cd C:\
	(08dd45e3) C:\>mkdir java

Now, we'll issue a `git clone` command for the above-mentioned repository, cloning it into the `C:\java` folder. 

	(08dd45e3) C:\>git clone https://github.com/rafaelsteil/simple-webserver C:\java

The contents of the repository should now appear in the `C:\java` folder of the container.

The server can now be run from within the container. To do so, run the command `java -jar C:\java\SimpleWebServer.jar` from the containerized command prompt. 

	(08dd45e3) >java -jar C:\java\SimpleWebServer.jar

The server is now running on port 80 of your local machine. To confirm the server is running, open a web browser and visit **http://localhost** -- you should see a listing of all the files in the `C:\java` folder of the container. 

## Create an Image

Let's say you want to use this new container as a basis for other projects -- perhaps expanding on the functionality of this simple webserver. 

This can be easily accomplished in Spoonium by creating an **image** of the current container. This will memorialize the container, along with any of it's dependencies so that new containers can be created on top of it. 

To do this, we'll first need to stop the container, if it is still running. To do this, simply close or kill any processes running inside the container. In this case, that should just be the command prompt. 

Once the container is stopped, we'll use the `spoon commit` command to create a new image from the container. 

The `commit` command has 2 mandatory parameters: the ID of the container to commit and the name of the image to be created. We'll commit our recently created image with the name **simple-java-webserver**. 

	>spoon commit 08dd45e3 simple-java-webserver

By default, this will create a new images that *includes* the base `spoonbrew/git` and `spoonbrew/java` images. If you wish to only include the container itself in the new image, add the `--no-base` flag to the `commit` command. 

	>spoon commit --no-base 08dd45e3 simple-java-webserver

#### Optional: Tag the Image

A given image has two pieces of publicly available metadata attached to it: it's **name** and it's **tag**. A tag is similar to a version, and can be used to keep track of the different iterations on a single image. 

To illustrate this idea, we'll tag our newly created image as **1.0**.

**Note**: If an image is not explicitly tagged, it is automatically given the tag **master**. 

To tag an image, use the `spoon tag` command, with the image and the new tag as parameters. 

	>spoon tag simple-java-webserver:master simple-java-webserver:1.0

When `spoon images` is executed, you should now see a new entry for `simple-java-webserver:1.0`.

	>spoon images

	NAME			SIZE		CREATED
	spoonbrew/git	32.1MB 		8/08/2014 5:09:11 PM
	spoonbrew/jdk7	43.2MB 		8/10/2014 10:00:32 AM
    
    # Push to the Spoonium Hub

We'll finish this tutorial by explaining how the newly created `simple-java-webserver` can be uploaded to the [Spoonium Hub](http://spoonium.net/hub), where it can be made publicly available or shared with other collaborators. 

This can be especially useful when working in development teams that need to share work with each other. When you push an image to the Spoonium Hub, it creates a new repository for it (if one doesn't already exist) under your account. The repository page is then viewable from the URL: **http://spoonium.net/hub/{username}/{repo name**. This repository will be public, by default. 

 To push an image, execute the `spoon push` command from your local command prompt. The `push` command takes two parameters: the repository to push to and the name of the image to push. 

In this case, we'll push to a repository named **java-webserver**. 

	>spoon push java-webserver simple-java-webserver:master

**Note**: If you tagged your image in the previous section, use the command: `spoon push java-webserver simple-java-webserver:1.0`. 