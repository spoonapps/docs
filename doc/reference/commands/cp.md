### cp

The `cp` command copies a files from one container to another between a container and the native filesystem. 

```
Usage: spoon cp <options> [<source-container>:]<path-from> [<target-container>:]<path-to>

<options> available:
      --wait-after-error     Leave program open after error
```

```
# Copy a file from a container to the native system
> spoon cp 2de7:C:\project\file.txt C:\Users\Spoonuser

# Copy a file from a container to another container
> spoon cp 2de7:C:\project\file.txt 3vj3:C:\other-project

# Container paths must be absolute
> spoon cp 2de7:file.txt C:\Users\Spoonuser

ERROR

# Native paths are relative to the current prompt
C:\Users> spoon cp 2de7:C:\project\file.txt \Spoonuser
```