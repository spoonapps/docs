## ps

The `ps` command returns a list of all the containerized processes running on the local machine. 

By default, only the **PID**, **NAME**, **CONTAINER** and **USER** are returned for each process. 

To view the **UTIME** (user time), **KTIME** (kernel time), and **COMMAND** for each process, specify the `-l` flag. 

	> spoon ps -l

To return the table with tab-separated columns, specify the `--csv` flag. 

	> spoon ps --csv

By default, Spoon will truncate data in each column to a set width. To return untruncated data, use the `--no-trunc` flag. 

	> spoon ps --no-trunc