### env

The `env` instruction creates a new environment variable inside the working container. 

```
env <name>=<value>
```

This environment variable will be persisted to the output image from the `build` command. 

Only one environment variable can be added per `env` instruction. To add multiple environment variables to the working container, use multiple `env` instructions.

When multiple environment variables with the same name are defined in set of images used to run a container then the value from last image is used. For two environment variables: PATH and PATHEXT special behavior is defined. All defininions are concatenated with themselves and with host value using semicolon as joinining character. Host value appears last and value from last image appears in front.

```
env foo=bar
env path="c:\path to executables\"
```

In container these variables with have following values:

```
foo=bar
path=c:\path to executables;C:\WINDOWS\system32;C:\WINDOWS
```

Environment variable can be overriden in image or container when an application (e.g. installer or `setx`) stores new value in registry.