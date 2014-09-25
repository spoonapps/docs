### Java

In this tutorial, we'll containerize a Java web server project. You'll learn to effectively configure and use Java in a container.

**Topics Covered:**

- The basic image creation workflow
- Configuring environment variables within a container
- Using git within a container

#### Pull Required Dependencies

Before beginning, we'll get all of the dependencies we'll need to run and containerize the Java project. In this case, that means we'll need both Java and Git inside our container. Luckily, both of these images can be found in the **spoonbrew** account on the Spoon hub. 

```
# Pull dependencies
> spoon pull spoonbrew/jdk:7.65

> spoon pull spoonbrew/git
```

#### Configure the Container

Since we'll be pulling the sources into our container using Git, let's start the container and do all of our work in there. 

```
# Start the container
> spoon run -w="C:\" -d --startup-file=cmd.exe spoonbrew/git,spoonbrew/jdk7

# Create and navigate to C:\java
(3df234f3) C:\> mkdir java & cd java

# Clone the project
(3df234f3) C:\java> git clone https://github.com/rafaelsteil/simple-webserver.git

# Change directory to the base project directory
(3df234f3) C:\java> cd simple-webserver

# Run the server from within the container
(3df234f3) C:\java\simple-webserver> java -jar SimpleWebServer.jar
```

The server is now running on port 80 of your local machine. To confirm the server is running, open a web browser and visit **http://localhost** -- you should see a listing of all the files in the **C:\\java** folder of the container. 

#### Create an Image

Let's say you want to use this new container as a basis for other projects -- perhaps expanding on the functionality of this simple webserver. 

```
# Stop the container
> spoon stop 3df234ff3

# Commit the container
> spoon commit 3df234f3 simple-java-webserver
```

By default, this will create a new images that includes the base spoonbrew/git and spoonbrew/java images. If you wish to only include the container itself in the new image, add the **--no-base** flag to the commit command. 

```
> spoon commit --no-base 3df234f3 simple-java-webserver
```

**Optional**: Tag the Image

A given image has two pieces of publicly available metadata attached to it: it's **name** and it's **tag**. A tag is similar to a version and should be used to mark major branches or releases of a project. 

To illustrate this idea, we'll tag our newly created image as **1.0**.

```
# Create a new tag of 1.0 for the image
> spoon tag simple-java-webserver 1.0
```

When `spoon images` is executed, you should now see a new entry for **simple-java-webserver:1.0**.

```
> spoon images

ID            Name                   Tag   Created                Size
--            ----                   ---   -------                ----
7a85fe8f7ad1  spoonbrew/jdk 		 7.65  8/22/2014 11:34:19 AM  74.3 MB
9iejrk2a34hd  spoonbrew/git 		 1.94  8/21/2014 11:32:00 AM  50.4 MB
3j24fjdk3kj4  simple-java-webserver        8/22/2014 11:52:32 AM  20.2 MB
3j24fjdk3kj4  simple-java-webserver  1.0   8/22/2014 11:59:59 AM  20.2 MB
```

#### Push to the Spoon Hub

We'll finish this tutorial by pushing the newly created **simple-java-webserver** image to the [Spoon Hub](/hub). 

```
# Push the image
> spoon push simple-java-webserver
```

This will create a new repository in your Spoon Hub account called **simple-java-webserver**, where the newly-pushed image will be placed. 

Note that if you tagged your image in the previous section, use the command: `spoon push simple-java-webserver:1.0`. 