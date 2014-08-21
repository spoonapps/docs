## build

The `build` command is used to automate the creation of images. The build command can build images from a **.me** build script or a **.xappl** configuration file. 

If you wish to build from an existing container, use the `commit` command.

For more information on **.me** files, see [Build scripts](TODO: add link).

For more information on **.xappl** files, see [XAPPL file format](TODO: add link).  

#### Using .me Scripts

A **.me** script is simply a list of instructions that the Spoon IDE will follow to create a container. After the last instruction in a script, the Spoon IDE will automatically run `spoon commit` on the recently created container, creating a new image. 

When building from a **.me** script, the Spoon IDE will take the following steps: 

1. Create an empty container from all of the base images specified in the `FROM` instruction -- this is equivalent to `spoon run <image>`
2. Perform any subsequent instructions in the newly created container 
3. After the last instruction, stop the container
4. Commit the stopped container
5. Remove the container from the local machine

#### Using .xappl Files

A **.xappl** file is an XML file that contains all of the filesystem and registry information for a given container. It also contains all of the Spoon VM settings to apply to the container. 

#### Command Line Flags

The `build` command accepts a number of flags that will modify its behavior at runtime. 

Any command line flags that correspond to a **.me** instruction (such as the `-e` flag and the `ENV` instruction), will be overriden by their corresponding instruction, if they conflict. 

##### Environment Variables

Environment variables can be added to the container through the `-e`, `--env`, or `--env-file` flags. These environment variables are initialized at container creation, and thus may be overridden by variables created with the `ENV` instruction in the build script. 

For example, if the build script 
	
	FROM spoonbrew/scratch
	ENV VAR=2

is used with the command line

	C:\>spoon build -e=VAR=1 C:\spoon.me

the resulting image will contain an environment variable, `VAR` with value **2** (*not* 1). 

To create multiple environment variables in the container, use multiple `-e` or `--env` flags. For example, the following command would add 2 environment variables, VAR1 with value 1 and VAR2 with value 2, to the built image. 

	C:\>spoon build -e=VAR1=1 -eVAR2=2 C:\spoon.me

Alternatively, use the `--env-file` flag and specify all of the environment variables you wish to add to the image in a line-delimited text file. For example, the previous command could be replicated using the following command: 

	C:\>spoon build --env-file=C:\env-vars.txt C:\spoon.me

where **env-vars.txt** has the contents: 

	VAR1=1
	VAR2=2

**Note**: If the `--env-file` and the `-e` or `--env` flags are specified in the same command, the flags will always be processed in the order: 

1. Variables specified in the `env-file` are added
2. Variables specified by the `-e` or `--env` flags are added in the order they are specified in the command. 

If these flags conflict with one another, the "last one" wins. That is, whichever flag was processed last by the Spoon IDE will override any previously set values for that variable. 

##### Naming and Tagging Builds

Builds can be named with the `-n` or `--name` flag. A tag can be optionally included in the value for this flag. If a tag is not provided, the default tag of `master` will be applied. 

**Example usage**

	spoon build -n=my-new-image C:\spoon.me

Creates an image with name and tag `my-new-image:master`. 

	spoon build -n=my-new-image:1.0 C:\spoon.me

Creates an image with name and tag 'my-new-image:`1.0`.

##### Using a Legacy Spoon VM

By default, the `build` command will create the intermediate container and output image using the latest version of the **Spoon VM**. To use a legacy version, specify the version number you wish to use with the `--xvm` flag. 

For example, the following command builds an image using version 11.6.205 of the Spoon VM. 

	spoon build --xvm=11.6.205 C:\spoon.me 

##### Working Directory

The working directory inside the container can be specified with the `-w` or `--working-dir` flags. This flag may be overridden by any `WORKDIR` instructions in the container. 

Note that this flag sets the woring directory within the intermediate container used to build the output image. It does *not* set the initial working directory of the image. 