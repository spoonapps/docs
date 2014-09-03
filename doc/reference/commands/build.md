### build

The `build` command is used to automate the creation of images. The `build` command can build images from a SpoonScript or a **.xappl** configuration file. 

To build from an existing container, use the `commit` command.

#### Using SpoonScript

A SpoonScript is a list of instructions that Spoon will follow to create a container. After the last instruction in a script, Spoon will automatically run `spoon commit` on the recently created container, creating a new image. 

When building from a **.me** script, the Spoon IDE will take the following steps: 

1. Create an empty container from all of the base images specified in the `from` instruction -- this is equivalent to `spoon run <image>`
2. Perform any subsequent instructions in the newly created container 
3. After the last instruction, stop the container
4. Commit the stopped container
5. Remove the container from the local machine

Any command line flags that correspond to a SpoonScript instruction will be overriden by their corresponding instruction, if they conflict. 

#### Using .xappl Files

A **.xappl** file is an XML file that contains all of the filesystem and registry information for a given container. It also contains all of the Spoon VM settings to apply to the container. 

#### Environment Variables

Environment variables can be added to the container through the `-e` or `--env-file` flags. These environment variables are initialized at container creation, and thus may be overridden by variables created with the `env` instruction in the build script. 

To create multiple environment variables in the container, use multiple `-e` flags. For example, the following command would add 2 environment variables, VAR1 with value 1 and VAR2 with value 2, to the built image. 

	> spoon build -e=VAR1=1 -eVAR2=2 C:\SpoonScript

Alternatively, use the `--env-file` flag and specify all of the environment variables you wish to add to the image in a line-delimited text file. For example, the previous command could be replicated using the following command: 

	> spoon build --env-file=C:\env-vars.txt C:\spoon.me

where **env-vars.txt** has the contents: 

	VAR1=1
	VAR2=2

**Note**: If the `--env-file` and `-e` flags are used in the same command, the `env-file` flag is always processed before the `-e` flag. In the case of a conflict, the `-e` flag always takes precedence. 

#### Other Command Line Flags

Builds can be given names with the `-n` flag. 

	> spoon build -n=my-new-image C:\spoon.me

	...
	...
	Output Image: my-new-image

	# Tags can be optionally added to the -n flag
	> spoon build -n=my-new-image:1.0 C:\spoon.me
	
	...
	...
	Output Image: my-new-image:1.0


By default, the build command will create the intermediate container and output image using the latest version of the **Spoon VM**. To use a legacy version, specify the version number you wish to use with the `--xvm` flag. 

	# Build the image using version 11.6.205 of the Spoon VM
	> spoon build --xvm=11.6.205 C:\spoon.me 

The working directory inside the container can be specified with the `-w` flag. This flag may be overridden by a `workdir`  instructions in a SpoonScript.

Note that this flag sets the woring directory within the intermediate container used to build the output image. It does *not* set the initial working directory of the image. 

The `--diagnostic` flag enables logging within the intermediate container. This flag does not create diagnostic-mode images.