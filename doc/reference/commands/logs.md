### logs

The `logs` command fetches the logs for a container, if they exist. This is especially useful for debugging or inspecting containers. 

By default, only the standard streams for a container are recorded and logged. To enable more comprehensive logging, use the `--diagnostic` flag of the `run` command when the container is initially created or started by `start`. 

Logs are kept till the next start of given container instance. They can be previewed at any moment and `--list` shows available logs. When container is started, currently available logs of the proccesses in run instance are displayed. When container is stopped, logs from recently run instance are presented.

	# Can only show stdout or stderr logs
	> spoon logs --stdout 2de7fda8

	> spoon logs --stderr 2de7fda8

	# Show timestamps for log entries
	> spoon logs -t 2de7fda8

	# Show stream prefixes of log entries
	> spoon logs -s 2de7fda8

	# Follow log output in real-time
	> spoon logs -f 2de7fda8

	# Similar to Unix 'tail', only show last 5 lines
	> spoon logs --tail=5 2de7fda8

	# Show diagnostic logs instead of stdandards streams
	> spoon logs --diagnostic 2de7fda8

	# Show logs for specified process
	> spoon logs --pid=666 2de7fda8

	# List available logs
	> spoon logs --list 2de7fda8

Stream prefix for **stdout** is `out` and `err` for **stderr**.

Timestamp is Windows timestamp format, a 64-bit value representing the number of 100-nanosecond intervals since January 1, 1601 (UTC).
