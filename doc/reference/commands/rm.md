# rm

The `rm` command is used to remove containers from the local registry. 

It is especially useful for clearing out old, deprecated, and/or unused containers from your system. 

When a container is removed with the `rm` command, all files, registry keys, and metadata associated with the container are permanently deleted from your system. 

## Removing containers

To remove a single container, use the command `spoon rm <container ID>`. 

**Note**: The Spoon IDE uses prefix-matching when searching for container IDs. Thus, you should *not* have to specify the full container ID for the container you want to remove. The first 4-6 characters will usually suffice. 

To remove all of the containers in your local registry, specify the `-a` flag in lieu of the `<container ID>`. 

	spoon rm -a

