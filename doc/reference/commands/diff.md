### diff

The diff command shows changes made in a container's filesystem. Changes are shown relative to the base image that the container was created from. 

	# show all changes made in a container
	> spoon diff <container id>

By default, the diff command will show changes in the virtual filesystem and registry. 

	# only show changes to the registry
	> spoon diff --subsystems=registry <container id>

	# only show changse to the filesystem
	> spoon diff --subsystems=files <container id>

To only show changes beneath a certain node in the filesystem or registry directory tree, use the **--path** or **--registry-path** flags. 

	# only show changes in HKCU
	> spoon diff --registry-path=@HKCU@ <container id>

	# only show changes in system32
	> spoon diff --path=C:\Windows\system32

#### Interpreting diff Results

The leading character of each line denotes the type of change made at that path. 

|| **Character** || **Type of Change** ||
|| A || Added ||
|| C || Changed ||
|| D || Deleted ||

If a file is changed, the diff results will show the a change in the folder, along with the change to the file.  
For example, if one added a file to a container at **C:\Users\Spoonuser\file.txt**: 

	> spoon diff --subsystems=files <container id>
	File system changes:
	C C:\Users\Spoonuser
	A C:\Users\Spoonuser\file.txt