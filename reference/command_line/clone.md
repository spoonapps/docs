### clone

The `clone` command creates a copy of an existing container.

```
Usage: spoon clone  <existing container> [<new container name>]
```

#### Examples:

```
# Create an unnamed copy of a container
> spoon clone 28c

# Create a named copy of a container
> spoon clone test-container copy-of-test-container

```