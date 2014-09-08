### stop

The `stop` command stops containers which are currently running. 

```
Usage: spoon stop <options> <container>...

<options> available:
  -a, --all                  Stop all running containers
      --wait-after-error     Leave program open after error

```

`start` command accepts either list of containers to close or `-a` parameter to close all running containers.

If the `stop` command is run against a non-running container then no action will be taken. 

To enable diagnostic logging for the container, specify the `--diagnostic` flag. 
