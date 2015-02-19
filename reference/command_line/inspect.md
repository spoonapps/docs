### inspect

The `inspect` command displays contents of the image.

```
inspect - Inspect changes to the image

Usage: spoon inspect <options> <image>

<options> available:
      --exclude=VALUE        Show details for all subsystems, except the
                               specified ones
      --format=VALUE         Use json format for output
      --include=VALUE        Show only details for selected subsystems:
                               dependencies, files, registry, services, startu-
                               p, dns, ports, env
```

#### Examples:

```
# Show all details about the image
> spoon inspect my-image

# Show filesystem changes only
> spoon inspect --include=files my-image

# Show all changes, but files and registry
> spoon inspect --exclude=files,registry my-image
```
