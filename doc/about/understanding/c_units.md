# The Units of Spoonium



## Images

An image is a read-only filesystem and registry. Images typically contain a single application or dependency. For example, the Java runtime would be packaged into a single image. Similarly, a custom application could be packaged and built into another image. Required dependencies can then be *merged* at runtime to create a single filesystem and registry that contains an application and its dependencies. 

Images are entirely stateless. That is, once created an image *cannot* be modified. To modify an image, one must create a new **container** from the image, make any required modifications, and `commit` the container. 

## Containers

Containers consist of a readable/**writable** file system and registry. Whenever an image is run, a new container is created. A container creates a new virtual filesystem and registry consisting of all the files in any of the "run" images. This filesystem can be read from *and* written to. 

Unlike images, containers are *dyanmic* and stateful. Along with a virtual filesystem and registry, a container hosts running processes. 

Each container runs in its own isolated environment, independently of any host processes or concurrently running containers. 

Containers only run for the lifetime of the processes they host. If all of the processes contained within a container are stopped or killed, the container shuts down. Containers can also be manually stopped, started, or deleted from the Spoon CLI. 

## Registries

A registry is a cache of images. On Spoonium, a registry can be *local* or *remote*. 

A local registry consists of any files stored locally on a computer. Executing `spoon images` will return a list of all the files in your local registry.

A remote registry is simply a cache of images on a server or remote location. An example of a remote registry is the [Spoonium Hub](http://spoonium.net/hub).  

On Spoon, images are stored in SpoonDB. 

## Repositories
