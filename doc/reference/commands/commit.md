### commit

The commit command builds an image from a container. The container is built from its most recent state. 

A container must be stopped before it can be committed to an image. 

#### Merging Images

By default, the commit command will merge all base images the container runs on top of

For example, if a container were created with the command `spoon run spoonbrew/git;spoonbrew/nuget` and later committed with the command `spoon commit <container id> my-new-image`, the new image would contain: 

- Any files and registry keys created or modified in the container
- The files and registry keys from the **spoonbrew/git** image
- The files and registry keys from the **spoonbrew/nuget** image

However, if the same container were committed with the command `spoon commit --no-base <container id> my-new-image`, `my-new-image` would only contain the files and registry keys created or modified in the container. 