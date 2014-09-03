### tag

The `tag` command applies a new tag to an image or returns all the available tags for that image. 

```
Usage: spoon tag <image> [<tag>]
```

If a tag is specified then a new tag is applied to the image head. 

```
> spoon tag my-image 1.0
Output image: my-image:1.0
```

If no tag is specified then all the available tags are displayed.

```
> spoon tag my-image
All available tags of my-image:
head (local)
1.0 (local)
0.1.29
```