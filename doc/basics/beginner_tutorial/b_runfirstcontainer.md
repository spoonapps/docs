# Run Your First Container

Now that you're logged into Spoonium, you're ready to run your first container! We'll begin by pulling (downloading) an image from the Spoonium Hub. 

## Pull an  Image

Images are the building blocks for everything in Spoonium. They serve as a base (read-only) filesystem and registry that your application will use while running in a container. 

Since you don't have any images on your local machine yet, you'll need to pull one down from the remote registry at [http://spoonium.net/hub](http://spoonium.net/hub). We'll do this using the `spoon pull` command. 

The `pull` command takes a single parameter: the name of the image you want to pull from the remote registry. "Pull" is really just a fancy word for "copy." When an image is "pulled" from a remote registry, a copy of that image is downloaded to your local machine. 

Let's start simple by pulling the **spoonbrew/scratch** image. This image is completely empty: this is roughly equivalent to a freshly-installed, or "clean" computer. 

	>spoon pull spoonbrew/scratch

When the image has finished downloading, you will see `Pull complete` appear in the command prompt. 

	>spoon pull spoonbrew/scratch
	Pulling scratch:master from spoonbrew
	Pull complete

**Note**: The **spoonbrew** user account is maintained by the staff at Spoon. It provides a number of pre-configured images for popular runtimes, frameworks, and tools such as .NET, Java, and NodeJS. 

## Create a Container

To create a new container, use the `spoon run` command. The `run` command will bootstrap a new container from the specified image. Any parameters specified after the `<image>` will be passed to the startup file. 

For **spoonbrew/scratch**, the default startup file is **cmd.exe** (AKA "the command prompt"). We'll start our new container with a classic "Hello World!"

	>spoon run -a spoonbrew/scratch echo Hello World!

You should see the following output: 

	Hello World! 
	25fdso8823fdsa734fdhasjd6588p098

**Congratulations!** You just ran your first container! 

Before we go any further, let's backtrack and go over what just happened.

When the `run` command was executed, a new container was created and a new, containerized command prompt executed the command `echo Hello World!`. The command prompt process then dies and the container stops. When the container stops, it's 32-character ID is printed to the command prompt.

In this case, we also specified the `-a` flag. This will `attach` the native command prompt to the virtual container's `STDIN`, `STDOUT`, and `STDERR` streams, redirecting them back to the native prompt. If you didn't `attach`, you'd see a new command prompt briefly appear on your screen. 

## A More Intricate Example

That example was a little simple -- let's do something slightly more interesting before moving on. In this example, we'll run a container and create a new file within that container. 

To begin, create a new container with the run command. This time, we just want to start a command prompt without executing a command.

	>spoon run spoonbrew/scratch

You should see a new command prompt appear. This prompt is running in the container. 

**Note**: An easy way to tell if a command prompt is containerized or not is by looking at the prompt. Spoon will prepend the first 8 characters of the container ID to the prompt whenever the command prompt is running inside a Spoon container. Whereas your native command prompt will look something like this:

	C:\>

a containerized command prompt will look like this: 

	(87ddvf54) C:\>

Now, let's create a new directory in our container with the `mkdir` command. This directory will only be created *inside the container* and not on your local system. 

	(87ddvf54) C:\>mkdir C:\spoonroot

Now, navigate to that directory. To create a simple text file, pipe the output of an `echo` command to a file name (the file will be created for you, if it doesn't already exist). 

	(87ddvf54) C:\>cd C:\spoonroot
	(87ddvf54) C:\spoonroot>echo Hello World! > hello.txt

Finally, we'll close the command prompt, shutting down the container. 

	(87ddvf54) C:\spoonroot>exit
	87ddvf5455lp09xbenn71944c5dzzem5


	
	