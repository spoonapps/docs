# Running the Container

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