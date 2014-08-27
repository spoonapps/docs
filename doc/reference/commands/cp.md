### cp

The cp command copies a file or directory from one container to another. It can also copy a file or directory from a container to the native filesystem. 

	# copy a file from a container to the native system
	> spoon cp 2de7:C:\project\file.txt C:\Users\Spoonuser

	# copy a file from a container to another container
	> spoon cp 2de7:C:\project\file.txt 3vj3:C:\other-project

	# container paths must be absolute
	> spoon cp 2de7:file.txt C:\Users\Spoonuser
	ERROR

	# native paths are relative to the current prompt
	C:\Users> spoon cp 2de7:C:\project\file.txt \Spoonuser