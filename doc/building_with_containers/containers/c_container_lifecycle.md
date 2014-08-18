# The Lifecycle of a Container

The lifecycle of a container is controlled by the processes within that container. When the process within a container exits or completes, the container stops running.

Take, for example, this command for starting a new container:

	C:\>spoon run -a cmd.exe /c echo hello world
	hello world
	641bad5a7f904442a399a32f301ba8ed
	C:\>

In this case, we started a new command prompt, executed the command `echo hello world`, and then, because the `/c` flag was specified, the command window closed. Once this process died, the container was automatically stopped and its ID was returned to the native prompt. 

Now, compare this behavior to if the `/k` flag was specified for `cmd.exe`: 

	C:\>spoon run -a cmd.exe /k echo hello world
	hello world
	(641bad5a) C:\>

In this case, we started a new command prompt and again executed echo hello world. This time, however, we specified the `/k` flag to keep the command prompt open after the echo command finished execution. Because the `cmd.exe` process in the container is still running, the container continues running. We can continue to execute commands in the container and it will continue to run until the contained command prompt process exits.

	(641bad5a) C:\>echo hello again
	hello again
	(641bad5a) C:\>exit
	641bad5a7f904442a399a32f301ba8ed
	C:\>

Processes within a container are run as child processes of the **Spoon VM** executable, which manages the container environment. 

## Stopping Containers from the Command Line

A container with running processes can be forcefully stopped with the `spoon stop` command. The `stop` command takes a single parameter -- the ID of the container to stop. This command will stop the **Spoon VM** process that manages the container along with any of its child processes -- thus shutting down the container. 

## Starting Containers from the Command Line

Alternatively, stopped containers can also be restarted with the `spoon start` command. Like the `stop` command, the `start` command accepts a single parameter -- a container ID. When a container is restarted with `start`, it uses the same startup command as specified when the container was originally created with `spoon run`. 

Take, for example, a container with ID `55djk3x1` created with the command: `spoon run spoonbrew/scratch cmd.exe /c echo hello world`. This container will start, execute `echo hello world` in a new command prompt, and then shut down. 

If this container were to then be restarted with the command: `spoon start 55djk3x1`, a new command prompt would be spawned, the command `echo hello world` would execute, and the container would shut down. 