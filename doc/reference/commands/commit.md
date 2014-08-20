## commit

The `commit` command builds an image from a container. The container is built from its most recent state. 

A container must be stopped before it can be committed to an image. 

Whereas containers are modifiable, **images are read-only**. This means that once you commit a container, its contents can no longer be modified -- effectively creating a snapshot of the container at a given point in time.

This idea roughly parallels the idea of *snapshotting* that is available in many traditional OS virtualization software packages (such as Virtualbox). 

You should `commit` a container when you want to memorialize its state at that point in time. 

You can then continue your work on top of the newly-committed image. 

#### Merging Images

By default, the `commit` command will merge any base images the container runs on top of into the newly-created image. 

For example, if a container were created with the command `spoon run spoonbrew/git;spoonbrew/nuget cmd` and later committed with the command `spoon commit <container id> my-new-image`, the image `my-new-image` would contain: 

- Any files and registry keys created or modified in the container
- The files and registry keys from the `spoonbrew/git` image
- The files and registry keys from the `spoonbrew/nuget` image

However, if the same container were committed with the command `spoon commit --no-base <container id> my-new-image`, `my-new-image` would only contain the files and registry keys created or modified in the container. 