## workdir

	workdir <path>

The `workdir` instruction sets the working directory inside the container. If a `workdir` command is not specified (or a `-w` flag is not specified at the command line), all commands will be executed from the same working directory as the native command prompt. 

Unlike `cmd cd <path>`, the `workdir` instruction will persist the working directory to all subsequent instructions. 