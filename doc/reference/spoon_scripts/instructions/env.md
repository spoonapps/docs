### env

The **env** instruction creates a new environment variable inside the working container. 

```
env <name>=<value>
```

This environment variable will be persisted to the output image from the **build** command. 

Only one environment variable can be added per **env** instruction. To add multiple environment variables to the working container, use multiple **env** instructions. Assignment of the PATH environment variable will appended to those on the host device.

```
env foo=bar
env path="c:\path to executables\"
```