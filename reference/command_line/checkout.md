### checkout

The `checkout` command restores any image from the history. 

```
Usage: spoon checkout <options> <id> <image>

<options> available:
      --format=VALUE         Use json format for output
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

# JSON output

When `--format=json` option was passed this command will provide output in JSON format. It will contain either an `image` object with information about checked out image or an `error` object if command failed.