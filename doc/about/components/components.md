## Spoon VM

The backbone of Spoonium is the **Spoon Virtual Machine**. It's a lightweight implementation of core operating system APIs, including the filesystem, registry, process, and threading subsystems, within the Windows user-mode space. Applications executing within the Spoon VM interact with a virtualized filesystem, registry, and process environment, rather than the host machine.

The virtualization engine handles requests within the VM internally or routes requests to the host device filesystem and registry if appropriate. It performs these actions according to the virtual application configuration.

The Spoon VM supports merge, override, write-copy, and hide isolation modes between the virtual and host filesystem and registry. These settings are available for directories as well as individual files.

The virtualization engine dynamically remaps shell folder paths so that proper application behaviour is preserved across various client operating systems. Similarly, registry key values containing explicit path names or prefixes are dynamically remapped to the appropriate values for each host device. A generalized multi-platform virtualization layer dynamically adapts virtual machine behavior based on the endpoint platform.

In addition to desktop applications, the VM supports virtualization of system services such as web servers and local database engines, component object model (COM) servers, and network services such as DNS. The VM also supports advanced operating system features including kernel object namespace isolation and side-by-side (SxS) manifests.

The Spoon virtual microkernel has been optimized to produce negligible storage and runtime performance overhead. Spoon's local caching feature can be adjusted from zero to full local caching, even allowing large numbers of applications to be used from storage-constrained thin client devices.

## Containers

A container is an isolated virtual environment consisting of a filesystem, registry, and the Spoon VM.

Files, folders, and registry keys in a container are completely separate from the host system as well as other containers, allowing for multiple isolated user space instances on a single system.

More information on [working with containers](http://spoonium.net/docs/containers#buildingcontainers).

## Images

An image is a read-only filesystem and registry.

Images are building blocks for new containers. If a project needs MongoDB, then specify that image when starting a new container.

Containers can also be saved as images. Building block images like MongoDB merge with the altered container state and are saved as a new image.

More information on [working with images](http://spoonium.net/docs/containers#buildingimages).

## IDE and Command Line Interface

The IDE, previously known as **Spoon Studio**, allows developers and systems administrators to build Spoon images through a friendly graphical user interface. The IDE is most commonly used for it's "snapshot" method of containerization. Read more about IDE [here](http://spoonium.net/docs#IDE).

The command line interface (CLI) is a command line tool for creating containers and building images in real-time. The CLI also provides a suite of tools for managing containers and images.

**Developers** can use the CLI to containerize their entire developer stack into their application -- ensuring that the same product a developer sees is the one encountered by end-users.

**System administrators** can use the CLI to more effectively manage their infrastructure.

Read more about using the CLI [here](http://spoonium.net/docs/containers#commandline).

## Hub

The [Spoonium Hub](http://spoonium.net/hub) is a public, SaaS platform for hosting and distributing Spoon images. 

Hub **repositories** host images for a single project. For example, images for each version of .NET can be found in the [spoonbrew/dotNet](http://spoonium.net/hub/spoonbrew/dotNET) repository. A repository houses the entire version history of a project.

The hub can aid in end-user deployment as well as internal development. New application releases can be pushed to a public repository, where they can instantly be pulled and run by your end-users. 

Internal and pre-release builds can be held in private repositories only accessible by the members of your organization.

More information on [getting started with the hub](http://spoonium.net/docs/containers#basics) and [working with repositories](http://spoonium.net/docs/containers#repositories).

## Spoon Server

Spoonium supports deployment to both [public](http://spoonium.net/hub) and private hub servers.

We offer an on-premise solution called Spoon Server that allows your organization to host an internal hub. Any Windows machine can host this software and i                           t provides the same functionality as the Spoonium Hub, but hosted entirely on your organization's network.

For more information, contact our sales team at [sales@spoon.net](mailto:sales@spoon.net).