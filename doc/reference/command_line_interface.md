# Command Line Interface

To list available commands, either run `spoon` without parameters

	spoon

or run `spoon help`

	spoon help

The Spoon command line interface is also aliased as `spn`. Thus, when using Spoon's command line interface you may prefix commands with `spoon` or `spn`. 

## build

	'build' - Build a new image from a Spoon.me build script or XAPPL configuration file

	Usage: spoon build <options> <path>
	Example: spoon build -n="My Container" -w="C:\myapp" -e=VAR1=foo "C:\directory\installscript.me"

	<path>: path to Spoon.me script or .xappl configuration file
	<options> available:
		-n, --name=VALUE			Name of the image
		-w, --working-dir=VALUE		The initial working directory of the container
		-e, --env=VALUE				Environment variable (and it's value) to add to the container
		--env-file=VALUE			Specify a line-delimited file of environment variables to add to the container
		--xvm=VALUE					The Spoon VM to use
		--diagnostic				Enable diagnostic logging
		
## commit

	'commit' - Create a new image from a container

	Usage: spoon commit <options> <container> <image>
	Example: spoon commit --no-base 55kj8dx my-new-image

	<container>: the ID of the container to build a new image from
	<image>: the name of the image to be built
	<options> available:
		--no-base				Build the container without including base images

## config

	'config' - 	View and modify configuration settings

	Usage: spoon config <options>
	Example: spoon config --hub=http://spoonium.net

	<options> available:
		--hub=VALUE				The remote registry to push to and pull from

## cp

	'cp' - Copy a file or directory from a container to the local machine

	Usage: spoon cp <container>:<path> <local path>
	Example: spoon cp 55kj8dx:C:\root\file.txt C:\Users\Administrator

	<container>: the container to copy from
	<path>: the absolute path to the file or directory to copy
	<local path>: the absolute or relative destination path for the copied file or directory
		
## diff

	'diff' - Inspect changes to a container's filesystem and/or registry

	Usage: spoon diff <options> <container>
	Example: spoon diff 55kj8dx
	
	<container>: the ID of the container to inspect
	<options> available: 
		--path=VALUE				Only show changes below this directory in the filesystem tree

## export

	'export' - Copy a Spoon image in the local registry to a path on the local machine
	
	Usage: spoon export <image> <path>
	Example: spoon export my-new-image:master C:\images
	
	<image>: The image to export
	<path>: The directory to copy the image to

## images

	'images' - List the images in the local registry

	Usage: spoon images <options>
	Example: spoon images

	<options> available:
		--csv					Print the output with tab-separated columns
		--no-trunc				Do not truncate columns

## import

	'import' - Build an image from the specified file and adds it to the local registry

	Usage: spoon import <options> <filetype> <path>
	Example: spoon import -n="my-new-image" \\f2\images\image.svm
			 spoon import -n="my-msi-image" C:\root\app.msi

	<filetype>: the type of file to import.
		-svm 					Spoon image file
		-msi						Microsoft software installer
		-thinapp					Thinapp configuration file 
	<path>: the path to the spoon image to import
	<options> available:
		-n, --name				The name to give the imported image

## login

	'login' - Log the user into the remote registry. 

	Usage: spoon login <username> <password>
	Example: spoon login my-new-username fake-password

## logout

	'logout' - Log the current user out

	Usage: spoon logout
	Example: spoon logout


## logs

	'logs' - Fetch diagnostic logs for a container

	Usage: spoon logs <options> <container>
	Example: spoon logs -t 55kj8dx

	<container>: the ID of the container to fetch the logs of
	<options> available: 
		-f								Follow log output
		-t								Show timestamps of log entries
			--tail=VALUE				Only show the specified number of lines from the end of the logs
			--stdout					Fetch the stdout logs
			--stderr					Fetch the stderr logs

## ps

	'ps' - List the running containers on the device

	Usage: spoon ps <options>
	Example: spoon ps --all

	<options> available:
		-a, --all						List all containers on the device, running and non-running
			--csv					 	Print output with tab-separated columns
			--no-trunc					Do not truncate columns
		-l, --latest						List the most recently created container, running or non-running
		-n=VALUE							List the 'n' most recently created containers, running and non-running

## pull

	'pull' - Copy an image from a remote hub to the local registry

	Usage: spoon pull [<repository>/]<image>[:<tag>]
	Example: spoon pull spoonbrew/git:master

## push

	'push' - Upload the specified image to the remote hub

	Usage: spoon push [<repository>] <image>[:<tag>]
	Example: spoon push my-new-repo my-new-image
			 spoon push my-new-image:1.0

## rm

	'rm' - Remove one or more containers from the local machine
	
	Usage: spoon rm <options> <container>
	Example: spoon rm 55kj8dx

	<container>: the ID of the container to remove
	<options> available:
		-a, --all: 						Remove all containers on the local machine

## rmi 

	'rmi' - Remove one or more images from the local machine

	Usage: spoon rmi <options> <image>
	Example: spoon rmi my-new-image

	<image>: the name of the image to remove
	<options> available: 
		-a, --all:						Remove all images on the local machine

## run

	'run' - Create and run a command in a container

	Usage: spoon run <options> <image> <command> [<args>...]
	Example: spoon run -a spoonbrew/nuget cmd.exe
			 spoon run -w=C:\ my-new-image cmd.exe

	<image>: the base image to run the container on top of
	<command>: the command to run in the container
	<args>: (optional) arguments to pass to the <command>
	<options> available:
		-a, --attach					Redirect stdin, stdout, and stderr of the container to the current command prompt
		-d, --detach					Do not show stdin, stdout, and stderr of the container
		-e, --env=VALUE					Add the specified environment variable to the container
			--env-file=VALUE				Add all environment variables in the line-delimited file to the container
		-w, --working-dir=VALUE			The initial working directory of the container
			--diagnostic					Enable diagnostic logging in the container
			--disable=VALUE				Disable the specified container setting
			--enable=VALUE				Enable the specified container setting
			--xvm=VALUE					The Spoon VM version to run the new container with

## start

	'start' - Restart a container that is not running

	Usage: spoon start <container>
	Example: spoon start 55kj8dx

	<container>: The ID of the container to restart

## tag

	'tag' - Create a copy of an image with a new name

	Usage: spoon tag <image> [<namespace>/]<name>:<tag>
	Example: spoon tag spoonbrew/git:master user/my-git:master
			 spoon tag my-new-image:master user/my-new-image:1.0

	<image>: the name of the image to rename. Includes the image's namespace or tag, if applicable
	<namespace>: the namespace of the new copy
	<name>: the name of the new copy
	<tag>: the tag of the new copy

## top

	'top' - Display the running processes in a container
	
	Usage: spoon top <options> <container>
	Example: spoon top 55kj8dx

	<container>: the ID of the container to examine
	<options> available: 
		-l						Display long-formatted table of results

## version

	'version' - Show the current version of the Spoon IDE
	Usage: spoon version
