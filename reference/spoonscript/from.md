### from

The `from` instruction creates a new container and sets the base image(s) for that container. 

```
from <image>
```

The `from` instruction must be placed at the beginning of a `.me` file or omitted if a clean base image is desired.

Multiple images can be specified in a single `from` instruction by separating each image with a comma or space. If the same file, registry entry, or environment variable exists in multiple images added via the `from` instruction, then the one from whichever image was specified last will win the conflict and be used in the virtual environment. Virtual machine settings are taken from the last image specified in the `from` instruction.

Due to this "layering" approach, it is a good practice to specify images with newer versions of applications or libraries after images with older versions.

```
from <image 1> <image 2>

# Start container with git and node
from git/git node/node
```

**Note**: To initialize an empty container, use the `spoonbrew/clean` image

```
from spoonbrew/clean
```
