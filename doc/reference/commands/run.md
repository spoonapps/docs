### run

The run command creates new containers.

	# create a container using the spoonbrew/apache image
	> spoon run spoonbrew/apache

	# create a container with apache and mysql
	> spoon run spoonbrew/apache;spoonbrew/mysql

Containers are started with the startup file specified in the base image. If a startup file is not set in the base image, the default of `%COMSPEC% /k` is applied. 
	
	# default startup file is used to start container
	> spoon run spoonbrew/jdk

	# override the startup file to use the command prompt
	> spoon --startupFile=cmd.exe run spoonbrew/jdk

When passing arguments to a startupfile or command, we recommend separating these arguments from the rest of the command with a **--**. Arguments specified after a **--** mark are passed directly to the startup file/command.

If a **--** mark is not used, any argument matching a run command flag will be interpreted by Spoon, which may lead to unexpected behavior. 

    # spoon will interpret the /d flag and execute a container in detached mode
    > spoon run spoonbrew/scratch /d
    
    # /d flag is passed to cmd.exe, disabling execution of AutoRun commands from the registry
    > spoon run spoonbrew/scratch -- /d 

A container's standard streams (stdin/out/err) can be redirected to either the current command prompt or the background using the **--attach** and **--detach** flags. 

	# redict standard streams to current command prompt
	> spoon run -a <image>

	# detach the container from the native prompt
	> spoon run -d <image>

Detaching from a container will allow further work to be done in the native prompt while the container is running.  

The initial working directory for the container can be set with **-w** flag. 

	# Set working directory to root of C: drive
	C:\Users> spoon run -w="C:\" spoonbrew/git

	(0x3842xd) C:\> 

	# By default, container working directory matches native
	C:\Users>spoon run spoonbrew/git
	
	(0x3842xd) C:\Users>

#### Adding Environment Variables

Environment variables can be added to a container with the **-e** or **--env-file** flags. 

	# add environment variable 'foo' with value 'bar'
	> spoon run -e=foo=bar <image>

	# specify multiple env vars with multiple flags
	> spoon run -e=foo=bar -e=x=2 <image>

If your container requires several environment variables, we recommend creating an **env-file**, a line-delimited text file that lists all the environment variables to add to the container. The example file, below, lists 3 environment variables: 

	foo=bar
	utensil=spoon
	my-var=10

Environment variables are always expanded on the host system before they are added to the container. 

	> echo %PATH%
	C:\Windows\system32;C:\Windows;

	> spoon run -e=%PATH%;C:\Users <image>

	(2fedfja3) > echo %PATH%
	C:\Windows\system32;C:\Windows;C:\Users	

Spoon VM settings can be enabled or disabled with the `--enable` and `--disable` flags, respectively. 

When the `--diagnostic` flag is included, the container will generate diagnostic logs that detail all of the operations that occur within the container. 

These diagnostic logs can later be viewed using the `spoon logs` command. 

#### Port Mapping

By default, all network operations (opening/closing ports, for example) are passed through to the local machine. To remap container ports to other ports on the local machine, use the **-p** or **-P** flags. Specific protocols (tcp or udp) can be mapped by specifying a **/[protocol]** after the mapping. 

	# map container port 8080 to local port 80
	> spoon run -p=80:8080 <image>

	# map udp traffic on container port 8080 to local port 80
	> spoon run -p=80:8080/udp <image>

	# map all container ports to random ports on the local machine
	> spoon run -P <image>