# Pushing Images to a Remote Registry

Images in a local registry can be copied to a remote registry with the `push` command. 

Similar to `pull`, the `push` command takes a single parameter: the image to push. The image parameter may be fully-qualified with a username, name, and tag or partially-qualified -- the only required qualification is the image name. 

The form of a fully-qualified image is `username/name:tag`. 

If the image is not fully-qualified, Spoon will apply the following defaults for the image repository and tag.

1. The tag `head` will be applied to the image. 
2. The image will be pushed to the currently-logged in user's remote registry.

For example, if the user `spoonuser` executes the command `spoon push my-new-image`, the image will be pushed as `spoonuser/my-new-image:head`. 

If a repository `my-new-image` does not exist in the remote registry, a new one will be created. This repository will be **public** by default, unless the user pushing the image has private repositories available. 