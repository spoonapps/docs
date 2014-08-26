### rm

The `rm` command removes containers from the local machine. 

To remove a single container, use the command `spoon rm <container ID>`. 

To remove all of the containers in your local registry, specify the `-a` flag in lieu of the `<container ID>`. 

	spoon rm -a

**Note**: Spoon uses prefix-matching when searching for container IDs.  The first 4-6 characters of the ID will usually suffice. 