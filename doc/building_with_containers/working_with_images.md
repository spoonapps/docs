# Working with Images

Images are the foundation of all of the work you'll do in the Spoon IDE. They serve as read-only foundations for containers to run "on top of" -- providing a base filesystem and registry that the container can access. 

## The Local Registry

The local registry is the cache of images on the local machine. By default, the registry is empty. Images can only be added to the registry through the `pull` or `import` commands. 

#### Adding Images

There are three commands that can be used to add images to the local registry. 

1. Pull
2. Import
3. Build

###### Pull

The `pull` command is used to copy an image from a remote registry (the **Spoonium Hub**, for example) the user's local registry. The user must be logged in to a remote registry to use the `pull` command. 

The `pull` command takes a single parameter: the image to pull. When specifying the image to pull, one may optionally specify a repository and tag to pull. If these options are not specified, the following defaults will be applied: 

1. The tag `master` will be applied to the specified image
1. Spoon will look in the logged-in user's account on the remote registry for a matching image
2. If an image is not found, Spoon will look in the `spoonbrew` account for a matching image

If no matching image is found, the `pull` will fail. 

###### Import

Images can also be added to the local registry through the `import` command. The `import` command will accept an `MSI`, ThinApp `package.ini`, or Spoon `SVM`, convert it into an image, and add the newly-created image into the local registry. 

The `import` command takes an optional `-n` or `--name` parameter, which can be used to name the imported image. If a name is not specified, the image will be named using the image's 32-character ID. 

###### Build

Images can be built from a `.xappl` configuration file or from a `.me` build script. The newly-built image is then automatically added to the user's local registry. 

The `build` command has an optional `-n` or `--name` parameter that can be used to name the newly built image. If a name is not specified, the image will be named using the image's 32-character ID. 

#### Removing Images

Images can be removed from the local registry with the `spoon rmi` command. The `rmi` command can reference the name or the ID of an image. 

#### Viewing Images in the Registry

To get a list of all the images in the local registry, execute the `spoon images` command. This command generates a table listing all of the images in the user's local registry. 

## Pushing Images to a Remote Registry

Images in a local registry can be copied to a remote registry with the `push` command. 

Similar to `pull`, the `push` command takes a single parameter: the image to push. The image parameter may be fully-qualified with a username, name, and tag or partially-qualified -- the only required qualification is the image name. 

The form of a fully-qualified image is `username/name:tag`. 

If the image is not fully-qualified, Spoon will apply the following defaults for the image repository and tag.

1. The tag `head` will be applied to the image. 
2. The image will be pushed to the currently-logged in user's remote registry.

For example, if the user `spoonuser` executes the command `spoon push my-new-image`, the image will be pushed as `spoonuser/my-new-image:head`. 

If a repository `my-new-image` does not exist in the remote registry, a new one will be created. This repository will be **public** by default, unless the user pushing the image has private repositories available. 

## Naming and Tagging Images

#### Renaming

TODO: wait for this command to stabilize

#### Tagging

Images can be tagged with the `spoon tag` command. A tag in Spoon is roughly equivalent to a tag in Git -- that is, a tag refers to a specific point in the revision history of an image. It is most commonly used to denote major points (such as releases) in an image's lifetime. 

Images are tagged by specifying the image to tag, followed by the tag to be applied. For example, to tag the image `my-new-image` with the tag `1.0`, execute the command

	spoon tag my-new-image 1.0

