In this section, you'll learn to work with and manage containers.

## Creating Containers

The `spoon run` command creates new containers. It has 2 required parameters:

1. A base `<image>` to provide the virtual filesystem and registry for the container. If no files or registry keys are necessary, use this [empty image](http://spoonium.net/hub/spoonbrew/scratch).

2. A `<command>`, which is an executable to launch inside the container. This can be any executable in the **base image**, the command window `cmd.exe`, or any other valid Windows utility.
    
    # Launch a command window in a new container with scratch as the base image
	> spoon run spoonbrew/scratch cmd.exe

Operations executed in the new command window are applied to the container, not the host system.

To avoid confusion, the prompt is prepended by the first 8 characters of the container ID when a command window is running in a container.

    # Host command window
	> spoon run spoonbrew/scratch cmd.exe
	
    # Container command window
	(8dpp9eb5) C:\>

Edit and modify the container's virtual filesystem and registry using the same command-line interfaces available in Windows Command Prompt.

## Processes and Stopping Containers

The life cycle of a container is controlled by the processes within that container. When a process within a container exits or completes, the container exits as well.

Processes in a container spawn as child processes of the **Spoon VM** executable, which manages the container environment. 

To forcefully exit a container, use the `spoon stop` command from a native command window. The `stop` command requires the ID of the container as a parameter. This command will kill the **Spoon VM** process that manages the container along with any child processes. 

You can also explicitly shut down a container from a command window running in the container by typing `exit` or entering Ctrl+C.

Restart a closed container with the `spoon start` command and specify the container ID.

    > spoon start 8dpp9eb5

The container is restarted and launches the same startup command specified in the original `spoon run` command.

## Managing Containers

Containers can be tracked and managed through the `spoon containers` command.

	> spoon containers

	ID           IMAGES              COMMAND       CREATED          STATUS
	03bddd8bef   spoonbrew/scratch   cmd           8/14/2014 1:03   Running
	52hd888xa3   local/server-app    startup.bat   8/14/2014 1:00   Stopped

This produces a tabular output listing the container IDs, creation dates, base images, and commands.

<!-- If your container has multiple processes with transient lifetimes, it may be useful to view which processes are, at a given point in time, running within a container. 

The `top` command will list and detail all of the running processes in a container.

To view the running processes in a given container, execute `spoon top <id of the container to view>`. -->

Remove a container with the `spoon rm` command:

    # Specify a container ID
    > spoon rm 03bddd8bef

Since CLI uses prefix-matching to find the container, you only need to specify the first 4-5 characters of the container ID.

Specifying the `-a` flag removes all containers from the local registry with the exception of running containers. Running containers must be stopped before being removed.

#### Debugging

If your container unexpectedly crashes, specify the `--diagnostic` flag to enable **diagnostic mode** for a container.

	> spoon run --diagnostic <image> <command>

Diagnostic mode containers will produce *debugging logs*.

    # Fetch the logs
    > spoon logs

This command also returns logs of all the standard streams (`STDIN`, `STDOUT`, `STDERR`) for the specified container.

**Note**: Enabling diagnostic mode will cause your container to run slower than expected. We recommend only enabling this mode for diagnostic/debugging purposes. 

Changes to a container's filesystem and registry can be viewed with the `spoon diff` command. 

## Building Images from Containers

To create a new image from a container, save it using `spoon commit`.

    # Specify the container ID and a name for the new image
    > spoon commit 52hd888xa3 test

By default, the `commit` command merges sandbox changes with the base images and builds a new image from these merged layers. Specifying the "--no-base" option builds a new image of the sandbox changes without merging the base images.

After a container has been committed, it is deleted from your system.