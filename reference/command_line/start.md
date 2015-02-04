### start

The `start` command restarts a container which is not currently running. 

```
Usage: spoon start <options> <container>

<options> available:
  -d, --detach               Run the container in the background
      --diagnostic           Enable diagnotic logging
      --disable-sync         Automatic container pushes are disabled
      --private              Synchronize this container privately, visible only to me
      --public               Synchronize this container publicly, visible to everyone
      --startup-file=VALUE   Override the default startup file
      --wait-after-error     Leave program open after error
      --wait-after-exit      Leave program open after it exits
      --with-root=VALUE      Set the containers root directory
```

If the `start` command is run against an already-running container then no action will be taken. 

To enable diagnostic logging for the container, specify the `--diagnostic` flag. 

To run the container in the background then specify the `-d` or `--detach` flag.

To temporarily alter the startup file, specify it with `--startup-file` parameter. The change overrides the original startup files and does not apply to a subsequent container starts or commits.

When the container stops, the exit code of startup file is displayed in decimal form.
