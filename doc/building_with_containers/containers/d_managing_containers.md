# Managing Containers

#### Tracking Containers

Containers can be tracked and managed through the spoon ps command. This command will list all of the currently-running containers on the local machine. The spoon ps command produces a tabular output listing the container's ID, date/time of creation, the base image, and the command the container was started with.

	>spoon containers

	ID           IMAGES              COMMAND       CREATED          STATUS
	03bddd8bef   spoonbrew/scratch   cmd           8/14/2014 1:03   Running
	52hd888xa3   local/server-app    startup.bat   8/14/2014 1:00   Running

To view all of the containers, both running and stopped, use the `-a` flag. 

	>spoon containers -a

## Viewing Processes in a Container

If your container has multiple processes with transient lifetimes, it may be useful to view which processes are, at a given point in time, running within a container. 

The Spoon IDE exposes this ability through the `top` command. The `top` command will list and detail all of the running processes in a container.

To view the running processes in a given container, execute `spoon top <id of the container to view>`. 

## Inspecting Changes in a Container

Changes to a container's filesystem and registry can be viewed with the `spoon diff` command. 

## Removing Containers

Containers can be removed, or deleted, from your local registry using the spoon rm command. The spoon rm takes one of two possible parameters:

- The **ID** of the container to remove. The Spoon IDE uses prefix-matching to find the container. You should only need to specify the first 4-5 characters of the container ID. 
- `-a-`: if this flag is specified, all containers in your local registry will be removed. 

**Note**: Running containers cannot be removed with the rm command. Running containers must be stopped before they can be removed.

## Debugging Containers

If your container unexpectedly crashes, you'll probably want to find out why. 

The easiest way to do this is with **diagnostic mode** containers. To enable diagnostic mode, run a container with the `--diagnostic` flag enabled. 

	>spoon run --diagnostic <image> 

Diagnostic mode containers will produce a special set of *debugging logs*. To fetch these logs, use the `spoon logs` command. 

The `spoon logs` command also returns logs of all the standard streams (`STDIN`, `STDOUT`, `STDERR`) for the specified container. 

**Note**: Enabling diagnostic mode will cause your container to run slower than expected. We recommend only enabling this mode for diagnostic/debugging purposes. 