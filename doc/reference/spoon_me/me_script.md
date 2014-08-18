#.me Scripting

Spoon can act as an automated builder, reading instructions from a `.me` file to create a container and then build a new image from that container.

## What is a .me Script?

A `.me` script is a text file containing a set of **instructions** that the Spoon IDE follows to create a container. At the end of the script, a new image is created from the container and the container is deleted. 

The syntax of a Spoon build script generally follows the pattern: 

	INSTRUCTION <arg 1> <arg 2> ...
	INSTRUCTION <arg 1> <arg 2> ...
	INSTRUCTION <arg 1> <arg 2> ...
	
The script is read top-to-bottom and commands are executed in the order they are read. Therefore, *order matters*!

All scripts have an implicit `commit` at the end of the script. This means that after the Spoon IDE has encountered the last instruction in the script, it executes `spoon commit` on the container it just created. If a name was supplied (via the `-n` or `--name` flag) to the build command, the container is committed to an image with that name. If a name was not provided, the new image will be created with a random hash as a name. 

## Building Images from a Git or VCS Repository



## Syntax

See [Scripting syntax](TODO: add link). 

