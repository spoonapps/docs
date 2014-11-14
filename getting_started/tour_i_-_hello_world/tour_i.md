## Tour I - Hello World!

### Installation

1. To create, save, run, and ship containers, you'll need to install and run the [Spoon plugin](http://start.spoon.net/install) on any Windows machine or VM.
2. [Create an account or log in](/login?return_to=/docs#try-it).

### Get Going

Open a new command prompt and follow the example below.

	# Check the help documentation.
	> spoon

	Available commands are:
	(Command list)
	
	# Log in to your Spoon account.
	> spoon login username password

	Logged in as username

### Pull an Image

We'll begin by pulling (downloading) a blank image from our remote registry, the Spoon Hub.

```
> spoon pull spoonbrew/clean

Pulling clean
Pull complete
```

Let's analyze this command:

```
spoon pull			# The pull command adds an image to your Spoon account.
spoonbrew/clean	# Specify the repository owner, "spoonbrew," and the image name, "clean."
```

There you go! If it worked as expected, you just pulled the **clean** image into your account; the clean image is completely empty and roughly equivalent to a freshly-installed, clean OS. You're ready to create your first container!

**Note**: The **[spoonbrew](/hub/spoonbrew)** user account is maintained by the Spoon team. We provide a number of preconfigured images for popular runtimes, frameworks, and tools such as .NET, Java, and NodeJS. 

### Create a Container

Let's create a new container using the `spoon run` command, which will bootstrap a new container from any specified image. Any parameters specified after the `<image>` will be passed to the startup file. 

For **spoonbrew/clean**, the default startup file is **cmd.exe** (the command prompt). 

```
> spoon run spoonbrew/clean echo Hello World!

# A new, containerized command prompt will appear with your output:

Hello World! 
```

```
# Exit the new containerized command prompt.
(25fdso88) C:\spoonroot> exit
```

```
# Your container ID will appear in your remaining command prompt window.

25fdso8823fdsa734fdhasjd6588p098
```

Let's break down what just happened:

```
spoon run			# Here we tell Spoon to kick off a new container with a specified image.
spoonbrew/clean	# Our desired repo owner, "spoonbrew," and the repo/image name, "clean."
echo Hello World!	# Command your container to start up with "Hello World!"
exit				# This closes your container and generates your container ID.
25fdso88...			# This output identifies the specific container you just ran.
```

Congratulations! You just ran your first container.

### Creating Files within a Container

In this example, we'll run a container and create a new text file within that container. 

```
# To begin, create a new containerized command prompt with the `run` command.
> spoon run spoonbrew/clean
```

You should see a new command prompt appear. This prompt is running in the container. 

**"Is my command prompt containerized, or not?"**

When the command prompt is running inside a Spoon container, you'll see the first 8 characters of the container ID in the prompt.

So, your **native** command prompt will look like this:

	C:\>

But a **containerized** command prompt will look something like this: 

	(87ddvf54) C:\>

In our container, let's make a new directory called "spoonroot" with the `mkdir` command.

```
(87ddvf54) C:\> mkdir C:\spoonroot
```

This directory will only be created *inside the container* and *not* on your local system, illustrated by viewing our containerized vs. native directories after executing the `mkdir` command:

```
# In the native command prompt:
C:\> dir

Directory of C:\Users\username
<DIR>          Desktop
<DIR>          Documents
<DIR>          Downloads

# In the container:
(87ddvf54) C:\> dir

Directory of C:\
<DIR>          Windows
<DIR>          spoonroot
```

Change to your new directory with the `cd` command.

```
(87ddvf54) C:\> cd C:\spoonroot

(87ddvf54) C:\spoonroot>
```

Create a simple text file by piping the `echo` command to the file name "hello.txt"

```
(87ddvf54) C:\spoonroot> echo Hello World! > hello.txt
```

Finally, `exit` the command prompt, shutting down the container. 

```
(87ddvf54) C:\spoonroot> exit

# Your container ID will appear in your remaining command prompt.

87ddvf5455lp09xbenn71944c5dzzem5
```

#### Commit Changes and Push

Now it's time to memorialize and share your changes by creating a new image from the container. Bring up your full list of containers with `spoon containers`. Note your ID.

```
> spoon containers
	
ID            Images                    Command  		    Created
87ddvf5455lp  spoonbrew/clean         echo Hello Wor  7/31/2014 9:20:18 AM
```

Turn your container into a new image with `spoon commit`.

```
> spoon commit 87ddv helloworld
	
Committing container 87ddvf5455lp to image helloworld
Commit complete
```

Let's analyze what just happened:

```
spoon commit	# The `commit` command creates a new image from a specified container.
87ddv			# Specify the container with at least 2 digits of the container ID.
helloworld		# The name you'd like for your new image.
```

View the newly created image with the `spoon images` command, which returns a list of all images present on the local machine.

```
> spoon images
	
Name                    Created					Size
helloworld		 		7/31/2014 9:29:27 AM	0.1MB
spoonbrew/clean	 	7/31/2014 9:20:26 AM	0.0MB
```

Upload the **helloworld** image to the Spoon Hub with the `spoon push` command.

```
> spoon push helloworld

Pushing image helloworld to spoonuser/helloworld
Push complete
Image is public
```

Congrats on your first push! What just happened?

```
spoon push		# The push command commits any image to the Spoon Hub.
Push complete	# Signals the image has uploaded.
Image is public	# Pushed images are publicly added to the account of the logged-in user.
```

Once the `Push complete` message appears in your command prompt, the image is on the [Spoon Hub](/hub), which functions similarly to a remote repository in Git - it allows your work to be accessed from any computer with access to the remote. You can view your new image by going to https://spoon.net/hub/[*username*]/helloworld.

Repository pages on Spoon serve as complete version histories of different images, just like remote repositories in Git, and every Spoon user has an unlimited number of public repositories.

Public repositories are great for sharing work with others. They're a quick and easy access point for colleagues, collaborators, or end users to access, download, and run your project. Read more about repositories [here](/docs/hub/repositories).