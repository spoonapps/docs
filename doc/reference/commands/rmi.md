## rmi

The `rmi` command removes an image, or images, from the local registry. 

If you want to save an image but don't want to have it in your local registry, use the `spoon export` command to export the `.svm` file to your local file system. 

To remove a single image from the local registry, specify the image name or ID as an argument to the `spoon rmi` command. 

	spoon rmi <image>

The `rmi` command will only truly *delete* an image if the image specified in the command is the last image in the local registry with that ID. Otherwise, the reference with the specified name is removed. For example, if and image with ID `fd4safew4r56` is named `spoonuser/my-image:head` and `my-image:head` and the command `spoon rmi my-image:head` is executed, the reference `my-image:head` will no longer refer to image `fd4safew4r56`, but the image itself is *not deleted*. 

If an image `rmi` command is passed an image ID, the image is deleted and all references (names, tags, etc.) are removed from the local registry. 

To remove all the images in your registry, specify the `-a` flag as the argument to the `spoon rmi` command. 

	spoon rmi -a