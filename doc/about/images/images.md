An image is a read-only filesystem and registry. Images typically contain a single application or dependency. For example, the Java runtime would be packaged into a single image. Similarly, a custom application could be packaged and built into another image. Required dependencies can then be *merged* at runtime to create a single filesystem and registry that contains an application and its dependencies. 

Images are entirely stateless. That is, once created an image cannot be modified. To effectively modify an image, one must create a new container from the image, make any required modifications, and `commit` the container as a new image. 

Images as saved containers

Images as building blocks for containers

More information on [working with images]().