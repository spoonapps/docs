### run

The `run` command creates a new container.

```
Usage: spoon run <options> <image> [<parameters>...]

<options> available:
  -a, --attach               Attach to stdin, stdout, and stderr of the container
  -d, --detach               Run the container in the background
      --diagnostic           Enable diagnotic logging
      --disable=VALUE        Disable the specified Spoon VM setting
  -e, --env=VALUE            Set environment variables inside the container
      --enable=VALUE         Enable the specified Spoon VM setting
      --env-file=VALUE       Read in a line delimited file of ENV variables
      --hosts=VALUE          Add an entry to the virtual /etc/hosts file (<redirect>:<name>)
      --link=VALUE           Add link to another container (<container>:<alias>)
      --route-add=VALUE      Add a TCP or UDP mapping format: [<hostPort>]:<containerPort>[/tcp|udp]
      --route-block=VALUE    Isolate all ports of specified protocol (TCP or UDP) by default
      --startup-file=VALUE    Override the default startup file
      --trigger=VALUE        Execute named group of startup files
      --vm=VALUE             The Spoon VM version to run the container with
  -w, --working-dir=VALUE    Set the initial working directory inside the container
      --wait-after-error     Leave program open after error
```

Specify multiple base images by separating with a comma. If two images contains the same file - first one is taken. Always ensure that images with new versions of applications/libraries are passed first. Virtual machine settings are taken from last image in the list.

```
# Create a container using the spoonbrew/apache image
> spoon run spoonbrew/apache

# Create a container with apache and mysql
> spoon run spoonbrew/apache,spoonbrew/mysql

# Create a container with .NET 3 and 4
> spoon run spoonbrew/dotnet:4.0.3,spoonbrew/dotnet:3.5.1
```

Containers are started with the startup file specified in the last passed image. If a startup file is not set in the base image then `cmd.exe /k` is used. 
	
```
# Default startup file is used to start container
> spoon run spoonbrew/jdk

# Override the startup file to use the command prompt
> spoon run --startup-file=cmd.exe spoonbrew/jdk
```

When passing arguments to a startupfile or command, we recommend separating these arguments from the rest of the command with a `--`. Arguments specified after the `--` mark are passed directly to the startup file/command.

If a `--` mark is not used, any argument matching a `run` command flag will be interpreted by Spoon which may lead to unexpected behavior. 

```
  # Spoon will interpret the /d flag and execute a container in detached mode
  > spoon run spoonbrew/scratch /d
  
  # /d flag is passed to cmd.exe, disabling execution of AutoRun commands from the registry
  > spoon run spoonbrew/scratch -- /d 
```

A container's standard streams (stdin/out/err) can be redirected to either the current command prompt or the background using the `--attach` and `--detach` flags. 

```
# Redict standard streams to current command prompt
> spoon run -a <image>

# Detach the container from the native prompt
> spoon run -d <image>
```

Detaching from a container will allow further work to be done in the native prompt while the container is running.  

The initial working directory for the container can be set with `-w` flag. 

```
# Set working directory to root of C: drive
C:\Users> spoon run -w="C:\" spoonbrew/git

(0x3842xd) C:\> 

# By default, container working directory matches native
C:\Users>spoon run spoonbrew/git

(0x3842xd) C:\Users>
```

Spoon VM settings can be enabled or disabled with the `--enable` and `--disable` flags, respectively. For a list of Spoon VM settings, see **VM Settings** section of the documentation.

When the `--diagnostic` flag is used, the container will generate diagnostic logs that detail all of the operations that occur within the container. These diagnostic logs can later be viewed using the `spoon logs` command and be used to troubleshoot errors and configuration issues. 

#### Adding Environment Variables

Environment variables can be added to a container with the `-e` or `--env-file` flags. 

```
# Add environment variable 'foo' with value 'bar'
> spoon run -e=foo=bar <image>

# Specify multiple env vars with multiple flags
> spoon run -e=foo=bar -e=x=2 <image>
```

If your container requires several environment variables then we recommend creating an **env-file**. An **env-file** is a line-delimited text file that lists all the environment variables to add to the container. The example file below lists 3 environment variables: 

```
foo=bar
utensil=spoon
my-var=10
```

Environment variables are always expanded on the host system before they are added to the container. 

```
> echo %PATH%

C:\Windows\system32;C:\Windows;

> spoon run -e=%PATH%;C:\Users <image>

(2fedfja3) > echo %PATH%
C:\Windows\system32;C:\Windows;C:\Users	
```

#### Port Mapping

All network operations (opening/closing ports, for example) are passed through to the local machine. To remap container ports to other ports on the local machine, use the `--route-add` flag. Specific protocols (tcp or udp) can be mapped by specifying a `/[protocol]` after the mapping. If no protocol is specified, tcp is assumed.

```
# Map container tcp port 8080 to local port 80
> spoon run --route-add=80:8080 <image>

# Map udp traffic on container port 8080 to local port 80
> spoon run --route-add=80:8080/udp <image>

# Map container tcp port 80 to random port on local machine
# The random port can be later queried using the netstat command
> spoon run --route-add=:80 <image>
```

The default policy of allowing containers to bind to any ports on the local machine can be changed with the `--route-block` flag. It isolates all services bound to container ports on specified protocols (tcp or udp). They can only be opened using the `--route-add` flag.

```
# Isolate all tcp services of a container
> spoon run --route-block=tcp <image>

# Isolate all tcp and udp services, but allow container tcp port 3486
# be bound to port 80 on local machine
> spoon run --route-block=tcp,udp --route-add=80:3486 <image>
```

#### Adding Custom Name Resolution Entries

All containers use name resolution provided by the host operating system. You can add specific name resolution overrides using the `--hosts` flag. The syntax is similar to that of the `hosts` file of the operating system.

```
# Make name my-test-service resolve to whatever the name
# test-service-43 resolves
> spoon run --hosts=my-test-service:test-service-43 <image>

# Make name mysite.net resolve to IPv4 address 127.0.0.1 and
# name ipv6.mysite.net resolve to IPv6 address ::1
> spoon run --hosts=127.0.0.1:mysite.net --hosts=::1:ipv6.mysite.net <image>
```

#### Linking Containers Together

If you decided to not expose any services running in a container to the public by specifying the `--route-block` flag and not `--route-add`, you may still want to be able to connect to the services in your container from another container on the same machine. This is where container linking can be used.

When creating a container with the `spoon run` command, you can use the `--link` flag to link it to any existing containers and the new container will be able to connect to any services exposed by the linked containers. Such connection creates a parent-child relationship where the newly created container is the parent.

With each link, an alias name must be specified. Name resolution overrides are added to the parent container so it can refer to its children by these names.


##### Example

First create two containers, each exposing web sites on private port 80, but with no services exposed outside the containers. Run them in detached mode.

```
> spoon run --route-block tcp,udp -d <image>

05bf1aa429204d1586487f4015e1428c

> spoon run --route-block tcp,udp -d <image>

94a38820b45443c9ac74792215e33a00
```

Then create a web browser container linked to the previously created containers.

```
> spoon run --link 05bf:web1 --link 94a3:web2 myself/webbrowser http://web1 http://web2
```

You will be able to browse websites served by the linked containers even though they are not publically available.


#### Using Startup Triggers

Images can be created with SpoonScript that have multiple startup files. Collections of startup files can be linked together by a trigger name and executed together.

```
# in spoon.me file to create "test-trigger" image...
startup file ["c:\windows\system32\notepad.exe", "c:\windows\regedit.exe"]
startup file doc=[("c:\windows\system32\notepad.exe", "c:\doc\welcome.txt"), ("c:\windows\system32\notepad.exe", "c:\doc\howto.txt")]


# from command-prompt...

# launch both notepad and regedit are launched
> spoon run test-trigger

# launch welcome.txt and howto.txt in notepad
> spoon run test-trigger --trigger=doc
```
