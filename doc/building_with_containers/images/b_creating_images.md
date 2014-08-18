#Creating Images

There are four ways to create an image:

1. By manually committing a container, with the spoon commit command.
2. Using the `spoon build` command to automatically create images from a build script.
3. Using the `spoon import` command to build images from Spoon XAPPL configuration files. 
4. By using the `spoon import` command to convert other file types to Spoon images.

## Commit a Container

**Associated Command**: `spoon commit`

If you have an existing container that you would like to create an image from, use the spoon commit command. Before committing a container, make sure that it is not running.

## Automate Images Builds

**Associated Command**: `spoon build`

Images can be automatically built using Spoon's scripting build language. This language consists of a set of instructions that recreate the steps of configuring a container to build from.

The build command can be broken down into 3 steps:

1. Create an empty container.
2. Follow the instructions in the build script to configure the container.
3. Commit the container.

After the container is committed, it is automatically removed from your machine.

## Building from a XAPPL File

**Associate Command**: `spoon build` 

XAPPL files are static configuration files that specify all of the files, registry keys/values, and virtual machine settings to use when building a new image. The Spoon IDE can build images based on XAPPL configuration files using `spoon build` command. 

**Note**: This command is equivalent to building as a Component in the Spoon IDE GUI. 

## Converting From Other File Types

**Associated Command**: `spoon import`

The import command currently supports building from 2 external file types: 

1. Microsoft Software Installer (`MSI`)
2. ThinApp Configuration (`package.ini`)

To import these filetypes, the appropriate flag must be set indicating the type of file to import. 

To import an `MSI`, use the command `spoon import -msi <path to msi>`. 

To import a Thinapp configuration, use the command `spoon import -thinapp <path to msi>`. 

# Adding Existing Images

There are two commands that can be used to add an existing Spoon image to the local registry. 

1. Pull
2. Import

## Pull

The `pull` command is used to copy an image from a remote registry (the **Spoonium Hub**, for example) the user's local registry. The user must be logged in to a remote registry to use the `pull` command. 

The `pull` command takes a single parameter: the image to pull. When specifying the image to pull, one may optionally specify a repository and tag to pull. If these options are not specified, the following defaults will be applied: 

1. The tag `master` will be applied to the specified image
1. Spoon will look in the logged-in user's account on the remote registry for a matching image
2. If an image is not found, Spoon will look in the `spoonbrew` account for a matching image

If no matching image is found, the `pull` will fail. 

## Import

If you have an existing image on your local machine (such as from **Spoon IDE** or from a legacy version of **Spoon Studio**), you can `import` it to your local registry. 

The `import` command requires a single parameter: the path to the image to be imported. You can optionally specify a name for the image using the `-n` or `--name` flag. If the image is not named, its ID will be used as a default name. 

