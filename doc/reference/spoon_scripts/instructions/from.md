### from

```
from <image>
```

The from instruction creates a new container and sets the base image(s) for that container. A valid **.me** file must start with a from instruction and may only contain one from instruction. 

Multiple images can be specified in a single from instruction by putting a space between subsequent images. 

```
from <image 1> <image 2>

# Start container with git and node
from spoonbrew/git spoonbrew/node
```

**Note**: To initialize an empty container, use the `spoonbrew/scratch` image

```
from spoonbrew/scratch
```