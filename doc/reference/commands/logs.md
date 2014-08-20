## logs

The `logs` command is most useful for **debugging**. If something goes (unexpectedly) wrong inside a running container, you can inspect any logs that Spoon recorded for that container with the `logs` command. 

By default, only the standard streams for a container are recorded and logged. To enable more comprehensive logging, specify the `--diagnostic` flag for the `run` command. 

To show the timestamps for any recorded logs, specify the `-t` flag. 

To show only the logs of `stdout` or `stderr`, specify the `--stdout` or `--stderr` flags, respectively. 

The `log` command also has a `--tail=VALUE` flag. Similar to the `tail` on *nix machines, the `--tail=VALUE` flag will only show the last `VALUE` lines of the logs. 