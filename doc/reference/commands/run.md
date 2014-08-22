## run

The `run` command creates new containers.

The `run` command requires an `<image>` be specified -- this will be the base image(s) for the new container.  

The **base image** must be a valid Spoon image (`.svm` file extension) and must also exist in your local registry. If the image does not exist in your local registry, the Spoon IDE will try and find a matching one on the Spoonium Hub and download it before starting the container. 

Containers are started with the startup file specified in the base image. If a startup file is not set in the base image, a default of `%COMSPEC%` is applied. 

For example, to print "Hello World" to the command prompt in the new container with the command: 

	> spoon run --startupFile=cmd.exe <image> -- /c echo Hello World

**Note**: The container created with this command will shut down after the `echo` command finishes. To keep the container "alive", the `cmd.exe` process must continue running. In this case, we can accomplish this by passing the `/k` flag to `cmd.exe`. 

	> spoon run  --startupFile=cmd.exe <image> -- /k echo Hello World

A container's standard streams (`STDIN`, `STDOUT`, `STDERR`) can be redirected to either the current command prompt or the background using the `attach` and `detach` flags. 

To redirect all standard streams to the current command prompt, add the `-a` or `--attach` flag to the run command. 

	> spoon run -a <image>

To "detach" the new container from the native command prompt, specify the `-d` or `--detach` flag. This will create a new container without blocking futher work in the native prompt. 

The initial working directory for the container can be set with the `-w` or `--working-dir` flag. If the `-w` flag is not specified, the initial working directory of the container is inherited from the native command prompt. 

	C:\Users>spoon run spoonbrew/git
	
	# Default to the current directory of the native prompt
	(08fx44zq) C:\Users>

Environment variables can be added to a container with the `-e`, `--env`, or `--env-file` flags. 

For example, to add the environment variable `foo` with value `bar` to a new container, add the flag `-e=foo=bar`. 

Multiple `-e` or `--env` flags can be added to a single `run` command to add multiple environment variables. 

	> spoon run -e=foo=bar -e=x=2 <image>

If your container requires several environment variables, we recommend creating an `env-file` for the container. An `env-file` is a line-delimited text file that lists environment variable key-value pairs on each line. The example file, below, lists 3 environment variables: 

	foo=bar
	utensil=spoon
	my-var=10

Environment variables are always expanded on the host system before they are added to the container. 

For example, when adding new paths to the `PATH` variable, adding the flag `-e=%PATH%;<new path>` to the `spoon run` command will create a `PATH` variable in the container that consists of the `<new path>` appended to the native system `PATH`. 

Spoon VM settings can be enabled or disabled with the `--enable` and `--disable` flags, respectively. 

When the `--diagnostic` flag is included, the container will generate diagnostic logs that detail all of the operations that occur within the container. These are especially useful when debugging 

These diagnostic logs can later be viewed using the `spoon logs` command. 

When passing arguments to a startupfile or command, we recommend separatign these arguments from the rest of the command with a `--`. Arguments specified after a `--` mark are passed directly to the startup file/command.

If a `--` mark is not used, any argument matching a `spoon run` flag will be passed to `spoon`, which may lead to unexpected behavior. 

    # spoon will interpret the /d flag and execute a container in detached mode
    > spoon run spoonbrew/scratch /d
    
    # /d flag is passed to cmd.exe, disabling execution of AutoRun commands from the registry
    > spoon run spoonbrew/scratch -- /d 