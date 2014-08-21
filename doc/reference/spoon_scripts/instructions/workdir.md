## WORKDIR

	WORKDIR <path>

The `WORKDIR` instruction sets the working directory inside the container. If a `WORKDIR` command is not specified (or a `-w` flag is not specified at the command line), all commands will be executed from the same working directory as the native command prompt. 

Unlike `CMD cd <path>`, the `WORKDIR` instruction will persist the working directory to all subsequent instructions. 