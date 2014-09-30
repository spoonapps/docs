### workdir

The `workdir` instruction sets the working directory inside the container.

```
workdir <path>
```

If a workdir command is not specified then all commands will be executed from the same working directory as the native command prompt. 

Unlike `cmd cd <path>`, the `workdir` instruction will persist the working directory to all subsequent instructions. 

Last `workdir` instruction will also set working directory on output image. See `run` command for more details.