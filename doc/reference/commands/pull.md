## pull

The `pull` command copies an image from a remote registry to your local registry. 

This command requires a single parameter: the image to pull. 

The image to pull can be specified with up to 3 identifiers, only 1 of which (the name) is mandatory: 

- Namespace
- Name
- Tag

If a namespace is not specified, it will default to that of the logged-in user. 

If a tag is not specified, the default tag of `head` is applied. 