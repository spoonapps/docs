### rm

The `rm` command removes containers from the local machine. 

```
Usage: spoon rm <options> <container>

<options> available:
  -a, --all                  Remove all containers on the local machine
```

Use the `-a` flag to remove all containers at one time. Note that this operation cannot be undone.

```
# Remove a single container by specifying the ID
> spoon rm f1ea9fe

Container f1ea9fefjdkaslfh324fdadfshjkl3cndkj3 has been removed

# Remove all containers on the local machine with the -a flag
> spoon rm -a

All containers have been removed
```