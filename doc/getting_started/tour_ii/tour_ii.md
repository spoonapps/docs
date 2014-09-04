## Tour II - A Web Application

Spoonium gives users the tools to easily test and deploy web applications. In this example, we will use the popular **[Ghost](http://ghost.org/)** web blogging application to showcase the features of the Spoonium system that make it particularly useful for this purpose.

### Topics Covered

```
1. Creating a new web application image by combining base images
2. Running a web application image
3. Running multiple instances of a web application with the help of port mapping
4. Copying data from one container to another
5. Layering images (adding multiple images to a container)
6. Reverting a container to its original state
```

### Create a Ghost Image

Let's start by opening a new command prompt and logging in the Spoonium Hub.

```	
# Log in to your Spoonium account
C:\> spoon login username password

Logged in as username
```

For this Ghost example, we will need to start our container with some basic utilities, such as wget and 7zip. We  will also pull and run the NodeJS server, which is required for the Ghost application. For this, we'll use `spoon run`, which will automatically pull the named images and begin running them in a new containerized command prompt.

```
# Create a new container with basic utilities and the Node JS server.
C:\> spoon run wget,7zip,node

Downloading wget:head from https://spoonium.net/users/spoonbrew
Downloading 7zip:head from https://spoonium.net/users/spoonbrew
Downloading node:head from https://spoonium.net/users/spoonbrew

# This will pull these images into a new containerized command prompt (as shown in Tour I).
```

Let's analyze this command:

```
spoon run

# Unlike Tour I, we skipped the `spoon pull` command. Why?
# `spoon run` will simultaneously download and run images in a new container.

wget,7zip,node

# Unlike Tour I, we have omitted the "owner/" namespace from image names. Omitting the namespace causes the Spoon IDE to first search for the named images on your local machine's image repository.
# If it doesn't find a match locally, the IDE then automatically searches for the images in the spoonbrew account on the Spoonium Hub, as it did in this example.
```

In your container, make a directory for the Ghost web application.

```
# Create "ghost" directory.
(c99f354f) C:\> mkdir c:\ghost

# Change the current directory to "ghost" with `cd` command.
(c99f354f) C:\> cd c:\ghost

(c99f354f) C:\ghost>

# Like Tour I, this directory exists inside your container - not on your local system.
```

Download the Ghost application into your container. Although we use the **--no-check-certificate** flag as a shortcut in this example, you should be validating SSL connections against a real certificate in a production environment.

```
# Using wget, download and install the Ghost web application with the included tools.
(c99f354f) C:\ghost> C:\wget\wget.exe http://ghost.org/zip/ghost-0.5.1.zip --no-check-certificate

'ghost-0.5.1.zip' saved

# Using 7zip, extract the Ghost application.
(c99f354f) C:\ghost> C:\7zip\7z.exe x ghost-0.5.1.zip

Everything is Ok

# Using NodeJS npm (Node Package Manager) tool, install the ghost application in production mode.
(c99f354f) C:\ghost> npm install
```

When it's all done, `exit` the container.

```
(c99f354f) C:\ghost> exit

# Your native command prompt will output a "Ghost container" ID and exit code:

c99f354fdf7847fe9be2261f8a475e15
Process returned exit code 0x0
```

In your native command prompt, `commit` the container to create the Ghost image.

```
# Like in Tour I, `commit` using your partial container ID and your chosen name for your new image.
C:\>spoon commit c99f354f ghost:0.5.1

Committing container c99f354fdf7847fe9be2261f8a475e15 to image ghost:0.5.1
Commit complete
```

### Running the Ghost Web Application

Once we have created our Ghost image, we can `run` it.

```
C:\>spoon run ghost:0.5.1

# This will initialize a fresh container using our newly created Ghost image.
```

Once in the container, start the Ghost web application with the NodeJS server.

```
# Change to the ghost directory.
(bc53e584) C:\> cd C:\ghost

# Start the NodeJS server.
(bc53e584) C:\ghost> npm start

Ghost is running in development...

# Your blog is now available on http://localhost:2368
```

Set up your Ghost blog account at **http://localhost:2368/admin**.

Go ahead and make your first post! :) Don't forget to save and publish it.

Your Ghost web application can then be used via any browser at **http://localhost:2368**.

![](/components/docs/quick_start/tour_ii/ghost-first-post.png)

When you are done, press **Ctrl+C** to stop the server, then `exit` the container.

```
# Ctrl+C to shut down. No need to terminate batch file.
Ctrl+C
Terminate batch file (Y/N)? N

# Exit the container to get the ID for your new Ghost container, which now has data in it.
(bc53e584) C:\ghost> exit

bc53e584fbf943098e7d0bf6109737eb
Process returned exit code 0xC000013A
```

This container ID will be used in later sections.

### Running Multiple Instances

Imagine that you needed to run or test multiple instances of the same application. In a typical scenario, you would have to create modified images that have individual configurations and would have to maintain these configurations after each update.

However, with the help of port mapping, we can run multiple instances of the Ghost web application image without having to do any of that. Simply map a host port to your application's internal port and you are ready to go. No mess, no fuss.

```
# Create a container that maps port 8080 on the host to port 2368 on the container
spoon run --route-add=8080:2368 ghost:0.5.1

# Create a container that maps port 8081 on the host to port 2368 on the container
spoon run --route-add=8081:2368 ghost:0.5.1

# Create a container that maps port 8082 on the host to port 2368 on the container
spoon run --route-add=8082:2368 ghost:0.5.1
```

Then use the commands to start the Ghost web application in each container, to make all three instances accessible.

```
# Change the current directory to where Ghost is installed and start the server
(cont808x) C:\> cd C:\Ghost & npm start
```

Using this set of commands, we create three containers using the same image. The application operates on the 2368 port internally, but is accessible via the 808x port that is assigned to it on the host.

![](/components/docs/quick_start/tour_ii/multiple.png)

### Saving a Database to a Layer

Now that we have a Ghost database created and filled with some data, let's **copy** it to a new container using the `spoon cp` command. We can convert this container later to an image and use it as a backup, or to layer existing data on top of a clean ghost image.

Saving a database to a layer can help you test different application versions against the same database, back up databases in case an app breaks something, test against new/old database versions, and change a database during development without messing with a "master" database.

First, we will need to create a blank container that will hold the database.

```
# Create a container from scratch
C:\> spoon run spoonbrew/scratch

# Exit the container to get your blank container ID.
(d65260ad) C:\> exit

d65260ad4c504381a34e21358b19307f
Process returned exit code 0x0
```

Next, use the spoon `cp` command to copy the database from the Ghost container (bc53e584 Running the Ghost Web Application) to the blank container.

```
C:\> spoon cp bc53e584:c:\ghost\content\data d65260ad:c:\ghost\content\data

# `Commit` the container as an image.
C:\> spoon commit d65260ad ghost-db

Committing container d65260ad4c504381a34e21358b19307f to image ghost-db
Commit complete
```

Create a new container using the ghost image with the database layered on top of it.

```
# Create a ghost container with ghost-db layered on top of it.
# Since the 2368 port is already taken, we'll also map a new port to the container.
C:\> spoon run --route-add=8083:2368 ghost:0.5.1,ghost-db
```

Start the NodeJS server and verify that the blog has the database.

```
(9a82febf) C:\> cd ghost & npm start
```

![](/components/docs/quick_start/tour_ii/ghost-first-post-2.png)

### Reverting the Container

We can use the `spoon revert` command to restore a container to its original state.

Let's go back to our original container and try this.

```
# `Revert` the container to its original state using the container ID.
C:\> spoon revert bc53e584

Deleted all changes in container bc53e584fbf943098e7d0bf6109737eb

# `Start` that container again.
C:\> spoon start bc53e584
```

Change directory to Ghost and start the server.

```
(bc53e584) C:\> cd ghost & npm start

# When you visit the website, the Ghost web application should be reverted to its original state.
```

![](/components/docs/quick_start/tour_ii/ghost-revert.png)

This command is especially useful if your database was somehow corrupted or an unrecoverable error made your web application unusable. Instead of trying to figure out where the problem is and attempting to clean your environment, which can take hours to do, you can simply `revert` the container to its original state with the `spoon revert` command.

### Pulling It All Together

Imagine that you have a live environment with a production, testing, and developing instance of the Ghost web application. You can use the port mapping and layering technique to run all three environments using the same database and the same config on the same machine. This eliminates the need for extra server machines, as well as the risk when deploying due to config mismanagement, and you can easily spin up more instances and tear down unneeded ones.

```
# Create a Ghost 0.5.0 instance using the same database and config on port 9090
spoon run --route-add=9090:2368 ghost:0.5.0,ghost-db,ghost-config

# Create a Ghost 0.5.1 instance using the same database and config on port 9091
spoon run --route-add=9091:2368 ghost:0.5.1,ghost-db,ghost-config

# Create a Ghost 0.5.2 instance using the same database and config on port 9092
spoon run --route-add=9092:2368 ghost:0.5.2,ghost-db,ghost-config
```
