### cp

The `cp` command copies a file or directory from one container to another. It can also copy a file or directory from a container to the native filesystem. 

The path of the file or directory to copy must be *absolute*, or the `cp` command will fail. 

The path of the local destination (if copying to the native filesystem) for the copied file/directory may be a relative path. Paths are relative to the current directory in the local command prompt. 