## Spoon Scripts

Spoon can act as an automated builder, reading instructions from a `.me` file to create a container and then build a new image from that container.

A `.me` script is a text file containing a set of **instructions** that the Spoon IDE follows to create a container. At the end of the script, a new image is created from the container and the container is deleted. 

The syntax of a Spoon build script generally follows the pattern: 

	instruction <arg 1> <arg 2> ...
	instruction <arg 1> <arg 2> ...
	instruction <arg 1> <arg 2> ...
	
The script is read and executed top-to-bottom. 

Spoon Script files are not case-sensitive. However, we recommend making all instructions UPPERCASE and all arguments lowercase, to more easily delineate the two. 

All scripts have an implicit `commit` at the end of the script. After the last instruction in the script, it executes `spoon commit` on the container. If a name was not provided to the `build` command (via the `-n` or `--name` flag), the new image will be created with its ID as its name. 

### Syntax Rules

1. Spoon scripts are line-delimited and must only contain 1 instruction per line. Line continuation is not supported. 
2. All lines must follow the general structure: `instruction <args>`
3. Inline comments are not supported. Comments must be applied at the beginning of a line and are applied to the entire line. 

### Comments

Comments are denoted by the `#` character. 

	#this is a comment

Comments cannot be made inline with a command. Comments must be specified at the beginning of a line. 

```
#this is a valid comment

from spoonbrew/node  #this is not a valid comment
```