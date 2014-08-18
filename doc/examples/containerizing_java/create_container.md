# Create a Container

## Start the Container

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