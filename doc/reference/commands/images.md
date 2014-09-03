### images

The `images` command lists all of the images present in the current user's local registry. 

	# List all images in local registry
	> spoon images
	
	ID 			  Name  				Tag	 Created 				Size
	-- 			  ----  				---  -------    			----
	7a85fe8f7ad1  spoonbrew/chocolatey       8/22/2014 11:34:19 AM  3.6 MB

By default, the results of `spoon images` are truncated so that they are most readable in the command prompt. To prevent the Spoon IDE from truncating data, specify the `--no-trunc` flag. 

The `--csv` flag can be specified to return the output of the `spoon image` command as a tab-separated table. 