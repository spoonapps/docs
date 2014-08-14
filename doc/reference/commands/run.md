# run

The `run` command is used to create new containers. 

The `run` command has 2 required arguments: 

1. The base image(s) to use as a foundation for the container
2. The command to start the container with

The **base image** must be a valid Spoon image (`.svm` file extension) and must also exist in your local registry. If the image does not exist in your local registry, the Spoon IDE will try and find a matching one on the Spoonium Hub and download it before starting the container. 

The **command** to start the image with must be an executable, script, or Windows utility that can run within the container. Any arguments supplied after the **command** are passed as arguments to the command. 

For example, to start a new command prompt in the container, execute: 

	C:\>spoon run <image> cmd.exe

Similarly, I could print "Hello World" to the command prompt in the new container with the command: 

	C:\>spoon run <image> cmd.exe echo Hello World

**Note**: The container created with this command will shut down after the `echo` command finishes. To keep the container "alive", the `cmd.exe` process must continue running. In this case, we can accomplish this by passing the `/k` flag to `cmd.exe`. 

	C:\>spoon run <image> cmd.exe /k echo Hello World

## Command Line Flags

The `run` command accepts several command line parameters that modify the command's behavior at runtime. 

###### Redirecting STDIN, STDOUT, and STDERR

A container's standard streams (`STDIN`, `STDOUT`, `STDERR`) can be redirected to either the current command prompt or the background using the `attach` and `detach` flags. 

To redirect all standard streams to the current command prompt, add the `-a` or `--attach` flag to the run command. 

	C:\>spoon run -a <image> cmd.exe

Likewise, to suppress the standard streams of a container, add the `-d` of `--detach` flag to the run command. 

	C:\>spoon run -d <image> cmd.exe

This will effectively run the container in the background of your computer.

###### Set the Container Working Directory

The initial working directory for the container can be set with the `-w` or `--working-dir` flag. If the `-w` flag is not specified, the initial working directory of the container is inherited from the native command prompt. 

	C:\Users>spoon run spoonbrew/git cmd.exe
	
	(08fx44zq) C:\Users>

###### Create Environment Variables

Environment variables can be added to a container with the `-e`, `--env`, or `--env-file` flags. 

For example, to add the environment variable `foo` with value `bar` to a new container, the flag `-e=foo=bar` would be added to the `spoon run` command. 

Multiple `-e` or `--env` flags can be added to a single `run` command to add multiple environment variables. 

	C:\>spoon run -e=foo=bar -e=x=2 <image> cmd.exe 

If your container requires several environment variables, we recommend creating an `env-file` for the container. An `env-file` is a line-delimited text file that lists environment variable key-value pairs on each line. The example file, below, lists 3 environment variables: 

	foo=bar
	utensil=spoon
	my-var=10

**Environment Variable Expansion**

Environment variables are always expanded on the host system before they are added to the container. 

For example, when adding new paths to the `PATH` variable, adding the flag `-e=%PATH%;<new path>` to the `spoon run` command will create a `PATH` variable in the container that consists of the `<new path>` appended to the native system `PATH`. 


###### Configuring Spoon VM Settings

Spoon VM settings can be enabled or disabled with the `--enable` and `--disable` flags, respectively. 

By default, all VM settings are disabled. 

The list of valid VM settings is: 

- `SpawnVm`
- `ReadOnly`
- `SuppressLogging`
- `AccurateFolders`
- `SpawnComServers`
- `IsolateWindowsClasses`
- `IndicateVirtualization`
- `ReadShare`
- `DRMCompat`
- `ShutdownProcTree`
- `DEPCompat`
- `IndicateElevated`
- `SuppressInjection`
- `FaultExecutables`
- `HonorWow6464Access`
- `SuppressPopups`
- `HideShellWindow`
- `PeriodicRegFlush`
- `EnableDiagnostics`
- `ForceWriteCopyIsolation`
- `EnableCrashLogging`
- `AttachConsole`
- `MergePathEnvVars`
- `MergeVmSettings`
	
###### Enabling Container Diagnostics

When the `--diagnostic` flag is included, the container will generate diagnostic logs that detail all of the operations that occur within the container. These are especially useful when debugging 

These diagnostic logs can later be viewed using the `spoon logs` command. 
