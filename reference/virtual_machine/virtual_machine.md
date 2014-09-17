## Virtual Machine

**Layering**

The Spoon VM is capable of running multiple images in a single virtual machine instance(container) by layering the file system and registry of each image.

This allow's users to create modular components that can be reused by larger projects. 

In this section, the term layer is used interchagibly with image, since a layer within a container is always created by an image.

**Layering Scenarios**

Layering is used to support [Spoon IDE components](/docs/reference#ide-runtimes-and-components). It is also used when [dependencies](/docs/reference#dependencies) are created.

**Conflicts Between Layers**

In most scenarios, image layers will define unique resources that do not conflict with each other. However, it is possible for the layers to have conflicting resources and settings.

If multiple layers define different isolation modes for the same path, the first layer that defines the isolation mode will be used. 

For example, if the the "git" image defines a folder c:\git with full isolation, and "node" image includes the c:\git folder with merge isolation. 

The following command will create a container with the folder c:\git set to full isolation.

```
spoon run git,node
```

The following command will create a container with the folder c:\git set to merge isolation.

```
spoon run node,git
```