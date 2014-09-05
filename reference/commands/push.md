### push

The `push` command syncs an image from your local registry to the remote registry. 

```
Usage: spoon push <options> [<namespace>/]<image>[:<tag>]

<options> available:
      --wait-after-error     Leave program open after error
```

If the namespace is not specified then Spoon will look for a repository belonging to the current user that corresponds to the image name. If this does not exist, a new, public repository will be created and the image will be pushed there.