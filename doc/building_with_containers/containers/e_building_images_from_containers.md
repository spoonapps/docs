# Building Images from Containers

If you would like to create a new image from your container, you can commit it using the spoon commit command. The commit command takes 2 parameters: 

1. The ID of the container you want to commit
1. The name of the image you want to build from the container

The `commit` command also takes an optional `--no-base` parameter. By default, the `commit` command will merge the container's sandbox with its base image, and build a new image from these merged layers. When the `--no-base` flag is specified, the sandbox and base image will not be merged and a new image will be built from the sandbox, alone.

After a container has been committed, it is deleted from your system. However, you can now build new containers using your newly created image as a base image!

If you want to share your new image with others, you can `push` it up to a remote registry using the `spoon push` command. 