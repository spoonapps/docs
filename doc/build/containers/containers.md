Containers form the backbone of the Spoonium ecosystem. In this section, we'll walk you through the many ways to work with and manage containers once they've been created with the `spoon run` command. 

The easiest way to tell if you are inside a container is to check your prompt. When a command prompt exists within a container, the prompt is prepended by the first 8 characters of the container's ID.


	>spoon start 8dpp9e
	
	(8dpp9eb5) >

Once inside a container, you can edit and modify the container's virtual filesystem and registry using the same command-line interfaces as are available in the Windows Command Prompt.

To "break out" of a container, kill any running processes inside that container. For example, if running a command prompt inside a container, to stop the container type `exit` or press Ctrl-C.

## Creating Containers

Containers are created with the `spoon run` command. 

The `spoon run` command has 2 required parameters: 

1. An `<image>` (or `<**images>`). All containers require a **base image** to run on top of. The image specified here will serve as this base for the newly created container. 
2. The `<command>` to start the container. 

The `<command>` should be of the form: `<executable> <**args>`. The executable may be any executable in the **base image**, `cmd.exe`, or any other valid Windows utility. 

For example, to create a new container using the `spoonbrew/scratch` image and the command `cmd.exe`, execute:
	
	spoon run spoonbrew/scratch cmd.exe

This command will create a new container with a command prompt running *within* that container. Thus, any operations done in the commmand prompt will be applied to the container environment, not the host system. 

The container will continue to run for as long as the command prompt stays open.

Sometimes one of `<executable>` `<**args>` may be same as `spoon` argument. To prevent `spoon` from treating this argument as its own prefix `<**args>` with a `--` mark. For example:

    spoon run spoonbrew/scratch cmd.exe /d
    spoon run spoonbrew/scratch cmd.exe -- /d 

First command passes `/d` to `spoon` and executes container in detached mode. Second one passes `/d` to `cmd.exe` so it does not execute `AutoRun` command from registry. Good practice is to always use `--` mark before arguments.

## Container Lifecycle

The lifecycle of a container is controlled by the processes within that container. When the process within a container exits or completes, the container stops running.

Take, for example, this command for starting a new container:

	C:\>spoon run -a spoonbrew/scratch cmd.exe -- /c echo hello world
	hello world
	641bad5a7f904442a399a32f301ba8ed
	C:\>

In this case, we started a new command prompt, executed the command `echo hello world`, and then, because the `/c` flag was specified, the command window closed. Once this process died, the container was automatically stopped and its ID was returned to the native prompt. 

Now, compare this behavior to if the `/k` flag was specified for `cmd.exe`: 

	C:\>spoon run -a spoonbrew/scratch cmd.exe -- /k echo hello world
	hello world
	(641bad5a) C:\>

In this case, we started a new command prompt and again executed echo hello world. This time, however, we specified the `/k` flag to keep the command prompt open after the echo command finished execution. Because the `cmd.exe` process in the container is still running, the container continues running. We can continue to execute commands in the container and it will continue to run until the contained command prompt process exits.

	(641bad5a) C:\>echo hello again
	hello again
	(641bad5a) C:\>exit
	641bad5a7f904442a399a32f301ba8ed
	C:\>

Processes within a container are run as child processes of the **Spoon VM** executable, which manages the container environment. 

A container with running processes can be forcefully stopped with the `spoon stop` command. The `stop` command takes a single parameter -- the ID of the container to stop. This command will stop the **Spoon VM** process that manages the container along with any of its child processes -- thus shutting down the container. 

## Starting Containers from the Command Line

Alternatively, stopped containers can also be restarted with the `spoon start` command. Like the `stop` command, the `start` command accepts a single parameter -- a container ID. When a container is restarted with `start`, it uses the same startup command as specified when the container was originally created with `spoon run`. 

Take, for example, a container with ID `55djk3x1` created with the command: `spoon run spoonbrew/scratch cmd.exe -- /c echo hello world`. This container will start, execute `echo hello world` in a new command prompt, and then shut down. 

If this container were to then be restarted with the command: `spoon start 55djk3x1`, a new command prompt would be spawned, the command `echo hello world` would execute, and the container would shut down. 

## Managing Containers

Containers can be tracked and managed through the spoon ps command. This command will list all of the currently-running containers on the local machine. The spoon ps command produces a tabular output listing the container's ID, date/time of creation, the base image, and the command the container was started with.

	>spoon containers

	ID           IMAGES              COMMAND       CREATED          STATUS
	03bddd8bef   spoonbrew/scratch   cmd           8/14/2014 1:03   Running
	52hd888xa3   local/server-app    startup.bat   8/14/2014 1:00   Running

To view all of the containers, both running and stopped, use the `-a` flag. 

	>spoon containers -a

If your container has multiple processes with transient lifetimes, it may be useful to view which processes are, at a given point in time, running within a container. 

The Spoon IDE exposes this ability through the `top` command. The `top` command will list and detail all of the running processes in a container.

To view the running processes in a given container, execute `spoon top <id of the container to view>`. 

#### Removing Containers

Containers can be removed, or deleted, from your local registry using the spoon rm command. The spoon rm takes one of two possible parameters:

- The **ID** of the container to remove. The Spoon IDE uses prefix-matching to find the container. You should only need to specify the first 4-5 characters of the container ID. 
- `-a-`: if this flag is specified, all containers in your local registry will be removed. 

**Note**: Running containers cannot be removed with the rm command. Running containers must be stopped before they can be removed.

#### Debugging

If your container unexpectedly crashes, you'll probably want to find out why. 

The easiest way to do this is with **diagnostic mode** containers. To enable diagnostic mode, run a container with the `--diagnostic` flag enabled. 

	>spoon run --diagnostic <image> 

Diagnostic mode containers will produce a special set of *debugging logs*. To fetch these logs, use the `spoon logs` command. 

The `spoon logs` command also returns logs of all the standard streams (`STDIN`, `STDOUT`, `STDERR`) for the specified container. 

Changes to a container's filesystem and registry can be viewed with the `spoon diff` command. 

**Note**: Enabling diagnostic mode will cause your container to run slower than expected. We recommend only enabling this mode for diagnostic/debugging purposes. 

## Building Images from Containers

If you would like to create a new image from your container, you can commit it using the spoon commit command. The commit command takes 2 parameters: 

1. The ID of the container you want to commit
1. The name of the image you want to build from the container

The `commit` command also takes an optional `--no-base` parameter. By default, the `commit` command will merge the container's sandbox with its base image, and build a new image from these merged layers. When the `--no-base` flag is specified, the sandbox and base image will not be merged and a new image will be built from the sandbox, alone.

After a container has been committed, it is deleted from your system. However, you can now build new containers using your newly created image as a base image!

If you want to share your new image with others, you can `push` it up to a remote registry using the `spoon push` command. 