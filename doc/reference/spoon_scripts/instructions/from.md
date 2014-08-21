## FROM

	FROM <image>

**Equivalent command**: `spoon run <image>`

The `FROM` instruction creates a new container and sets the base image for that container to the image specified in the instruction. A valid `.me` file **MUST** start with a `FROM` instruction *and* can only contain a single `FROM` instruction. 

Multiple images can be specified in a single `FROM` instruction by putting a space between subsequent images. 

	FROM <image 1> <image 2>

For example, to start a container with `spoonbrew/git` and `spoonbrew/node` as base images, the `FROM` instruction would be: 

	FROM spoonbrew/git spoonbrew/node

**Note**: To initialize an empty container, use the `spoonbrew/scratch` image

	FROM spoonbrew/scratch