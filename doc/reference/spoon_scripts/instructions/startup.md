### startup file

```
startup file <command> <params...>
startup file [<exec>, <params...>]
```

The startup file instruction is used to specify the startup file or script to run when a new container is created from this image (using `spoon run`). 

This instruction is only applied to the output image -- it does not affect the intermediate container. 

The startup file instruction will accept parameters as a space-delimited list or as a JSON-array of strings. 

If parameters are specified as a space-delimited list, the first parameter is the startup command and all subsequent parameters are parameters that will be passed to the startup command. When specified in this manner, commands are interpreted by the Windows shell. 

```
# hello world is passed to the 'echo' command
startup file echo hello world
```

If parameters are specified as a JSON-array of strings, the first item in the array is the startup executable and all subsequent items are passed as parameters to the startup executable.  When specified in this manner, parameters are passed directly to the startup executable. 

```
# "clone" and "https://github.com/spoonium/docs" are passed to git.exe
startup file ["git.exe", "clone", "https://github.com/spoonium/docs"]
```