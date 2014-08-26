## Try It!

### Pull an  Image

We'll begin by pulling (downloading) an image from the Spoonium Hub. Images are the building blocks for everything in Spoonium. They serve as a base (read-only) filesystem and registry that your application will use while running in a container. 

Because you don't have any images on your local machine yet, you'll need to pull one from the remote registry at [http://spoonium.net/hub](http://spoonium.net/hub). We'll do this using the `spoon pull` command. 

The `pull` command takes a single parameter: the name of the image you want to pull from the remote registry. "Pull" is really just a fancy word for "copy." When an image is "pulled" from a remote registry, a copy of that image is downloaded to your local machine. 

Let's start simple by pulling the **spoonbrew/scratch** image. This image is completely empty: this is roughly equivalent to a freshly-installed, or "clean" computer. 

	> spoon pull spoonbrew/scratch

When the image has finished downloading, you will see `Pull complete` appear in the command prompt. 

```Batchfile
> spoon pull spoonbrew/scratch
Pulling scratch:master from spoonbrew
Pull complete
```

**Note**: The **spoonbrew** user account is maintained by the staff at Spoon. It provides a number of pre-configured images for popular runtimes, frameworks, and tools such as .NET, Java, and NodeJS. 

### Create a Container

To create a new container, use the `spoon run` command. The `run` command will bootstrap a new container from the specified image. Any parameters specified after the `<image>` will be passed to the startup file. 

For **spoonbrew/scratch**, the default startup file is **cmd.exe** (AKA "the command prompt"). We'll start our new container with a classic "Hello World!"

	> spoon run -a spoonbrew/scratch echo Hello World!

You should see the following output: 

	Hello World! 
	25fdso8823fdsa734fdhasjd6588p098

**Congratulations!** You just ran your first container! 

Before we go any further, let's backtrack and go over what just happened.

When the `run` command was executed, a new container was created and a new, containerized command prompt executed the command `echo Hello World!`. The command prompt process then dies and the container stops. When the container stops, it's 32-character ID is printed to the command prompt.

In this case, we also specified the `-a` flag. This will `attach` the native command prompt to the virtual container's `STDIN`, `STDOUT`, and `STDERR` streams, redirecting them back to the native prompt. If you didn't `attach`, you'd see a new command prompt briefly appear on your screen. 

### Creating files within a container

In this example, we'll run a container and create a new file within that container. 

To begin, create a new container with the run command. This time, we just want to start a command prompt without executing a command.

	> spoon run spoonbrew/scratch

You should see a new command prompt appear. This prompt is running in the container. 

**Note**: An easy way to tell if a command prompt is containerized or not is by looking at the prompt. Spoon will prepend the first 8 characters of the container ID to the prompt whenever the command prompt is running inside a Spoon container. Whereas your native command prompt will look something like this:

	C:\>

a containerized command prompt will look like this: 

	(87ddvf54) C:\>

Now, let's create a new directory in our container with the `mkdir` command. This directory will only be created *inside the container* and not on your local system. 

	(87ddvf54) C:\>mkdir C:\spoonroot

Now, navigate to that directory. To create a simple text file, pipe the output of an `echo` command to a file name (the file will be created for you, if it doesn't already exist). 

	(87ddvf54) C:\> cd C:\spoonroot
	(87ddvf54) C:\spoonroot> echo Hello World! > hello.txt

Finally, we'll close the command prompt, shutting down the container. 

	(87ddvf54) C:\spoonroot> exit
	87ddvf5455lp09xbenn71944c5dzzem5

#### Commit Changes and Push

Now it's time to memorialize your changes by creating a new image from the container.

To do create an image from an existing container, use the `spoon commit` command. 

First, let's remind ourselves of the ID of the last container we ran. We can do this with the `spoon ps -l` command, which will return the metadata for the last container created on the local machine.

	> spoon containers
	ID            IMAGES                    COMMAND  CREATED
	87ddvf5455lp  spoonbrew/scratch:master  cmd      7/31/2014 9:20:18 AM

We can create a new image by from a container using the `spoon commit` command. The `commit` command takes two parameters: the ID of the container to commit, and the name for the new image you'd like to create. For this tutorial, we'll name the image hello-world.

	> spoon commit 87ddv helloworld
	Commiting container 87ddvf5455lp to helloworld:HEAD
	Commit complete

You can view the newly created image by running the `spoon images` command. This command returns a table listing all of the images present on the local machine.

	> spoon images
	NAME                      SIZE   CREATED
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