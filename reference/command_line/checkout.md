### checkout

The `checkout` command restores any image from the history. 

```
Usage: spoon checkout <options> <id> <image>

<options> available:
      --overwrite            Overwrite existing image
      --wait-after-error     Leave program open after error
      --wait-after-exit      Leave program open after exit
```
    
The new image name has to be unique on the local machine or use the `--overwrite` flags to overwrite an existing image.

```
# Checkout a old image by its id
> spoon checkout 73dfe6973074 restored-image

Restored the restored-image image
```