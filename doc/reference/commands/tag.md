# tag

The `tag` command copies an image and renames the copy with the namespace/name/tag specified in the command. 

The `tag` command requires 2 arguments: 

1. The image to be renamed. This argument may include the image's namespace and/or tag. 
2. The name to assign to the copy. 

## Adding an Image to a Namespace

Before an image is pushed, it must reside under a `namespace` in the local registry. An image under a namespace will have the form `<namespace>/<image name>`, as opposed to just `<image name>`. 

To assign an image to a namespace, use the `tag` command. Specify the image you want to assign, followed by the `namespace/<image name>`. 

For example, to assign the image `my-new-image:master` to the namespace `spoonuser`, the command would be: 

	spoon tag my-new-image:master spoonuser/my-new-image:master

 