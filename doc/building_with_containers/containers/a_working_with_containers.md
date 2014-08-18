# Working with Containers

Containers form the backbone of the Spoonium ecosystem. In this section, we'll walk you through the many ways to work with and manage containers once they've been created with the `spoon run` command. 

## Working Inside Containers

The easiest way to tell if you are inside a container is to check your prompt. When a command prompt exists within a container, the prompt is prepended by the first 8 characters of the container's ID.


	>spoon start 8dpp9e
	
	(8dpp9eb5) >

Once inside a container, you can edit and modify the container's virtual filesystem and registry using the same command-line interfaces as are available in the Windows Command Prompt.

To "break out" of a container, kill any running processes inside that container. For example, if running a command prompt inside a container, to stop the container type `exit` or press Ctrl-C.
