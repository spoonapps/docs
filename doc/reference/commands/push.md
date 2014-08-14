# push

The `push` command copies an image from your local registry to the remote registry that you are logged into. 

**Note**: You must be logged in to a remote hub to use the `push` command. 

The `push` command accepts 2 parameters: 

1. (Optional) The repository to copy the image to
2. The image (and tag) to push

If a repository is not specified, `push` will look for a repository belonging to the current user that corresponds to the image name. If this does not exist, a new (public) repository will be created and the image will be pushed to this new repository. 

If a tag is not explicitly specified in the `push` command (i.e. `spoon push my-image`), the default tag of `master` will be applied before the push is attempted. 

For example, the command `spoon push my-image` is equivalent to `spoon push my-image:master`.  

## Pushing to Remote Repositories

Before copying the image to the remote registry, the `push` command will first look for an existing repository under the current user's namespace. If such a repository exists, the image will be pushed to that repository. If it does not, a new one will be created and the image will be added to it. 

## Public/Private Visibility of Pushed Images

The access rights of a pushed image are inherited from the repository the image is pushed to. That is, if an image is pushed to a private repository, it too will be private. If an image is pushed to a public repository, it will be publicly visible. 

If an image is pushed to the remote registry and a corresponding repository does not already exist, a public repository will be created and the image will be added to this repository. 

## Pushing a Tagged Image to :master

If you have previously tagged an image and would now like to push it to the `master` tag of the remote repository, the image must be re-tagged before it is pushed. 

To do this, use the `spoon tag` command to re-tag the image with the new `master` tag. Then, push the newly-tagged image to the remote repository. 

