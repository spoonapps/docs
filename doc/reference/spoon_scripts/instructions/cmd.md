### cmd

The cmd instruction can be used either: 

1. As a command prompt: `cmd <command> <**args>`
2. Like an *exec*: `cmd ["executable", "param1", "param2"]`

#### As a Command Prompt

Using this syntax, each command is executed in its own command prompt -- a new command prompt being spawned for each instruction. Thus, any stateful commands (`cd`, for example), must be chained to other commands with an ampersand to have their desired effect. 

For example, to read a file in the **C:\Spoon** directory: 

```
# does not work
cmd cd C:\spoon
cmd more text-file.txt

# work!
cmd cd C:\spoon & more text-file.txt
```

**Note**: If you wish to use `cd` functionality in your script, consider using the `WORKDIR` instruction. 

#### Like an Exec

If you wish to spawn a process from an executable, and optionally supply parameters to that executable, you must express the desired *exec* as a JSON array of strings and give the full path to the executable (unless it is on the local system or container's `PATH`). Using this syntax, parameters are passed directly to the executable. 