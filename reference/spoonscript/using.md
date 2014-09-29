### using

The `using` instruction adds an additional, temporary image(s) for that container.

```
using <image>
```

Multiple images can be specified in a single `using` instruction by putting a space between subsequent images. If a file can be found both in image added by `using` and by `from` then file from `from` image is used. If a file can be found in two images added by `using` then file from last image is used.

```
using <image 1> <image 2>

# Start container with git and node
from spoonbrew/git spoonbrew/node
```

**Note**: Images added with `using` keyword are **NOT** included in final image
