## Try It!

### Installation

1. To create, save, run, and ship containers, you'll need to install and run the [Spoonium Plugin](http://start.spoon.net/install) on any Windows machine or VM.
2. [Create an account or log in](http://spoon.net/sso/spoonium.net/login).

### Get going

Open a new command prompt and follow the example below.

	# Check the help documentation
	> spoon
	
	# Log in to your Spoonium account
	> spoon login username password

### Pull an  Image

Images are the building blocks for everything in Spoonium. They serve as a base (read-only) filesystem and registry that your application will use while running in a container.

We'll begin by pulling (downloading) an image from our remote registry, the [Spoonium Hub](http://spoonium.net/hub).

Let's start by pulling the **spoonbrew/scratch** image (named after the repository owner, **spoonbrew**, and the image name, **scratch**). The **scratch** image is completely empty and roughly equivalent to a freshly-installed, clean computer. 

```
# The `pull` command takes just a single parameter: the owner and name of the image.
> spoon pull spoonbrew/scratch

# When the image has finished downloading, you will see `Pull complete`.
> spoon pull spoonbrew/scratch

Pulling scratch:master from spoonbrew
Pull complete
```

**Note**: The **[spoonbrew](http://spoonium.net/hub/spoonbrew)** user account is maintained by the Spoon team. We provide a number of pre-configured images for popular runtimes, frameworks, and tools such as .NET, Java, and NodeJS. 

### Create a Container

A [container](http://spoonium.net/docs/about#Containers) is an isolated virtual environment consisting of an [image](http://spoonium.net/docs/about#Images) and the [Spoon VM](http://spoonium.net/docs/about#virtual+machine).

Let's create a new container using the `spoon run` command, which will bootstrap a new container from any specified image. Any parameters specified after the `<image>` will be passed to the startup file. 

For **spoonbrew/scratch**, the default startup file is **cmd.exe** (the command prompt). 

```
# Start your new container with a classic "Hello World!"
> spoon run -a spoonbrew/scratch echo Hello World!

Hello World! 

# Close that containerized command prompt.
(25fdso88) C:\spoonroot> exit

# Your container ID will appear in your remaining command prompt window. We'll talk more about that later.

25fdso8823fdsa734fdhasjd6588p098
```

Congratulations! You just ran your first container.

### Creating files within a container

In this example, we'll run a container and create a new text file within that container. 

```
# To begin, create a new containerized command prompt with the `run` command.
> spoon run spoonbrew/scratch
```

You should see a new command prompt appear. This prompt is running in the container. 

**Tip**: "Is my command prompt containerized, or not?" When the command prompt is running inside a Spoon container, you'll see the first 8 characters of the container ID in the prompt.

So, your native command prompt will look like this:

	C:\>

But a containerized command prompt will look something like this: 

	(87ddvf54) C:\>

Back to the tutorial :)


```
# Make a new directory in our container with the `mkdir` command.

# This directory will only be created *inside the container* and *not* on your local system. 
(87ddvf54) C:\>mkdir C:\spoonroot
```

```
# Navigate to that directory. 
(87ddvf54) C:\> cd C:\spoonroot

# To create a simple text file, pipe the output of an `echo` command to a file name.
(87ddvf54) C:\spoonroot> echo Hello World! > hello.txt
```


```
# Finally, close the command prompt, shutting down the container. 
(87ddvf54) C:\spoonroot> exit

# Your container ID will appear in your remaining command prompt.

87ddvf5455lp09xbenn71944c5dzzem5
```

#### Commit Changes and Push

Now it's time to memorialize your changes by creating a new image from the container.

```
# Bring up your full list of containers with `spoon containers`. Note your ID.
	> spoon containers
	
	ID            IMAGES                    COMMAND  CREATED
	87ddvf5455lp  spoonbrew/scratch:master  cmd      7/31/2014 9:20:18 AM
```
```
# Create a new image from your container with `spoon commit` and two parameters: at least two digits of the container ID, and the name for your image ("helloworld").
	> spoon commit 87ddv helloworld
	
	Commiting container 87ddvf5455lp to helloworld:HEAD
	Commit complete
```

```
# View the newly created image with the `spoon images` command, which returns a list of all images present on the local machine.
	> spoon images
	
	NAME                      SIZE   CREATED
	helloworld:head 		  0.1MB  7/31/2014 9:29:27 AM
	spoonbrew/scratch:head 	  0.0MB  7/31/2014 9:20:26 AM
```

```
# Upload the **helloworld** image to the Spoonium Hub with the `spoon push` command. By default, pushed images will be added to the user account of the logged-in user. 
	> spoon push helloworld

	Pushing image helloworld:head to spoonuser/helloworld

# When the image has finished uploading, `Push complete` will appear in the command prompt. 
	> spoon push helloworld
	
	Pushing image helloworld:head to spoonuser/helloworld
	Push complete
```

Once the `Push complete` message appears in your command prompt, the image is on the [Spoonium Hub](http://spoonium.net/hub), which functions similarly to a remote repository in Git - it allows your work to be accessed from any computer with access to the remote. You can view your new image by going to **http://spoonium.net/hub/[username]/helloworld**.

Repository pages on Spoonium serve as complete version histories of different images, just like remote repositories in Git, and every Spoonium user has an unlimited number of public repositories.

Public repositories are great for sharing work with others. They're a quick and easy access point for colleagues, collaborators, or end users to access, download, and run your project. Read more about repositories [here](http://spoonium.net/docs/hub#repositories).

### Next Steps 

Learn more about:

- [Building containers and advanced Spoonium commands](/docs/build).
- [Practical examples and use cases](/docs/samples), such as containerizing Java, Node, Python, and .NET projects. 

Enjoy!