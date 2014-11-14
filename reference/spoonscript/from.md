### from

The `from` instruction creates a new container and sets the base image(s) for that container. 

```
from <image>
```

A valid `.me` file must start with a `from` instruction and may only contain one from instruction. 

Multiple images can be specified in a single `from` instruction by separating each image with a comma or space. If the same file, registry entry, or environment variable exists in multiple images added via the `from` instruction, then the one from whichever image was specified last will win the conflict and be used in the virtual environment. Virtual machine settings are taken from the last image specified in the `from` instruction.

Due to this "layering" approach, it is a good practice to specify images with newer versions of applications or libraries after images with older versions.

```
from <image 1> <image 2>

# Start container with git and node
from spoonbrew/git spoonbrew/node
```

**Note**: To initialize an empty container, use the `spoonbrew/clean` image

```
from spoonbrew/clean
```
