# Working with Images

Images serve as read-only foundations for containers to run "on top of" -- providing a base filesystem and registry that the container can access. They also serve to memorialize the state of an application at a certain point in time. 

Whereas a container is dynamic and can host running processes, an image is static. An image is, essentially, a snapshot of of a container at a specific point in time. 

## The Local Registry

The local registry is the cache of images on the local machine. When you first download and install the Spoon Plugin, the registry only contains a single image. Images can only be added to the registry through the `pull` or `import` commands. 

## Viewing Images

To get a list of all the images in the local registry, execute the `spoon images` command. This command generates a table listing all of the images in the user's local registry. 



