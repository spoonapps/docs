## What is Spoon?

Spoon allows you to package applications and their dependencies into a lightweight, isolated virtual environment called a "container." Containerized applications can then be run on any Windows machine that has Spoon installed, no matter the underlying infrastructure. This eliminates installs, conflicts, breaks, and missing dependencies.

Spoon containers are built on top of the Spoon Virtual Machine, an *application virtualization* engine that provides lightweight
namespace isolation of core operating system objects such as the filesystem, registry, process, networking, and threading subsystems.

### Why use Spoon?

Spoon dramatically simplifies and makes more reliable all phases of the software creation and deployment lifecycle:

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

And Spoon works seamlessly with [Turbo.net](http://turbo.net), an application hosting service that provides an application portal, desktop console, data synchronization, cloud storage, and more.

### How does it work?

Spoon containers are built on top of the **Spoon Virtual Machine Engine** (SVM), an application virtualization engine which provides lightweight implementation of core operating system APIs, including the filesystem, registry, process, networking, and threading subsystems. Applications executing within the Spoon virtual machine interact with a virtualized filesystem, registry, network, and process environment supplied by the SVM, rather than directly with the host device operating system. 

The image below illustrates how the SVM is isolated from the host environment.

![](/components/docs/getting_started/what_is_spoon/spoon-vm.png)

The Spoon VM is required to implement containerization on the Windows platform since the underlying OS does not provide appropriate containerization primitives. Put another way, Spoon VM plays the same role for Spoon containers as LXC does for Docker containers.

Unlike hardware virtualization systems like Microsoft Virtual PC and VMWare, or hypervisor systems such as Hyper-V, Spoon VM operates on top of the base operating on the execution stack and virtualizes specific operating system features required for application execution. This enables virtualized applications to operate efficiently, with the same performance characteristics as native executables.

There are several advantages in choosing Spoon containers over hardware virtualization systems:

- *Optimal performance:* Spoon containers run at the same speed as applications running natively against the host hardware, with a minimal memory footprint. In contrast, applications running within hardware-virtualized environments experience significant slow-downs and impose a large memory footprint due to the need to run multiple instances of a base operating system.

- *Dramatically reduced virtual environment size:* Spoon containers require a footprint proportional to the size of the virtualized application, data, and included components. As a result, Spoon containers are small enough to be quickly downloaded by end-users. Hardware virtualization requires an entire host operating system image, including many basic subsystems that are already present on the end-user device. Each virtual machine may occupy several gigabytes of storage.

- *Application density:* You can run multiple simultaneous Spoon environments per processor. Due to the high overhead of hardware virtualization, only a small number of hardware-virtualized environments per processor can run simultaneously.

- *Reduced licensing costs:* Spoon does not require the purchase of separate operating system licenses to use a container. Hardware virtualization systems require a host operating system in order to function, which can impose additional licensing costs and restrictions.

- *User mode implementation:* The Spoon application virtualization engine is implemented entirely in user mode and does not require administrative privileges. Note that applications requiring hardware device drivers or other non-user-mode software may require a hardware-virtualized environment to function properly.

### FAQ

**Do Spoon containers work by running a full OS virtual machine?**

No. Spoon containers use a special, lightweight *application-level VM* called Spoon VM. Spoon VM runs in user mode on top of a single instance
of the base operating system.

**How long does it take to start Spoon containers?**

Spoon container startup time is very fast -- on the order of seconds or less. (Startup time excludes any time required to download images.)

**What is the performance overhead of running inside a Spoon container?**

Containerized applications consume only a small percentage of additional CPU and memory consumption relative to native applications. In nearly
all cases, Spoon overhead is negligible.

**When I run a container with multiple base images, does it link multiple containers or make a single new container?**

Running with multiple base images creates a single container with all of the base images combined. However, this is implemented in an optimized way that avoids explicit copying of the base image container contents into the new container.

Spoon then stores deltas on top of the base images as the container state evolves. The `,` operator works left-to-right, so files or settings in later arguments override files or settings in previous arguments.

**Wow, that's amazing!**

Yes. Please enjoy responsibly.

**Does Spoon support virtual networking?**

Yes. See the `--route-add`, `--route-block`, `--link`, and `--hosts` commands.

**Does Spoon support linking multiple containers?**

Yes. See the `--link` command.

**Is there a difference between server and desktop application containers?**

No, there is no special distinction. And desktop containers can contain services/servers and vice versa.

**How does Spoon handle licensing?**

Spoon does not modify the licensing behavior of any applications running virtualized or within a container. Running on Spoon is identical
to running on a regular PC, or running on virtual hardware such as Virtual PC or VMware. And Spoon runs on a single instance of a base
operating system.

**Does Spoon provide a mechanism to track licenses?**

[Spoon Server](/server) includes a licensing module which will actively track and/or enforce licensing. For example, you can grant/deny privileges based on Active Directory or LDAP membership and define licensing constraints on a total user, total device, concurrent user, or concurrent device basis. Spoon Server also provides an analytics module that allows administrators to track application consumption and validate compliance
with licensing requirements.

**Where is the Spoon container hub?**

The public Spoon Hub is hosted at [http://spoon.net/hub](http://spoon.net/hub).

**What is the Spoon pricing model?**

Spoon.net is free to use for public repositories. Private repositories and other advanced features and tools are available in paid subscriptions.
See [Pricing and Plans](/pricing) for more information on Spoon plan options.

**What if I don't want to host my repositories hosted on Spoon.net?**

Spoon is available as an on-premises enterprise server. Please see **[Spoon Server](/server)** for more information or to request
an evaluation license.




