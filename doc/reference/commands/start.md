### start

The start command restarts a stopped container. 

If the start command is run against an already-running container, no action is taken. 

To enable diagnostic logging for the container, specify the `--diagnostic` flag. 

To suppress the container's standard streams, effectively running the container in the background, specify the `-d` or `--detach` flag after `spoon start`. 