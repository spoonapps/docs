## Tour II - A Web Application

In this walkthrough, we will go over how to manipulate containers for the specific task of web applications, specifically Ghost on a Node JS server. We will learn how to revert a container's state, share data between containers, and map ports to help out with any testing task.

### Topics Covered

1. Copy data from one container to another
2. Revert a container to its original state
3. Map ports between a container and the host

### Create a Ghost Image
```
# Open a new command prompt
	
# Log in to your Spoonium account
> spoon login username password
```

```
# Run some basic tools from the Spoonium Hub to create our Ghost image.
C:\>spoon run wget,7zip,node

# This will open a new containerized command prompt (as in Tour I).
```

```
# Once in the container, create a directory with `mkdir` for the Ghost web application and install it.
(c99f354f) C:\>mkdir ghost
(c99f354f) C:\>cd ghost
(c99f354f) C:\ghost>%spoon_wget% http://ghost.org/zip/ghost-0.5.1.zip --no-check-certificate
(c99f354f) C:\ghost>%spoon_7z% x ghost-0.5.1.zip
(c99f354f) C:\ghost>npm install --production

# When it's all done, `exit` the container.
(c99f354f) C:\ghost>exit


# Your native command prompt will show something like:

C:\>spoon run wget,7zip,node

c99f354fdf7847fe9be2261f8a475e15
Process returned exit code 0x0
```

```
# In your native command prompt, `commit` to create the Ghost image.
C:\>spoon commit c99f354f ghost:0.5.1

Committing container c99f354fdf7847fe9be2261f8a475e15 to image ghost:0.5.1
Commit complete
```

### Running the Ghost Web Application

```
# Once we have our Ghost image, let's `run` it.
C:\>spoon run ghost:0.5.1

eacc951825fb4892ae4663e7caf11d33
Process returned exit code 0x0

# This will open a new containerized command prompt.
```

```
# Once in the container, go to the Ghost directory and start the Node JS server.
(eacc9518) C:\>cd ghost
(eacc9518) C:\ghost>npm start --production
```

The Ghost web application can be accessed via any browser at **http://localhost:2368**, but you should first set up your account at **http://localhost:2368/admin**.

Go ahead and make your first post! :)

```
# When you are done, press Ctrl+C to stop the server and exit the container.
Ctrl+C
(eacc9518) C:\ghost>exit
```

### Copy Database

Now that we have a Ghost database created and filled with some data, let's copy it to a new container using the spoon cp command. We can use this container later as a backup or when running multiple instances.

```
# First, `run` a blank container ("scratch").
C:\>spoon run scratch

d65260ad4c504381a34e21358b19307f
Process returned exit code 0x0
```

```
# Next, use the spoon `cp` command to copy over the database file.
C:\>spoon cp d7df4eb9:c:\ghost\content\data\ghost.db d652:c:\ghost\content\data

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
spn run --route-add=8080:2368 ghost:0.5.1
spn run --route-add=8081:2368 ghost:0.5.1
spn run --route-add=8082:2368 ghost:0.5.1
```

Using this set of commands, you will not have three instances of the ghost application. Each instance will be accessible at port 808x on the host system, but all three instances of the application will think they are accessed at port 2368 internally. This is also useful when you do not want to keep a different config, for let's say production and development if they have different ports.

### DNS Virtualization -> for later with linking

This is also useful when you do not want to keep a different config, for let's say production and development if they have different ports.

```
spn run --hosts=127.0.0.1:myghostblog.com ghost:0.5.1
spn run --link=[ghost]:server firefox:31
```

### Pulling it all together

Combining these features together allows you to do powerful things, such as running multiple versions of web applications with the same database snapshot image.

```
spn run --route-add=8080:2368 ghost:0.5.0,ghost-db
spn run --route-add=8081:2368 ghost:0.5.1,ghost-db
spn run --route-add=8082:2368 ghost:0.5.2,ghost-db
```
