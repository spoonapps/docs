### diff

The `diff` command shows changes made in a container's filesystem. 

Changes are shown relative to the base image that the container was created from. 

The `--path` flag can be added to make the `diff` command only show changes to the container's filesystem in subdirectories of the specified path. For example, if the `--path=C:\Users` were specified, only changes in subdirectories of the **C:\Users** folder would be shown. 