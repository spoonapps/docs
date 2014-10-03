### using

The `using` instruction adds an additional, temporary image(s) for that container.

```
using <image>
```

Multiple images can be specified in a single `from` instruction by separating each image with a comma or space. If the same file, registry entry, or environment variable exists in multiple images added via the `from` instruction, then the one from whichever image was specified last will win the conflict and be used in the virtual environment. If the same file, registry entry, or environment variable exists in two images, one added via the `using` instruction and one added via the `from` instruction, then the one in the `from` image will win the conflict. Virtual machine settings are taken from the last image specified in the `from` instruction.

Due to this "layering" approach, it is a good practice to specify images with newer versions of applications or libraries after images with older versions.

```
using <image 1> <image 2>

# Start container with git and node
from spoonbrew/git spoonbrew/node
```

**Note**: Images added with `using` keyword are **NOT** included in final image
