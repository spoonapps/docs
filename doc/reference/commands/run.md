### run

The run command creates new containers.

The **base image** must be a valid Spoon image (`.svm` file extension) and must also exist in your local registry. If the image does not exist in your local registry, the Spoon IDE will try and find a matching one on the Spoonium Hub and download it before starting the container. 

Containers are started with the startup file specified in the base image. If a startup file is not set in the base image, the default of `%COMSPEC%` is applied. 

For example, to print "Hello World" to the command prompt in the new container with the command: 

	> spoon run --startupFile=cmd.exe <image> -- /c echo Hello World

**Note**: The container created with this command will shut down after the `echo` command finishes. To keep the container "alive", the `cmd.exe` process must continue running. In this case, we can accomplish this by passing the `/k` flag to `cmd.exe`. 

	> spoon run  --startupFile=cmd.exe <image> -- /k echo Hello World

When passing arguments to a startupfile or command, we recommend separatign these arguments from the rest of the command with a `--`. Arguments specified after a `--` mark are passed directly to the startup file/command.

If a `--` mark is not used, any argument matching a `spoon run` flag will be passed to `spoon`, which may lead to unexpected behavior. 

    # spoon will interpret the /d flag and execute a container in detached mode
    > spoon run spoonbrew/scratch /d
    
    # /d flag is passed to cmd.exe, disabling execution of AutoRun commands from the registry
    > spoon run spoonbrew/scratch -- /d 

A container's standard streams (`STDIN`, `STDOUT`, `STDERR`) can be redirected to either the current command prompt or the background using the `attach` and `detach` flags. 

To redirect all standard streams to the current command prompt, add the `-a` or `--attach` flag to the run command. 

	> spoon run -a <image>

To "detach" the new container from the native command prompt, specify the `-d` or `--detach` flag. This will create a new container without blocking futher work in the native prompt. 

The initial working directory for the container can be set with the `-w` or `--working-dir` flag. If the `-w` flag is not specified, the initial working directory of the container is inherited from the native command prompt. 

	C:\Users>spoon run spoonbrew/git
	
	# Default to the current directory of the native prompt
	(08fx44zq) C:\Users>

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