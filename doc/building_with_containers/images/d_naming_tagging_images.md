# Naming and Tagging Images

## Forking

Images can be named using the `spoon fork` command. The `fork` will create a new link to the specified image with a new, given name.    

## Tagging

Images can be tagged with the `spoon tag` command. A tag in Spoon is roughly equivalent to a tag in Git -- that is, a tag refers to a specific point in the revision history of an image. It is most commonly used to denote major points (such as releases) in an image's lifetime. 

Images are tagged by specifying the image to tag, followed by the tag to be applied. For example, to tag the image `my-new-image` with the tag `1.0`, execute the command

	>spoon tag my-new-image 1.0