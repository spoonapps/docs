### continue

The `continue` command downloads the last state of a container and then starts it.

```
Usage: spoon continue <options> <container>

<options> available:
  -d, --detach               Run the container in the background
      --diagnostic           Enable diagnostic logging
      --wait-after-error     Leave program open after error
      --wait-after-exit      Leave program open after exit
      --with-root=VALUE      Set the containers root directory
```

If the `continue` command is run against an already-running container then no action will be taken. 

To enable diagnostic logging for the container, specify the `--diagnostic` flag. 

To run the container in the background then specify the `-d` or `--detach` flag. 