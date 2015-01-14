### commit

The `commit` command builds an image from a container. The image is built from the container's most recent state. 

```
Usage: spoon commit <options> <container> <image>

<options> available:
      --no-base              Do not merge the base image(s) into the new image
      --overwrite            Overwrite existing image
      --wait-after-error     Leave program open after error
      --wait-after-exit      Leave program open after exit
```

#### Merging Images

The `commit` command will merge all the base images used in the container. This behavior can be overridden with the `--no-base` flag. 

For example, if a container were created with the command `spoon run "git/git,nuget/nuget"` and later committed with the command `spoon commit <container id> my-new-image`, the new image would contain: 

- Any files and registry keys created or modified in the container
- The files and registry keys from the **git/git** image
- The files and registry keys from the **nuget/nuget** image

However, if the same container were committed with the command `spoon commit --no-base <container id> my-new-image`, `my-new-image` would only contain the files and registry keys created or modified in the container. The `git/git` and `nuget/nuget` images are included as a dependency at runtime.

#### Startup file

If original image had startup file specified then commited image will retain it. If original image had startup file not specified and container was run with `--startup-file` parameter then commited image will have its startup file set to this parameter value.