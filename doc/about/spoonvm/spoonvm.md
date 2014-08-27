Spoonium is a platform for building, testing and deploying Windows applications and services in isolated containers. Once an application or service is put into a container, that image can be distributed to testers, Beta users or any Spoonium user by pushing the image to the Hub. This sections describes some of the building blocks of the Spoonium platform starting with the virtual machine.

## Virtual Machine

The runtime environment of Spoonium containers is supplied by the **Spoon Virtual Machine** or SVM, a lightweight implementation of core operating system APIs, including the filesystem, registry, process, and threading subsystems. Applications executing within the container interact with a virtualized filesystem, registry, and process environment supplied by the SVM, rather than the host machine.

The virtualization engine handles requests within the container internally or routes requests to the host device filesystem and registry if appropriate. It performs these actions according to the application configuration defined when creating the container, see the [Building](/docs/building) section.

In addition to the virtual filesystem and registry, the SVM supports virtualization of system services such as web servers and local database engines, component object model (COM) servers, and network services such as DNS. The SVM also supports advanced operating system features including kernel object namespace isolation and side-by-side (SxS) manifests.

The Spoon virtual microkernel, which is the engine of the SVM, has been optimized to produce negligible storage and runtime performance overhead. Applications running within a container will run with about the same performance characteristics as if it were running on the host system.