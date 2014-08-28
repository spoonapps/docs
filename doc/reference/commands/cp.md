### cp

The cp command copies a file or directory from one container to another. It can also copy a file or directory from a container to the native filesystem. 

	# Copy a file from a container to the native system
	> spoon cp 2de7:C:\project\file.txt C:\Users\Spoonuser

	# Copy a file from a container to another container
	> spoon cp 2de7:C:\project\file.txt 3vj3:C:\other-project

	# Container paths must be absolute
	> spoon cp 2de7:file.txt C:\Users\Spoonuser
	
	ERROR

	# Native paths are relative to the current prompt
	C:\Users> spoon cp 2de7:C:\project\file.txt \Spoonuser