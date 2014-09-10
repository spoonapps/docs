## Transitioning from Docker

*Docker* is a new containerization technology built on top of the `LXC` kernel containment system built into Linux. While there are some similarities
and between the Docker and Spoon virtualization platforms, there are also significant differences.

This section summarizes some of the substantial differences for the benefit of users familiar with Docker.

### Supported Platforms

Spoon was designed for the Windows platform and provides its own **Spoon VM** virtual machine implementation. Docker was designed for use on
Linux environments and depends on operating system support to provide virtualization.

Spoon supports many Windows-specific constructs such as Windows Services, COM/DCOM components, WinSxS side-by-side versioning, shell
registration, and many other mechanisms that do not exist on Linux operating systems.

Spoon also provides a desktop client that provides many features (GUI launch tool, file extension associations, Start Menu integration)
that allow virtualized applications to interact with the user in the same way as traditionally installed desktop applications; and
a browser plugin that allows containerized applications to be launched and streamed directly from a web browser.

### Layering

Spoon containers are designed to operate in a *layered* virtual machine architecture. Layers can be thought of as "transparent sheets"
of virtual environment configuration that can be dynamically stacked on top of one another to build many distinct configurations out of
discrete components. For example, to build a container for a Java application that uses a MongoDB database, one could combine a
Java runtime layer with a MongoDB database layer, and stack the application code and content in an application layer on top
of its dependency layers. Layers make it extremely easy to re-use shared components such as runtimes, databases, and plugins.

Layers can also be used to apply application configuration information. For example, one might have a layer that specifies the
default home page, favorites, and security settings on a browser. This can be applied on top of a base browser layer to impose those
settings onto a non-customized browser environment. Layers can be applied dynamically and programmatically, so it is even possible
to user layering to present distinct application configurations to distinct groups of users without rebuilding the base application
container. Continuing the browser example, one might have a base browser layer plus one configuration layer for the development team
and a different configuration layer for the sales team.

Layering can be used in the `spoon.me` automated build script to build containers on top of *multiple* base images. For example,
in SpoonScript the following is valid:

    from java, mongodb, redis

By contrast, Docker does not support creation of images from multiple base images. In other words, Spoon supports "multiple
inheritance" through source layering, and "polymorphism" through post-layering.

Spoon layering also enables *partial rollback* during container builds via the `using` command. This is especially useful
when an external tool is required during the build process but is not desired in the ultimate container. For example,

    using git
	  // pull in stuff using git
	
	// use the stuff to complete container setup

In this code, the contents of the `git` container will *not* be present in the output container. By contrast, Docker does
not distinguish between content that is imported for use only during the build process and content required by the
application container at runtime.

### Delivery Modes

Spoon, like Docker, supports the use of local containers and the ability to push and pull containers from a central
repository.

In addition, Spoon provides the ability to efficiently *stream* containers over the Internet. The Spoon system includes
a *predictive streaming* engine that allows containers to be launched efficiently over wide area networks (WANs) without
requiring the endpoint to download the entire VM image. This is important since many applications can be multiple gigabytes
in size, causing a large startup latency for remote end users. Spoon predictive streaming uses statistical techniques to predict
application resource access patterns based on profiles of previous user interactions and dynamically adapts the stream
data flow based on predictions of subsequent required resources.

Spoon provides a fully hosted application hosting service at [Spoon.net](http://spoon.net). [Spoon.net](http://spoon.net)
hosts application streams, provides application and user portals, automatically synchronizes user and application state to the
cloud, and provides file synchronization and shared folders. For more information, visit the [Spoon.net](http://spoon.net)
home page.

Spoon.net is also available as an on-premises [Spoon Server](http://spoon.net/server). Spoon Server provides the same
functionality as Spoon.net in a behind-firewall environment as well as additional enterprise features such as Active
Directory integration.

Spoon technology is integrated into select third-party enterprise application delivery platforms, including [Novell ZENworks
Suite](https://www.novell.com/products/zenworks/zenworks-suite/), [Novell ZENworks Application Virtualization](http://novell.com/zav),
and [LANDesk Management Suite](http://landesk.com).

### Variable Isolation

Unlike Docker, Spoon containers are *not* required to be completely isolated from the host device resources. Spoon can fully or
partially isolate objects as needed at a fine granularity.

A Spoon **isolation mode** may be specified on a per-object basis. For example, it is possible to specify that one directory
subtree should be fully isolated while another one is visible from the host device. Supported isolation modes include *full*,
*merge*, and *write copy*.

When a container is created, by default it is given a read-only view into the host device's file system and registry but any
changes are isolated and written instead to the container's sandbox. This allows virtual applications to consume host device
data and services yet prevent any changes which would alter the system configuration. 

Isolation from the host device only applies to processes that are created within the container. Existing applications or
system services will not be isolated, nor are their interactions with processes inside the container. For example, executing an
MSI installer package will result in an application being installed to the host device since the installation is
executed by a Windows system service. For this reason, we recommend use of a pre-existing package or the *snapshot* method
to install MSIs.

For more information on isolation modes, please see the Isolation Modes section of the Spoon documentation.

### Networking

By default, all Spoon container ports are exposed on the host device network adapter as if the containerized application had
been executed natively. If desired, ports can be closed with a single command and then opened
or remapped on an individual basis. Like Docker, Spoon supports mapping of TCP, UDP, and DNS, and container-level
remapping and IPC linking.

However, it is important to note that Docker *isolates* all ports by default. In Spoon, a server container will work
by default on the host device (ports open) and requires a separate command to close or relink the ports, which may be
desired for example to minimize the network surface area in production environments.

### Static Configuration

In addition to dynamic configuration via a console or script, Spoon also supports configuration via a static XML-based
specification that declares the files and other virtual machine state to be presented to the container. This 

To assist in building static configurations, Spoon inclues a graphical **Spoon IDE** interface and both graphical-
and command line-based *snapshot*-based configuration.

For more information on the Spoon IDE and snapshot tools, see the appropriate sections in the documentation.
