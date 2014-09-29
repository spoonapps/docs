### cmd

The `cmd` instruction is used to run a command in the container. 

The instruction has three forms: 

1. `cmd ("executable", "param1", "param2")` (executes the application directly)
2. `cmd <command> <param1> <param2>` (command is interpreted by cmd.exe, defaults to using "cmd.exe /c")
3. `cmd <param1> <param2>` (parameters are sent to the base image's startup file)

Please note that `spoon.exe` always runs outside of the container on the host even if passed as `cmd` parameter.

#### As an Executable

If you wish to launch a process from an executable and optionally supply parameters to that executable, you must express the desired *executable* as a tuple of strings and give the full path to the executable (unless it is on the local system or container's `PATH`). Using this syntax, parameters are passed directly to the executable. 

```
# open foo.txt in notepad
cmd ("c:\windows\system32\notepad.exe", "c:\users\user\desktop\foo.txt")
```

#### As a Shell Command

Using this syntax, each command is executed in its own command prompt -- a new command prompt being spawned for each instruction. Thus, any stateful commands (`cd`, for example), must be chained to other commands with an ampersand to have their desired effect. 

For example, to read a file in the **C:\Spoon** directory: 

```
# Does not work
cmd cd C:\spoon
cmd more text-file.txt

# Work!
cmd cd C:\spoon & more text-file.txt
```

**Note**: If you wish to use `cd` functionality in your script, consider using the `WORKDIR` instruction. 

#### As Parameters

Using this syntax, the parameters are sent to the default startup file in the base image. If multiple base images are specified, the startup file from the last specified image will be used.
