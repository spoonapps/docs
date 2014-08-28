### rmi

The rmi command removes an image, or images, from the local registry. 

	# remove an image by specifying it by name
	> spoon rmi my-image
	
	Image my-image:head was removed

	# remove all images with the -a flag
	> spoon rmi -a
	
	All images have been removed

If the same image is forked or tagged multiple times, the rmi command will only untag the specified name, not remove the image itself. 

	> spoon images
	
	ID 			  Name  				Tag	 Created 				Size
	-- 			  ----  				---  -------    			----
	7a85fe8f7ad1  spoonbrew/chocolatey       8/22/2014 11:34:19 AM  3.6 MB
	7a85fe8f7ad1  chocolatey-forked		1.0  8/22/2014 12:00:01 PM  3.6 MB

	> spoon rmi spoonbrew/chocolatey
	
	Image spoonbrew/chocolatey:head was untagged

	> spoon images
	
	ID 			  Name  				Tag	 Created 				Size
	-- 			  ----  				---  -------    			----
	7a85fe8f7ad1  chocolatey-forked		1.0  8/22/2014 12:00:01 PM  3.6 MB

	> spoon rmi chocolatey-forked:1.0
	
	Image chocolatey-forked:1.0 was removed

