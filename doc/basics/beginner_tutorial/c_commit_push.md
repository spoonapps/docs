# Commit Changes and Push

Now it's time to memorialize your changes by creating a new image from the container.

## Commit

To do create an image from an existing container, use the `spoon commit` command. 

First, let's remind ourselves of the ID of the last container we ran. We can do this with the `spoon ps -l` command, which will return the metadata for the last container created on the local machine.

	>spoon ps -l
	ID            IMAGES                    COMMAND  CREATED
	87ddvf5455lp  spoonbrew/scratch:master  cmd      7/31/2014 9:20:18 AM

We can create a new image by from a container using the `spoon commit` command. The `commit` command takes two parameters: the ID of the container to commit, and the name for the new image you'd like to create. For this tutorial, we'll name the image hello-world.

	>spoon commit 87ddv hello-world
	Commiting container 87ddvf5455lp to hello-world:HEAD
	Commit complete

## View Local Images

You can view the newly created image by running the `spoon images` command. This command returns a table listing all of the images present on the local machine.

	>spoon images
	NAME                      SIZE   CREATED
	local/hello-world:master  0.1MB  7/31/2014 9:29:27 AM
	spoonbrew/scratch:master  0.0MB  7/31/2014 9:20:26 AM

## Push

We'll finish this tutorial by uploading the newly-created image to the [Spoonium Hub](http://spoonium.net/hub). The Spoonium Hub functions similarly to a remote repository in Git – allowing your work to be accessed from any computer with access to the remote. All Spoonium accounts come with an unlimited number of public repositories. 

**Note**: Private repositories can also be hosted on the Spoonium Hub. For more information, see [pricing](http://spoonium.net/pricing). 

To upload the **hello-world** image, use the `spoon push` command. 

	>spoon push hello-world:head

By default, images will be pushed to the user account of the logged-in user. 

	>spoon push hello-world:head
	Pushing image hello-world:head to spoonuser/hello-world

When the image has finished uploading, `Push complete` will appear in the command prompt. 

	>spoon push hello-world:head
	Pushing image hello-world:head to spoonuser/hello-world
	Push complete

## View Remote Images
	
Once the `Push complete` message appears in your command prompt, the image is on the Spoonium Hub. You can view the image by going to http://spoonium.net/hub/<your username>/hello-world. 

If your account did not already have an existing repository named `hello-world`, Spoonium automatically created one and added the image to it.

The repository page on Spoonium serves as a complete version history of an image. If you're familiar with a `Git` remote repository, Spoonium is *very* similar. 

Public repositories are great for sharing work with others or for providing a quick and easy access point for colleagues, collaborators, or even end-users to download and access and run your project from. 
