# containers

The `containers` command lists all containers on the local machine. It returns the same result as `spoon ps -a`. 

By default, the output of `containers` will be truncated and space-formatted to fit within the width of the current command prompt. To prevent truncation, add the `--no-trunc` flag to this command. To return the table with tab-separated columns, add the `--csv` flag. 