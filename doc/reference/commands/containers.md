### containers

The containers command lists all containers on the local machine.  

Command line flags for the `containers` flag serve to modify or filter the command's results. 

	# Only show most recently created container
	> spoon containers -l

	ID				Images				Command   	Created 			Status
	--				------				-------		-------- 			------
	2de7fdf613dd	spoonbrew/scratch	cmd.exe 	8/25/2014 5:47:36	Stopped

	# Show last 'n' created containers
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

The `--no-trunc` flag includes additional columns in the output. Namely, **Ports** and **Settings** columns, as seen below.

	ID                                Images       Command  Created               Status   Ports      Settings
	--                                ------       -------  -------               ------   -----      --------
	df6ac93f8b6147b986d4c7849c3dcef0  ghost:0.5.1           8/26/2014 3:27:17 PM  Running  8080:2368  SpawnVm
	d6e44ae706c44ed1bd75a0830bed3239  ghost:0.5.1           8/26/2014 3:22:14 PM  Stopped             SpawnVm

The **Ports** column contains active port mappings, like the `spoon netstat` command.
