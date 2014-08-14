# Syntax for `.me` Scripts

## Rules

1. `.me` scripts are line-delimited and must only contain 1 instruction per line. Line continuation is *not* supported. 
2. All lines must follow the general structure: `INSTRUCTION <**args>`
3. Inline comments are not supported. Comments must be applied at the beginning of a line and are applied to the entire line. 

## Instructions

#### FROM

	FROM <image>

**Equivalent command**: `spoon run <image>`

The `FROM` instruction creates a new container and sets the base image for that container to the image specified in the instruction. A valid `.me` file **MUST** start with a `FROM` instruction *and* can only contain a single `FROM` instruction. 

Multiple images can be specified in a single `FROM` instruction by putting a space between subsequent images. 

	FROM <image 1> <image 2>

For example, to start a container with `spoonbrew/git` and `spoonbrew/node` as base images, the `FROM` instruction would be: 

	FROM spoonbrew/git spoonbrew/node

**Note**: To initialize an empty container, use the `spoonbrew/scratch` image

	FROM spoonbrew/scratch

#### CMD

The `CMD` instruction can be used either: 

1. As a command prompt: `CMD <command> <**args>`
2. Like an *exec*: `CMD ["executable", "param1", "param2"]`

###### As a Command Prompt

**Equivalent command**: `%COMSPEC% /c <command> <**args>`

If the `CMD` instruction is used with the corresponding `<command>` and `<args>` having valid command prompt syntax, the command is executed in a fresh command prompt within the container. A new command prompt is spawned for each `CMD` instruction. Thus, any stateful commands (`cd`, for example), must be chained to other commands with an ampersand (`&`) to have their desired effect. 

**Example**: Say a user wants to view the contents of a file located at `C:\spoon\text-file.txt`. The following sequence of instructions would *not* work: 

	CMD cd C:\spoon
	CMD more text-file.txt

Instead, they would have to use the single instruction:

	CMD cd C:\spoon & more text-file.txt

Alternatively, the full path to `text-file.txt` could be specified:

	CMD more C:\spoon\text-file.txt

**Note**: If you wish to use `cd` functionality in your script, consider using the `WORKDIR` instruction. 

###### Like an Exec

If you wish to spawn a process from an executable, and optionally supply parameters to that executable, you must express the desired *exec* as a JSON array of strings and give the full path to the executable (unless it is on the local system or container's `PATH`). 

#### ENV

	ENV <name> <value>

**Equivalent command**: `set <name>=<value>`

The `ENV` instruction creates a new environment variable inside the working container. This environment variable will be persisted to the output image from the `build` command. 

Only one environment variable can be added per `ENV` instruction. To add multiple environment variables to the working container, use multiple `ENV` instructions. 

	ENV foo bar
	ENV var 5

#### WORKDIR

	WORKDIR <path>

**Equivalent command**: `cd <path>`

The `WORKDIR` instruction sets the working directory inside the container. If a `WORKDIR` command is not specified (or a `-w` flag is not specified at the command line), all commands will be executed from the same working directory as the native command prompt. 

Unlike `CMD cd <path>`, the `WORKDIR` instruction will persist the working directory to all subsequent instructions. 