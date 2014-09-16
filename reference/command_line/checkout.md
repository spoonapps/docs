### checkout

The `checkout` command restores any image from the history. 

```
Usage: spoon checkout <options> <id> <image>

<options> available:
      --overwrite            Overwrite existing image
      --wait-after-error     Leave program open after error
```
    
The new name has to be unique on your local machine. The `--overwrite` flags allows to overwrite an existing image name.

```
# Checkout a old image by its id
> spoon checkout 73dfe6973074 restored-image

Restored the restored-image:head image
```