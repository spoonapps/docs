### logs

The logs command fetches the logs for a container, if they exist. This is especially useful for debugging or inspecting containers. 

By default, only the standard streams for a container are recorded and logged. To enable more comprehensive logging, use the **--diagnostic** flag of the **run** command when the container is initially created. 

	# Can only show stdout or stderr logs
	> spoon logs --stdout 2de7fda8

	> spoon logs --stderr 2de7fda8

	# Show timestamps for log entries
	> spoon logs -t 2de7fda8

	# Similar to Unix 'tail', only show last 5 lines
	> spoon logs --tail=5 2de7fda8