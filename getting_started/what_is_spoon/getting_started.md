## What is Spoon?

Spoon allows you to package applications and their dependencies into a lightweight, isolated virtual environment called a "container." Containerized ("Spooned") applications can then be run on any Windows machine that has Spoon installed, no matter the underlying infrastructure. This eliminates installs, conflicts, breaks, and missing dependencies.

#### For Developers

With Spoon, developers can:

- Develop and package applications in isolated containers that contain all dependencies, including runtimes such as .NET and Java, and databases such as SQL Server and MongoDB
- Automate testing and share test environments with QA, developers, and beta users with the [Spoon Hub](/hub)
- Simplify development and eliminate bugs by deploying applications in a "known good" configuration with a fixed set of components and dependencies
- Containers obviate the need for installers and prevent conflicts with natively installed software

#### For QA

With Spoon, testers can:

- Run development code in a pre-packaged, isolated environment with software-configurable networking
- Rapidly rollback changes and execute tests across a span of application versions and test environments
- Test in multiple client, server, and browser environments concurrently on a single physical device
- Accelerate test cycles by eliminating the need to install application dependencies and modify configuration

In addition to container functionality, Spoon offers a number of premium test services, such as manual and automated browser testing, Selenium testing, and CI integration. For more information, see [Testing](/docs/testing).

#### For IT Managers

With Spoon, system administrators can:

- Remove errors due to inconsistencies between staging, production, and end-user environments
- Allow users to test out new or beta versions of applications without interfering with existing versions
- Simplify deployment of desktop applications by eliminating dependencies (.NET, Java, Flash) and conflicts
- Improve security by locking down desktop and server environments while preserving application access

And Spoon works seamlessly with [Spoon.net](http://spoon.net), an application hosting service that provides an application portal, desktop console, data synchronization, cloud storage, and more.

#### Open Source

Spoon is 100% free for open source projects. Set up a free organization at Spoon.net and [contact us](/contact) if you need help or access to premium features.

## How does it work?

Spoon containers are built on the **Spoon Application Virtualization Engine** (SVM), a lightweight implementation of core operating system APIs, including the filesystem, registry, process, and threading subsystems. Applications executing within a container interact with a virtualized filesystem, registry, and process environment supplied by the SVM, rather than directly with the host machine. 

### How is Spoon different from hardware virtualization?

Unlike hardware virtualization systems like Microsoft Virtual PC and VMware, Spoon virtualizes only the operating system features required for application execution. This enables virtualized applications to operate efficiently, with the same performance characteristics as native executables.

There are several advantages in choosing Spoon containers over hardware virtualization systems:

- Optimal performance. Spoon containers run at the same speed as applications running natively against the host hardware, with a minimal memory footprint. In contrast, applications running within hardware-virtualized environments experience significant slow-downs and impose a large memory footprint.

- Dramatically reduced application size. Spoon containers require a footprint proportional to the size of the virtualized application, data, and included components. As a result, Spoon containers are small enough to be quickly downloaded by end-users. Hardware virtualization requires an entire host operating system image, including many basic subsystems that are already present on the end-user device. Each virtual machine may occupy several gigabytes of storage.

- Multiple virtual applications capability. You can run multiple simultaneous Spoon containers per processor. Due to the high overhead of hardware virtualization, only a small number of hardware-virtualized environments per processor can run simultaneously.

- Reduced licensing costs. Spoon does not require the purchase of separate operating system licenses to use a container. Hardware virtualization systems require a host operating system in order to function, which can impose additional licensing costs and restrictions.

- Kernel mode. The Spoon Application Virtualization Engine only virtualizes user-mode operating system features, whereas hardware virtualization systems emulate the entire OS stack, including kernel mode components. Applications requiring device drivers or other non-user-mode software may require a hardware-virtualized environment to function properly.

### The three main components of Spoon

#### Images - Build component

Spoon images serve as a read-only filesystem and registry that your application will use while running in a container. They contain all of the information on a certain type of container.

Verified images (like jdk, node, mongo)  are available for download from the [Spoon Hub](/hub), or a custom image can be created from any container with the `spoon commit` command. Thus, you can layer multiple dependency images together in a single container, rather than having to build one on top of another.

When instructed to run a container with the `spoon run` command, Spoon will automatically search for and download necessary images. Read more about [working with images](/docs/building/working-with-images).

#### Repositories - Distribution component

To share your public images and containers with others, we have the [Spoon Hub](/hub), which is filled with public repositories from both Spoon users and the [spoonbrew team](/hub/spoonbrew).

Free Spoon accounts come with unlimited public repositories. You can also upgrade to a [paid plan](/pricing) with private repositories, or host your own on-premises repositories (instructions found [here](/docs/deploying/to-a-spoon-server)).

Once an image is on the Hub, you can run it from another location. Read more about [repositories](/docs/hub/repositories).

#### Containers - Run component

Containers are created from an image or from multiple images. They hold everything needed for applications to run, and they can be run/started/stopped/removed, and more.

You can turn any container into a custom image template using the `spoon commit` command.

Read more about [working with containers](/docs/building/working-with-containers) and about [how Spoon works](/docs/getting-started/about), or jump right in with our "Hello World!" tutorial below.
