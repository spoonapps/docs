Images serve as read-only foundations for containers to run "on top of" -- providing a base filesystem and registry that the container can access. They also serve to memorialize the state of an application at a certain point in time. 

Whereas a container is dynamic and can host running processes, an image is static. An image is, essentially, a snapshot of of a container at a specific point in time. 

The local registry is the cache of images on the local machine. When you first download and install the Spoon Plugin, the registry only contains a single image. Images can only be added to the registry through the `pull` or `import` commands. 

To get a list of all the images in the local registry, execute the `spoon images` command. This command generates a table listing all of the images in the user's local registry. 

## Creating Images

There are four ways to create an image:

1. By manually committing a container, with the spoon commit command.
2. Using the `spoon build` command to automatically create images from a build script.
3. Using the `spoon import` command to build images from Spoon XAPPL configuration files. 
4. By using the `spoon import` command to convert other file types to Spoon images.

#### Commit a Container

**Associated Command**: `spoon commit`

If you have an existing container that you would like to create an image from, use the spoon commit command. Before committing a container, make sure that it is not running.

#### Automate Images Builds

**Associated Command**: `spoon build`

Images can be automatically built using Spoon's scripting build language. This language consists of a set of instructions that recreate the steps of configuring a container to build from.

The build command can be broken down into 3 steps:

1. Create an empty container.
2. Follow the instructions in the build script to configure the container.
3. Commit the container.

After the container is committed, it is automatically removed from your machine.

#### Building from a XAPPL File

**Associate Command**: `spoon build` 

XAPPL files are static configuration files that specify all of the files, registry keys/values, and virtual machine settings to use when building a new image. The Spoon IDE can build images based on XAPPL configuration files using `spoon build` command. 

**Note**: This command is equivalent to building as a Component in the Spoon IDE GUI. 

#### Converting From Other File Types

**Associated Command**: `spoon import`

The import command currently supports building from 2 external file types: 

1. Microsoft Software Installer (`MSI`)
2. ThinApp Configuration (`package.ini`)

To import these filetypes, the appropriate flag must be set indicating the type of file to import. 

To import an `MSI`, use the command `spoon import -msi <path to msi>`. 

To import a Thinapp configuration, use the command `spoon import -thinapp <path to msi>`. 


The `pull` command is used to copy an image from a remote registry (the **Spoonium Hub**, for example) the user's local registry. The user must be logged in to a remote registry to use the `pull` command. 

The `pull` command takes a single parameter: the image to pull. When specifying the image to pull, one may optionally specify a repository and tag to pull. If these options are not specified, the following defaults will be applied: 

1. The tag `master` will be applied to the specified image
1. Spoon will look in the logged-in user's account on the remote registry for a matching image
2. If an image is not found, Spoon will look in the `spoonbrew` account for a matching image

If no matching image is found, the `pull` will fail. 


#### Import

If you have an existing image on your local machine (such as from **Spoon IDE** or from a legacy version of **Spoon Studio**), you can `import` it to your local registry. 

The `import` command requires a single parameter: the path to the image to be imported. You can optionally specify a name for the image using the `-n` or `--name` flag. If the image is not named, its ID will be used as a default name. 

Images can be removed from the local registry with the `spoon rmi` command. The `rmi` command can reference the name or the ID of an image. 

If the name of an image is specified, the image will only be truly *deleted* if it is the last remaining image on your machine with that ID. For example, if a local registry contains two identical images with the same ID (hash) but different names, the image binary, itself, will not be deleted until `spoon rmi` has been run against both names. In this case, the first `rmi` command will only remove the specified name-ID association.

#### Naming and Tagging Images

Images can be named using the `spoon fork` command. The `fork` will create a new link to the specified image with a new, given name.    

Images can be tagged with the `spoon tag` command. A tag in Spoon is roughly equivalent to a tag in Git -- that is, a tag refers to a specific point in the revision history of an image. It is most commonly used to denote major points (such as releases) in an image's lifetime. 

Images are tagged by specifying the image to tag, followed by the tag to be applied. For example, to tag the image `my-new-image` with the tag `1.0`, execute the command

	>spoon tag my-new-image 1.0 

#### Pushing Images to a Remote Registry

Images in a local registry can be copied to a remote registry with the `push` command. 

Similar to `pull`, the `push` command takes a single parameter: the image to push. The image parameter may be fully-qualified with a username, name, and tag or partially-qualified -- the only required qualification is the image name. 

The form of a fully-qualified image is `username/name:tag`. 

If the image is not fully-qualified, Spoon will apply the following defaults for the image repository and tag.

1. The tag `head` will be applied to the image. 
2. The image will be pushed to the currently-logged in user's remote registry.

For example, if the user `spoonuser` executes the command `spoon push my-new-image`, the image will be pushed as `spoonuser/my-new-image:head`. 

If a repository `my-new-image` does not exist in the remote registry, a new one will be created. This repository will be **public** by default, unless the user pushing the image has private repositories available. 