### build

The `build` command is used to automate the creation of images. The `build` command can build images from a SpoonScript or a **.xappl** configuration file. 

```
Usage: spoon build <options> <path>

<options> available:
      --diagnostic           Enable diagnotic logging
  -e, --env=VALUE            Set environment variables inside the container
      --env-file=VALUE       Read in a line delimited file of ENV variables
      --mount=VALUE          Mount a host folder into the container. Format: [other-container:]SourceFolder=TargetFolder
  -n, --name=VALUE           Name of the image
      --no-base              Do not merge the base image into the new image
      --overwrite            Overwrite existing image
      --vm=VALUE             The Spoon VM version to run the container with
  -w, --working-dir=VALUE    Set the initial working directory inside the container
      --wait-after-error     Leave program open after error
      --wait-after-exit      Leave program open after it exits
```

To build an image from an existing container, use the `commit` command.

#### Using SpoonScript

A SpoonScript is a list of instructions that Spoon will follow to create a container. After the last instruction in a script, Spoon will automatically run `spoon commit` on the recently created container, creating a new image. 

When building from a **.me** script, Spoon will take the following steps: 

1. Create an empty container from all of the base images specified in the `from` instruction -- this is equivalent to `spoon run <image>`
2. Perform the remaining instructions in the newly created container 
3. Commit the container to a new image
4. Remove the container from the local machine

If there are any conflicts between a SpoonScript instruction and a command-line flag then the SpoonScript instruction will take precedence. 

#### Using .xappl Files

A **.xappl** file is an XML file that contains all of the filesystem, registry, and configuration information for a given image. A **.xappl** file can be built using Spoon Studio.

#### Environment Variables

Environment variables can be added to the container through the `-e` or `--env-file` flags. These environment variables are initialized at container creation and thus may be overridden by variables created with the `env` instruction in the build script. 

To create multiple environment variables in the container, use multiple `-e` flags. For example, the following command would add two environment variables, VAR1 with value 1 and VAR2 with value 2, to the built image. 

```
> spoon build -e=VAR1=1 -e=VAR2=2 C:\SpoonScript
```

Alternatively, use the `--env-file` flag and specify all of the environment variables you wish to add to the image in a line-delimited text file. For example, the previous command could be replicated using the following command: 

```
> spoon build --env-file=C:\env-vars.txt C:\spoon.me
```

where **env-vars.txt** has the contents: 

```
VAR1=1
VAR2=2
```

**Note**: If the `--env-file` and `-e` flags are used in the same command, the `env-file` flag is always processed before the `-e` flag. In the case of a conflict, the `-e` flag always takes precedence. 

#### Other Command Line Flags

Name images using the `-n` flag and overwrite existing images with the same name using the `--overwrite` flag. 

```
> spoon build -n=my-new-image C:\spoon.me
...
Output Image: my-new-image

# Try to build the same image second time
> spoon build -n=my-new-image C:\spoon.me
Error: The image already exists. You can overwrite with the --overwrite flag

# Try third time, with --overwrite flag
> spoon build -n=my-new-image C:\spoon.me --overwrite
...
Output Image: my-new-image

# Tags can be optionally added to the -n flag
> spoon build -n=my-new-image:1.0 C:\spoon.me
...
Output Image: my-new-image:1.0
```

The build command will create the intermediate container and output image using the latest version of the **Spoon VM**. To use a legacy version, specify the version number you wish to use with the `--vm` flag. 

```
# Build the image using version 11.6.205 of the Spoon VM
> spoon build --vm=11.6.205 C:\spoon.me 
```

The working directory inside the container can be specified with the `-w` flag. This flag may be overridden by a `workdir` instruction in a SpoonScript.

**Note**: This flag sets the woring directory within the intermediate container used to build the output image. It does *not* set the initial working directory of the image. 

The `--diagnostic` flag enables logging within the intermediate container. This flag does not create diagnostic-mode images.

#### Merging Images

The `build` command will include all images, which are referenced with the `from` statement in the script.  For example, when the script uses `from spoonbrew/git, spoonbrew/nuget`, then these two containers will be merged and stored into the newly built container.

The `--no-base` option will not merge in the script. Instead, the images are included at runtime. 