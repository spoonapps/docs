## cmd

The `cmd` instruction can be used either: 

1. As a command prompt: `cmd <command> <**args>`
2. Like an *exec*: `cmd ["executable", "param1", "param2"]`

#### As a Command Prompt

If the `cmd` instruction is used with the corresponding `<command>` and `<args>` having valid command prompt syntax, the command is executed in a fresh command prompt within the container. A new command prompt is spawned for each `cmd` instruction. Thus, any stateful commands (`cd`, for example), must be chained to other commands with an ampersand (`&`) to have their desired effect. 

This syntax is equivalent to executing `%COMSPEC% /c <command> <args>` in the container. 

**Example**: Say a user wants to view the contents of a file located at `C:\spoon\text-file.txt`. The following sequence of instructions would *not* work: 

	cmd cd C:\spoon
	cmd more text-file.txt

Instead, they would have to use the single instruction:

	cmd cd C:\spoon & more text-file.txt

Alternatively, the full path to `text-file.txt` could be specified:

	cmd more C:\spoon\text-file.txt

**Note**: If you wish to use `cd` functionality in your script, consider using the `WORKDIR` instruction. 

#### Like an Exec

If you wish to spawn a process from an executable, and optionally supply parameters to that executable, you must express the desired *exec* as a JSON array of strings and give the full path to the executable (unless it is on the local system or container's `PATH`). 