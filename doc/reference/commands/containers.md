# containers

The `containers` command lists all containers on the local machine. It returns the same result as `spoon ps -a`. 

By default, the output of `containers` will be truncated and space-formatted to fit within the width of the current command prompt. To prevent truncation, add the `--no-trunc` flag to this command. To return the table with tab-separated columns, add the `--csv` flag. 

## Command Line Flags

Command line flags for the `containers` flag serve to modify or filter the results returned by the `containers` command. 

If the `containers` command is run without flags, it will return only the containers currently running on the local machine. 

#### Filtering Results

###### List all containers

To list all the containers on the local machine, both running and non-running, specify the `-a` or `--all` flag. 

	>spoon containers -a

###### Only show the most recently created container

To only list the most recently created container, specify the `-l` or `--latest` flag. 

	>spoon containers -l

Both running and stopped containers may be returned by the `-l` flag. 

###### Show the 'n' most recently created containers

If you want to see the 'n' most recently created containers, specify the `-n` flag with a value corresponding to the number of most-recently created containers you wish to view. 

For example, the command `spoon containers -n=3` command will return a list of the 3 most-recently created containers. Similar to the `-l` flag, containers returned by this command may be running or stopped. 

If the value specified for `-n` is greater than the number of containers present on the local machine, all of the containers are listed (same result as running `spoon containers -a`). 

#### Formatting Results

###### Return the table as a tab-separated CSV

By default, the table that is returned by the `containers` command is space-formatted. If you wish to return the table with tabs (`\t`) between each column, add the `--csv` flag to the `ps` command. 

	C:\>spoon containers --csv

###### Don't truncate data

Data in the table returned by the `containers` command is, by default, truncated so that it prints nicely and is easily readable in a command prompt. If you wish to view the untruncated data in each column, specify the `--no-trunc` flag. 

	C:\>spoon containers --no-trunc