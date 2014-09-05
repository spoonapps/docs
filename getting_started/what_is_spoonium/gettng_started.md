## What is Spoonium?

Spoonium allows you to package applications and their dependencies into a lightweight, isolated virtual environment called a "container." Containerized ("Spooned") applications can then be run on any Windows machine that has Spoonium installed, no matter the underlying infrastructure. This eliminates installs, conflicts, breaks, and missing dependencies.

#### For Developers

With Spoonium, developers can:

- Develop and package applications in isolated containers that contain all dependencies, including runtimes such as .NET and Java, and databases such as SQL Server and MongoDB
- Automate testing and share test environments with QA, developers, and beta users with the [Spoonium Hub](http://spoonium.net/hub)
- Simplify development and eliminate bugs by deploying applications in a "known good" configuration with a fixed set of components and dependencies
- Containers obviate the need for installers and prevent conflicts with natively installed software

#### For QA

With Spoonium, testers can:

- Run development code in a pre-packaged, isolated environment with software-configurable networking
- Rapidly rollback changes and execute tests across a span of application versions and test environments
- Test in multiple client, server, and browser environments concurrently on a single physical device
- Accelerate test cycles by eliminating the need to install application dependencies and modify configuration

In addition to container functionality, Spoonium offers a number of premium test services, such as manual and automated browser testing, Selenium testing, and CI integration. For more information, see [Testing](http://spoonium.net/docs/testing).

#### For IT Managers

With Spoonium, system administrators can:

- Remove errors due to inconsistencies between staging, production, and end-user environments
- Allow users to test out new or beta versions of applications without interfering with existing versions
- Simplify deployment of desktop applications by eliminating dependencies (.NET, Java, Flash) and conflicts
- Improve security by locking down desktop and server environments while preserving application access

And Spoonium works seamlessly with [Spoon.net](http://spoon.net), an application hosting service that provides an application portal, desktop console, data synchronization, cloud storage, and more.

#### Open Source

Spoonium is 100% free for open source projects. Set up a free organization at Spoonium.net and [contact us](http://spoonium.net/contact) if you need help or access to premium features.

## How does it work?

Spoonium containers are built on the **Spoon Virtual Machine** (SVM), a lightweight implementation of core operating system APIs, including the filesystem, registry, process, and threading subsystems. Applications executing within a container interact with a virtualized filesystem, registry, and process environment supplied by the SVM, rather than directly with the host machine. There are three main components to Spoonium:

#### Images - Build component

Spoonium images serve as a read-only filesystem and registry that your application will use while running in a container. They contain all of the information on a certain type of container.

Verified images (like jdk, node, mongo)  are available for download from the [Spoonium Hub](http://spoonium.net/hub), or a custom image can be created from any container with the `spoon commit` command. Thus, you can layer multiple dependency images together in a single container, rather than having to build one on top of another.

When instructed to run a container with the `spoon run` command, Spoonium will automatically search for and download necessary images. Read more about [working with images](http://spoonium.net/docs/building#working-with-images).

#### Repositories - Distribution component

To share your public images and containers with others, we have the [Spoonium Hub](http://spoonium.net/hub), which is filled with public repositories from both Spoonium users and the [spoonbrew team](http://spoonium.net/hub/spoonbrew).

Free Spoonium accounts come with unlimited public repositories. You can also upgrade to a [paid plan](http://spoonium.net/pricing) with private repositories, or host your own on-premises repositories (instructions found [here](http://spoonium.net/docs/deploying#to-a-spoon-server)).

Once an image is on the Hub, you can run it from another location. Read more about [repositories](http://spoonium.net/docs/hub#repositories).

#### Containers - Run component

Containers are created from an image or from multiple images. They hold everything needed for applications to run, and they can be run/started/stopped/removed, and more.

You can turn any container into a custom image template using the `spoon commit` command.

Read more about [working with containers](http://spoonium.net/docs/building#working-with-containers) and about [how Spoonium works](http://spoonium.net/docs/getting+started#about), or jump right in with our "Hello World!" tutorial below.