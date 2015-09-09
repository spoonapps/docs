## What is Spoon?

Spoon leverages [Turbo.net](http://turbo.net) Container technology to provide super fast sandboxes for developers and testers to spin up test environments.   

### Why use Spoon?

Spoon dramatically simplifies testing:

- Run development code in a pre-packaged, isolated environment with software-configurable networking
- Rapidly rollback changes and execute tests across a span of application versions and test environments
- Test in multiple client, server, and browser environments concurrently on a single physical device
- Accelerate test cycles by eliminating the need to install application dependencies and modify configuration

### FAQ

**Do Spoon containers work by running a full OS virtual machine?**

No. Spoon containers use a special, lightweight *application-level VM* called Spoon VM. Spoon VM runs in user mode on top of a single instance
of the base operating system.

**How long does it take to start Spoon sandboxes?**

Spoon sandboxes startup time is very fast -- on the order of seconds or less. (Startup time excludes any time required to download images.)

**What is the performance overhead of running inside a Spoon sandbox?**

The sandbox consumes only a small percentage of additional CPU and memory consumption relative to native applications. In nearly
all cases, Spoon overhead is negligible.

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

**What is the Spoon pricing model?**

See [Pricing and Plans](/pricing) for more information on Spoon plan options.
