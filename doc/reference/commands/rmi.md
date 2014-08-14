# rmi

The `rmi` command removes an image, or images, from the local registry. The image removal process *will* delete the image from your machine -- so make sure you have a copy of any images you delete before they are removed. 

If you want to save an image but don't want to have it in your local registry, consider using the `spoon export` command to export the `.svm` file to your local file system. 

## Removing Images

To remove a single image from the local registry, specify the image name or ID as an argument to the `spoon rmi` command. 

	spoon rmi <image>

To remove all the images in your registry, specify the `-a` flag as the argument to the `spoon rmi` command. 

	spoon rmi -a