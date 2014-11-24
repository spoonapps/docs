### try

The `try` command creates a new, temporary container which is removed once it is closed.

```
Usage: spoon try <options> <image> [<parameters>...]

<options> available:
      --disable=VALUE        Disable the specified Spoon VM setting
  -e, --env=VALUE            Set environment variables inside the container
      --enable=VALUE         Enable the specified Spoon VM setting
      --env-file=VALUE       Read in a line delimited file of ENV variables
      --hosts=VALUE          Add an en to the virtual /etc/hosts file (<redirect>:<name>)
      --link=VALUE           Add link to another container (<container>:<alias>)
      --route-add=VALUE      Add a TCP or UDP mapping, format: [<hostPort>]:<containerPort>[/tcp|udp]
      --route-block=VALUE    Isolate all ports of specified protocol (TCP or UDP) by default
      --startup-file=VALUE   Override the default startup file
      --startup-file-commit=VALUE
                             Override the default startup file and save it to the committed image
      --trigger=VALUE        Execute named group of startup files
      --vm=VALUE             The Spoon VM version to run the container with
  -w, --working-dir=VALUE    Set the initial working directory inside the container
      --wait-after-error     Leave program open after error
      --wait-after-exit      Leave program open after it exits
```

Spoon `try` can be used to specify multiple images by separating each image with a comma. If the same file, registry entry, or environment variable exists in multiple images, then the one from whichever image was specified last will win the conflict and be used in the virtual environment. Virtual machine settings are taken from the last image specified in the `from` instruction.

Due to this "layering" approach, it is a good practice to specify images with newer versions of applications or libraries after images with older versions.

```
# Create a container using the apache/apache image
> spoon try apache/apache

# Create a container with apache and mysql
> spoon try apache/apache,mysql/mysql

# Create a container with .NET 3 and 4
> spoon try microsoft/dotnet:4.0.3,microsoft/dotnet:3.5.1
```

Containers are started with the startup file specified in the last passed image. If a startup file is not set in the base image then `cmd.exe /k` is used. 
	
```
# Default startup file is used to start container
> spoon try oracle/jdk

# Override the startup file to use the command prompt
> spoon try --startup-file=cmd.exe oracle/jdk
```

The initial working directory for the container can be set with the `workdir` instruction or the `-w` flag. The current directory will be used if `workdir` was not specified and no `--startup-file` parameter was provided when building the image. 

```
# By default, a container's working directory matches the host's working directory
C:\Users>spoon try git/git

(0x3842xd) C:\Users>

# This sets the working directory to the root of the C drive
C:\Users> spoon try -w="C:\" git/git

(0x3842xd) C:\> 

```

Spoon VM settings can be enabled or disabled with the `--enable` and `--disable` flags, respectively. For a list of Spoon VM settings, see **VM Settings** section of the documentation.

Please note that `spoon.exe` always runs outside of the container on the host even if executed from within the container.

#### Adding Environment Variables

Environment variables can be added to a container with the `-e` or `--env-file` flags. 

```
# Add environment variable 'foo' with value 'bar'
> spoon try -e=foo=bar <image>

# Specify multiple env vars with multiple flags
> spoon try -e=foo=bar -e=x=2 <image>
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

> spoon try -e=%PATH%;C:\Users <image>

(2fedfja3) > echo %PATH%
C:\Windows\system32;C:\Windows;C:\Users	
```

#### Port Mapping

All network operations (opening/closing ports, for example) are passed through to the local machine. To remap container ports to other ports on the local machine, use the `--route-add` flag. Specific protocols (tcp or udp) can be mapped by specifying a `/[protocol]` after the mapping. If no protocol is specified, tcp is assumed.

```
# Map container tcp port 8080 to local port 80
> spoon try --route-add=80:8080 <image>

# Map udp traffic on container port 8080 to local port 80
> spoon try --route-add=80:8080/udp <image>

# Map container tcp port 80 to random port on local machine
# The random port can be later queried using the netstat command
> spoon try --route-add=:80 <image>
```

The default policy of allowing containers to bind to any ports on the local machine can be changed with the `--route-block` flag. It isolates all services bound to container ports on specified protocols (tcp or udp). They can only be opened using the `--route-add` flag.

```
# Isolate all tcp services of a container
> spoon try --route-block=tcp <image>

# Isolate all tcp and udp services, but allow container tcp port 3486
# be bound to port 80 on local machine
> spoon try --route-block=tcp,udp --route-add=80:3486 <image>
```

#### Adding Custom Name Resolution Entries

All containers use name resolution provided by the host operating system. You can add specific name resolution overrides using the `--hosts` flag. The syntax is similar to that of the `hosts` file of the operating system.

```
# Make name my-test-service resolve to whatever the name
# test-service-43 resolves
> spoon try --hosts=my-test-service:test-service-43 <image>

# Make name mysite.net resolve to IPv4 address 127.0.0.1 and
# name ipv6.mysite.net resolve to IPv6 address ::1
> spoon try --hosts=127.0.0.1:mysite.net --hosts=::1:ipv6.mysite.net <image>
```

#### Linking Containers Together

If you decided to not expose any services running in a container to the public by specifying the `--route-block` flag and not `--route-add`, you may still want to be able to connect to the services in your container from another container on the same machine. This is where container linking can be used.

When creating a container with the `spoon try` command, you can use the `--link` flag to link it to any existing containers and the new container will be able to connect to any services exposed by the linked containers. Such connection creates a parent-child relationship where the newly created container is the parent.

With each link, an alias name must be specified. Name resolution overrides are added to the parent container so it can refer to its children by these names.


#### Using Startup Triggers

Images can be created with SpoonScript that have multiple startup files. Collections of startup files can be linked together by a trigger name and executed together.

```
# in spoon.me file to create "test-trigger" image...
startup file ["c:\windows\system32\notepad.exe", "c:\windows\regedit.exe"]
startup file doc=[("c:\windows\system32\notepad.exe", "c:\doc\welcome.txt"), ("c:\windows\system32\notepad.exe", "c:\doc\howto.txt")]


# from command-prompt...

# launch both notepad and regedit are launched
> spoon try test-trigger

# launch welcome.txt and howto.txt in notepad
> spoon try test-trigger --trigger=doc
```


#### Selecting VM version

A specific VM version can be selected by using the `--vm=version` flag. If the selected version is lower than the minimum version that is required by spoon.exe, then the minimum version will be used instead.
