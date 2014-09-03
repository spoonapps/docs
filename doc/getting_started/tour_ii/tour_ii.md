## Tour II - A Web Application

In this walkthrough, we will go over how to manipulate containers for the specific task of running web applications, specifically the blogging platform **[Ghost](http://ghost.org/)**, which is dependent on a Node JS server.

### Topics Covered

1. Copy data from one container to another.
2. Revert a container to its original state after making changes to the container.
3. Map ports between a container and the host.

### Create a Ghost Image

Open a new command prompt.

```	
# Log in to your Spoonium account
> spoon login username password

Logged in as username
```

Run some basic tools from the Spoonium Hub to create our Ghost image.

```
C:\> spoon run wget,7zip,node

# This will pull these images into a new containerized command prompt (as in Tour I).
```

In your container, create a directory with `mkdir` called "ghost" for the Ghost web application.

```
(c99f354f) C:\> mkdir ghost

#Change the current directory to "ghost" with `cd`.
(c99f354f) C:\> cd ghost

(c99f354f) C:\ghost>
```

Install Ghost into your container using your pulled images and the Ghost install URL.

```
(c99f354f) C:\ghost> C:\wget\wget.exe http://ghost.org/zip/ghost-0.5.1.zip --no-check-certificate
(c99f354f) C:\ghost> C:\7zip\7z.exe x ghost-0.5.1.zip

Everything is Ok
```

Install npm (Node Packaged Modules), the official package manager for NodeJS.
```
(c99f354f) C:\ghost> npm install --production
```

When it's all done, `exit` the container.

```
(c99f354f) C:\ghost> exit

# Your native command prompt will output a container ID and exit code:

c99f354fdf7847fe9be2261f8a475e15
Process returned exit code 0x0
```

In your native command prompt, `commit` to create the Ghost image.

```
# Like in Tour I, `commit` using your container ID and your new image name.
C:\>spoon commit c99f354f ghost:0.5.1

Committing container c99f354fdf7847fe9be2261f8a475e15 to image ghost:0.5.1
Commit complete
```

### Running the Ghost Web Application

```
# Once we have our Ghost image, let's `run` it.
C:\>spoon run ghost:0.5.1

# This will open a new containerized command prompt with Ghost running inside.
```

```
# Once in the container, go to the Ghost directory.
(eacc9518) C:\> cd ghost

(eacc9518) C:\ghost>

# Start the NodeJS server.
(eacc9518) C:\ghost> npm start --production

Your blog is now available on http://my-ghost-blog.com
Ctrl+C to shut down
```

Set up your Ghost blog account at **http://localhost:2368/admin**. The Ghost web application can then be used via any browser at **http://localhost:2368**. 

Go ahead and make your first post! :)

When you are done, press **Ctrl+C** to stop the server. Then terminate batch file and exit the container.

```
Ctrl+C
Terminate batch file (Y/N)? N

# Exit the container.
(eacc9518) C:\ghost> exit

# This will generate a new container ID for your Ghost container.

bc53e584fbf943098e7d0bf6109737eb
Process returned exit code 0xC000013A
```

### Copy Database

Now that we have a Ghost database created and filled with some data, let's **copy** it to a new container using the `spoon cp` command. We can use this container later as a backup or if we wanted to run multiple instances of Ghost.

First, `run` a new, blank container ("scratch") and get its container ID.

```
C:\>spoon run spoonbrew/scratch

# Exit from your new container.
(d65260ad) C:\> exit

# This will generate a new blank container ID.
d65260ad4c504381a34e21358b19307f
Process returned exit code 0x0
```

Next, use the spoon `cp` command to copy over the database file.

```
C:\> spoon cp d7df4eb9:c:\ghost\content\data\ghost.db d652:c:\ghost\content\data

# `Commit` the container as an image.
C:\>spoon commit d652 ghost-db

Committing container d65260ad4c504381a34e21358b19307f to image ghost-db
Commit complete
```

```
# Within the newly created container, `run` a new instance of ghost with the existing data.
C:\>spoon run ghost:0.5.1,ghost-db
```

### Revert Container to Original State

Imagine that you somehow made a mistake or the database got corrupted for some reason. Instead of trying to figure out where the problem is and attempting to clean your environment, which can take hours to do, you can simply `revert` the container to its original state with the spoon revert command.

```
# `Revert` the container to its original state using the container ID.
C:\>spoon revert eacc951825fb4892ae4663e7caf11d33
Deleted all changes in container eacc951825fb4892ae4663e7caf11d33

# `Start` that container again.
C:\>spoon start eacc951825fb4892ae4663e7caf11d33
```

### Running Multiple Instances with Port Mapping

Instead of dealing with a different config for your web application and having to figure out which one to use between production and test, you can use the port mapping feature to run multiple instances or without changing your config.

```
spoon run --route-add=8080:2368 ghost:0.5.1
spoon run --route-add=8081:2368 ghost:0.5.1
spoon run --route-add=8082:2368 ghost:0.5.1
```

Using this set of commands, you will not have three instances of the ghost application. Each instance will be accessible at port 808x on the host system, but all three instances of the application will think they are accessed at port 2368 internally. This is also useful when you do not want to keep a different config, for let's say production and development if they have different ports.

### Pulling it all together

Combining these features together allows you to do powerful things, such as running multiple versions of web applications with the same database snapshot image.

```
spoon run --route-add=8080:2368 ghost:0.5.0,ghost-db
spoon run --route-add=8081:2368 ghost:0.5.1,ghost-db
spoon run --route-add=8082:2368 ghost:0.5.2,ghost-db
```
