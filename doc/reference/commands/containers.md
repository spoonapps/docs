### containers

The containers command lists all containers on the local machine.  

Command line flags for the `containers` flag serve to modify or filter the command's results. 

	# only show most recently created container
	> spoon containers -l
	ID				Images				Command   	Created 			Status
	--				------				-------		-------- 			------
	2de7fdf613dd	spoonbrew/scratch	cmd.exe 	8/25/2014 5:47:36	Stopped

	# show last 'n' created containers
	> spoon containers -n=3
	ID				Images				Command   	Created 			Status
	--				------				-------		-------- 			------
	2de7fdf613dd	spoonbrew/scratch	cmd.exe 	8/25/2014 5:47:36	Stopped
	3efbdkj34hfd	spoonbrew/node		node app.js 8/25/2014 5:40:21   Running
	2fjdask34hdc	spoonbrew/node		node app.js 8/24/2014 6:00:01   Stopped


If the value specified for `-n` is greater than the number of containers present on the local machine, all of the containers are listed (same result as running `spoon containers -a`). 

#### Formatting Results

By default, the table that is returned by the containers command is space-formatted. If you wish to return the table with tabs (`\t`) between each column, add the `--csv` flag to the `ps` command. 

	> spoon containers --csv

Data in the table returned by the containers command is, by default, truncated so that it prints nicely and is easily readable in a command prompt. If you wish to view the untruncated data in each column, specify the `--no-trunc` flag. 

	> spoon containers --no-trunc