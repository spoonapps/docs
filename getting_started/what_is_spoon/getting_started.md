## What is Spoon?

Spoon allows you to package applications and their dependencies into a lightweight, isolated virtual environment called a "container." Containerized applications can then be run on any Windows machine that has Spoon installed, no matter the underlying infrastructure. This eliminates installs, conflicts, breaks, and missing dependencies.

Spoon containers are built on top of the Spoon Virtual Machine, an *application virtualization* engine that provides lightweight
namespace isolation of core operating system objects such as the filesystem, registry, process, networking, and threading subsystems.

### Why use Spoon?

Spoon dramatically simplifies and makes more reliable all phases of the software creation and deployment lifecycle:

- Run development code in a pre-packaged, isolated environment with software-configurable networking
- Rapidly rollback changes and execute tests across a span of application versions and test environments
- Test in multiple client, server, and browser environments concurrently on a single physical device
- Accelerate test cycles by eliminating the need to install application dependencies and modify configuration

In addition to container functionality, Spoon offers a number of premium test services, such as manual and automated browser testing, Selenium testing, and CI integration. For more information, see [Testing](/docs/testing).

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

Yes. See the `--route-add`, `--route-block`, `--link`, `--hosts`, and `--network` commands.

**Does Spoon support linking multiple containers?**

Yes. See the `--link` and `--network` commands.

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


