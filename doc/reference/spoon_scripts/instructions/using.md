### using

The `using` instruction adds an additional, temporary image(s) for that container.

```
using <image>
```

Multiple images can be specified in a single `using` instruction by putting a space between subsequent images. 

```
using <image 1> <image 2>

# Start container with git and node
from spoonbrew/git spoonbrew/node
```

**Note**: Images added with `using` keyword are **NOT** included in final image
