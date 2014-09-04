### startup file

The `startup file` instruction is used to specify the startup file or script to run when a new container is created from this image (using `spoon run`).

The instruction has four forms: 

1. `startup file ("executable", "param1", "param2")` (executes the application directly)
2. `startup file [("executable1", "param1", "param2"), ("executable2", "param1", "param2"), ...]` (executes the list of applications directly)
3. `startup file <command> <param1> <param2>` (command is interpreted by cmd.exe, defaults to using "cmd.exe /k")
4. `startup file <param1> <param2>` (parameters are sent to the base image's startup file)

This instruction is only applied to the output image and does not affect the intermediate container. 

#### As an Executable

If you wish to launch a process from an executable and optionally supply parameters to that executable, you must express the desired *executable* as a tuple of strings and give the full path to the executable (unless it is on the local system or container's `PATH`). Using this syntax, parameters are passed directly to the executable. 

```
# "clone" and "https://github.com/spoonium/docs" are passed to git.exe
startup file ["git.exe", "clone", "https://github.com/spoonium/docs"]
```

#### As a Shell Command

Using this syntax, each command is executed in its own command prompt -- a new command prompt being spawned for each instruction. Thus, any stateful commands (`cd`, for example), must be chained to other commands with an ampersand to have their desired effect. 

For example, to read a file in the **C:\Spoon** directory: 

```
# Hello world is passed to the 'echo' command
startup file echo hello world
```

#### As Parameters

Using this syntax, the parameters are sent to the default startup file in the base image. If multiple base images are specified, the startup file from the last specified image will be used.
