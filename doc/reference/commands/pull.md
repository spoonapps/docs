### pull

The `pull` command syncs an image from a remote registry to your local registry. 

```
Usage: spoon pull <options> [<namespace>/]<image>[:<tag>]

<options> available:
      --wait-after-error     Leave program open after error
```

The image to pull can be specified with up to 3 identifiers, only 1 of which (the name) is mandatory: 

- Namespace (user or org on the remote hub)
- Name of the remote repository
- Tag

If a namespace is not specified then it will default to that of the current user. 

If a tag is not specified then the **head** tag is applied. 