# diff

The `diff` command will show any changes to the container's filesystem from the base image that was `run`. 

## Command Line Flags

The `--path` flag can be added to make the `diff` command only show changes to the container's filesystem in subdirectories of the specified path. For example, if the `--path=C:\Users` were specified, only changes in subdirectories of the **C:\Users** folder would be shown. 