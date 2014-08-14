# top

The `top` command displays all the running processes within a container. For those familiar with Unix, `spoon top` is very similar to executing the Unix command `ps` inside of the specified container. 

The `top` command will, by default, return a table that lists the `PID`, `NAME`, and `USER` associated with each process running in the container. 

## Long Format

The `top` command also has an optional command line flag, `-l` which will return a *long format* table. This long format table includes the additional columns: `UTIME`, `KTIME`, and `COMMAND`. 

## Table Columns

	PID					ID of the process
	NAME				Name of the process
	USER				User account that the process is running under
	UTIME				User space CPU time
	KTIME				Kernel space CPU time
	COMMAND				The command the process was started with



