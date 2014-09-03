### export

The `export` command copies an image from the local registry to a specified path on your local machine or network. 

```
export - Export an image from the local registry to the specified path

Usage: spoon export <options> <image> <path>

<options> available:
      --wait-after-error     Leave program open after error
```

```
# Copy an image to the local machine
> spoon export my-new-image C:\

# Copy an image to a network share
> spoon export my-new-image \\server\folder
```