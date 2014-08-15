# Creating Containers

Containers are created with the `spoon run` command. 

The `spoon run` command has 2 required parameters: 

1. An `<image>` (or `<**images>`). All containers require a **base image** to run on top of. The image specified here will serve as this base for the newly created container. 
2. The `<command>` to start the container. 

The `<command>` should be of the form: `<executable> <**args>`. The executable may be any executable in the **base image**, `cmd.exe`, or any other valid Windows utility. 

For example, to create a new container using the `spoonbrew/scratch` image and the command `cmd.exe`, execute:
	
	spoon run spoonbrew/scratch cmd.exe

This command will create a new container with a command prompt running *within* that container. Thus, any operations done in the commmand prompt will be applied to the container environment, not the host system. 

The container will continue to run for as long as the command prompt stays open. 

