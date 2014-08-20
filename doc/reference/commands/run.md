## run

The `run` command creates new containers.

The `run` command requires an `<image>` be specified -- this will be the base image(s) for the new container.  

The **base image** must be a valid Spoon image (`.svm` file extension) and must also exist in your local registry. If the image does not exist in your local registry, the Spoon IDE will try and find a matching one on the Spoonium Hub and download it before starting the container. 

For example, to start a new command prompt in the container, execute: 

	> spoon run <image> cmd.exe

Similarly, I could print "Hello World" to the command prompt in the new container with the command: 

	> spoon run <image> cmd.exe echo Hello World

**Note**: The container created with this command will shut down after the `echo` command finishes. To keep the container "alive", the `cmd.exe` process must continue running. In this case, we can accomplish this by passing the `/k` flag to `cmd.exe`. 

	> spoon run <image> cmd.exe /k echo Hello World

A container's standard streams (`STDIN`, `STDOUT`, `STDERR`) can be redirected to either the current command prompt or the background using the `attach` and `detach` flags. 

To redirect all standard streams to the current command prompt, add the `-a` or `--attach` flag to the run command. 

	> spoon run -a <image> cmd.exe

To prevent the execution of the new container from blocking the native command prompt, specify the `-d` flag.

The initial working directory for the container can be set with the `-w` or `--working-dir` flag. If the `-w` flag is not specified, the initial working directory of the container is inherited from the native command prompt. 

	C:\Users>spoon run spoonbrew/git cmd.exe
	
	(08fx44zq) C:\Users>

Environment variables can be added to a container with the `-e`, `--env`, or `--env-file` flags. 

For example, to add the environment variable `foo` with value `bar` to a new container, the flag `-e=foo=bar` would be added to the `spoon run` command. 

Multiple `-e` or `--env` flags can be added to a single `run` command to add multiple environment variables. 

	> spoon run -e=foo=bar -e=x=2 <image> cmd.exe 

If your container requires several environment variables, we recommend creating an `env-file` for the container. An `env-file` is a line-delimited text file that lists environment variable key-value pairs on each line. The example file, below, lists 3 environment variables: 

	foo=bar
	utensil=spoon
	my-var=10

Environment variables are always expanded on the host system before they are added to the container. 

For example, when adding new paths to the `PATH` variable, adding the flag `-e=%PATH%;<new path>` to the `spoon run` command will create a `PATH` variable in the container that consists of the `<new path>` appended to the native system `PATH`. 

Spoon VM settings can be enabled or disabled with the `--enable` and `--disable` flags, respectively. 

When the `--diagnostic` flag is included, the container will generate diagnostic logs that detail all of the operations that occur within the container. These are especially useful when debugging 

These diagnostic logs can later be viewed using the `spoon logs` command. 