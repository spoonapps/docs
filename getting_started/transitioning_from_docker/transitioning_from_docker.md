## Transitioning from Docker

*Docker* is a new containerization technology built on top of the `LXC` kernel containment system built into Linux. While there are some similarities
and between the Docker and Spoon virtualization platforms, there are also significant differences.

This section summarizes some of the substantial differences for the benefit of users familiar with Docker.

### Supported Platforms

Spoon was designed for the Windows platform and provides its own virtual machine implementation, *Spoon VM*. Docker was designed for use on
Linux environments and depends on operating system support to provide virtualization.

Spoon supports many Windows-specific constructs such as Windows Services, COM/DCOM components, WinSxS side-by-side versioning, shell
registration, and many other mechanisms that do not exist on Linux operating systems.

Spoon also provides a desktop client that provides many features (GUI launch tool, file extension associations, Start Menu integration)
that allow virtualized applications to interact with the user in the same way as traditionally installed desktop applications.

### Delivery Models

Spoon, like Docker, supports the use of local containers and the ability to push and pull containers from a central
repository.

In addition, Spoon provides the ability to efficiently *stream* containers over the Internet. The Spoon system includes
a *predictive streaming* engine that allows containers to be launched efficiently over wide area networks (WANs) without
requiring the endpoint to download the entire VM image. This is important since many applications can be multiple gigabytes
in size, causing a large startup latency for remote end users. Spoon predictive streaming uses statistical techniques to predict
application resource access patterns based on profiles of previous user interactions and dynamically adapts the stream
data flow based on predictions of subsequent required resources.

### Variable Isolation Modes

Spoon containers are *not* required to be completely isolated from the host device resources. Spoon can fully or partially isolate objects
depending on the application.

Spoon allows an *isolation mode* to be specified on a per-object basis. For example, directory or per-registry key basis. Objects
can be isolated Isolation modes include *full*, *merge*, and *write copy*.

For more information on isolation modes, please see the corresponding section in the Spoon documentation.

### Container Isolation Defaults

When a container is created, it is given a read-only view into the host device's file system and registry and any changes are written to the container's sandbox. This allows virtual applications to interact with the host device yet prevent any changes which could alter the system configuration. 

Isolation from the host device only applies to processes which are created from within the container. Existing applications or system services will not be isolated nor are their interactions with processes inside the container. For example, executing an MSI installer package will result in an application being installed to the host device as the MSI file is processed by a Windows system service. In this case, using Spoon IDE to **snapshot** the installation process is recommended.

### Default Networking Behavior

By default, all Spoon container ports are exposed on the host device network adapter as if the containerized application had
been executed natively. If desired, ports can be closed with a single command and then opened
or remapped on an individual basis. By contrast, Docker isolates all ports by default. In both cases, ports can be remapped
and containers linked to one another as desired.  
