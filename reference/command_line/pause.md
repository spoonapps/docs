### pause

The `pause` command is used to pause a running container. 

```
Usage: spoon pause <container>

<options> available:
     --format=VALUE         Use json format for output
```

This will pause all processes and threads within the specified container. 

# JSON output

When `--format=json` option was passed this command will provide output in JSON format. It will contain `container` object with information about paused container or an `error` object if command failed.