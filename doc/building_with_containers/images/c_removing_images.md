# Removing Images 

Images can be removed from the local registry with the `spoon rmi` command. The `rmi` command can reference the name or the ID of an image. 

If the name of an image is specified, the image will only be truly *deleted* if it is the last remaining image on your machine with that ID. For example, if a local registry contains two identical images with the same ID (hash) but different names, the image binary, itself, will not be deleted until `spoon rmi` has been run against both names. In this case, the first `rmi` command will only remove the specified name-ID association. 