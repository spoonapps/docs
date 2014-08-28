## Try It!

### Installation

1. Install and run the [Spoonium Plugin](http://start.spoon.net/install) to create, save, run, and ship application containers.
2. [Create an account or log in](http://spoon.net/sso/spoonium.net/login).

### Get going

Open a new command prompt and follow the example below.

	# Check the help documentation
	> spoon
	
	# Log in to your Spoonium account
	> spoon login myusername mypassword

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

# You should see the following output: 
Hello World! 
25fdso8823fdsa734fdhasjd6588p098
```

Congratulations! You just ran your first container! 

Before we go any further, let's backtrack and go over what just happened.

1. When the `run` command was executed, a new container was created and a new, *containerized* command prompt executed the command `echo Hello World!`.
2. The command prompt process then died and the container stopped.
3. When the container stopped, its 32-character ID was printed to the new command prompt.

In this case, we also specified the **`-a` flag**. This will `attach` the native command prompt to the virtual container's `STDIN`, `STDOUT`, and `STDERR` streams, redirecting them back to the native prompt. If you didn't `attach`, you would have seen a new command prompt briefly appear on your screen.

### Creating files within a container

In this example, we'll run a container and create a new text file within that container. 

```
# To begin, create a new containerized command prompt with the `run` command.
> spoon run spoonbrew/scratch
```

You should see a new command prompt appear. This prompt is running in the container. 

**Tip**: An easy way to tell if a command prompt is containerized is to look at the prompt. When the command prompt is running inside a Spoon container, Spoon will prepend the first 8 characters of the container ID to the prompt.

So, your native command prompt will look like this:

	C:\>

But a containerized command prompt will look something like this: 

	(87ddvf54) C:\>

Moving on...


```
# Create a new directory in our container with the `mkdir` command ("make directory").
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
87ddvf5455lp09xbenn71944c5dzzem5
```

#### Commit Changes and Push

Now it's time to memorialize your changes by creating a new image from the container.

To do create an image from an existing container, use the `spoon commit` command. 

First, let's remind ourselves of the ID of the last container we ran. We can do this with the `spoon ps -l` command, which will return the metadata for the last container created on the local machine.

	> spoon containers
	
	ID            Images                    Command  Created
	87ddvf5455lp  spoonbrew/scratch:master  cmd      7/31/2014 9:20:18 AM

We can create a new image by from a container using the `spoon commit` command. The `commit` command takes two parameters: the ID of the container to commit, and the name for the new image you'd like to create. For this tutorial, we'll name the image hello-world.

	> spoon commit 87ddv helloworld
	
	Commiting container 87ddvf5455lp to helloworld:HEAD
	Commit complete

You can view the newly created image by running the `spoon images` command. This command returns a table listing all of the images present on the local machine.

	> spoon images
	
	Name                      Size   Created
	helloworld:head 		  0.1MB  7/31/2014 9:29:27 AM
	spoonbrew/scratch:head 	  0.0MB  7/31/2014 9:20:26 AM

We'll finish this tutorial by uploading the newly created image to the [Spoonium Hub](http://spoonium.net/hub). The Spoonium Hub functions similarly to a remote repository in Git – allowing your work to be accessed from any computer with access to the remote. All Spoonium accounts come with an unlimited number of public repositories. 

**Note**: Private repositories can also be hosted on the Spoonium Hub. For more information, see [pricing](http://spoonium.net/pricing). 

To upload the **helloworld** image, use the `spoon push` command. 

	> spoon push helloworld:head

By default, images will be pushed to the user account of the logged-in user. 

	> spoon push helloworld:head
	
	Pushing image helloworld:head to spoonuser/helloworld

When the image has finished uploading, `Push complete` will appear in the command prompt. 

	> spoon push helloworld:head
	
	Pushing image helloworld:head to spoonuser/helloworld
	Push complete

Once the `Push complete` message appears in your command prompt, the image is on the Spoonium Hub. You can view the image by going to http://spoonium.net/hub/[your username]/helloworld. 

If your account did not already have an existing repository named `helloworld`, Spoonium automatically created one and added the image to it.

The repository page on Spoonium serves as a complete version history of an image. If you're familiar with remote repositories in Git, Spoonium is *very* similar. 

Public repositories are great for sharing work with others or for providing a quick and easy access point for colleagues, collaborators, or even end-users to download and access and run your project from. 

### Next Steps 

Learn more about:

- [Building containers and advanced Spoonium commands](/docs/build).

- [Practical examples and use cases](/docs/samples), such as containerizing Java, Node, Python, and .NET projects. 

Enjoy!