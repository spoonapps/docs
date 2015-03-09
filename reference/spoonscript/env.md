### env

The `env` instruction creates a new environment variable inside the working container. 

```
env <name>=<value>
```

This environment variable will be persisted to the output image from the `build` command. 

Only one environment variable can be added per `env` instruction. To add multiple environment variables to the working container, use multiple `env` instructions. Well known system paths like `C:\Windows\System32` will be replaced by a variable that will be converted at runtime to the appropriate path for the execution environment.

When multiple environment variables with the same name are defined in set of images used to run a container, the value from last image is used. For two environment variables, PATH and PATHEXT, special behavior is defined. All values are concatenated together using the semicolon as the joining character. The value from the last image appears first and the host value is at the end.

```
env foo=bar
env path="c:\path to executables\"
```

In container these variables will have the following values:

```
foo=bar
path=c:\path to executables;C:\WINDOWS\system32;C:\WINDOWS
```

One environment variable can be set multiple times inside SpoonScript if `cmd` commands should have different environments. For each environment variable value from last `env` command is stored in final image. It is also possible to remove environment variable from final image with following syntax:

```
env foo=
```

Please note that if variable `foo` is also defined in one of `from` images and final image is created with `--no-base` flag then it will be still loaded into containers created with it.

Environment variables can be overridden in a container by explicitly setting the variable to a new value or when an application or installer sets a new value.
