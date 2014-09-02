## What is Spoonium?

Spoonium is a tool that can package an application and its dependencies in a virtual container. Containerized ("Spooned") applications can then be run on any Windows machine that has Spoonium installed, no matter the underlying infrastructure. This eliminates installs, conflicts, breaks, and missing dependencies.

This has benefits for several groups of people:

#### Developers

With Spoonium, developers can:

- Develop and test Windows applications in containers that can be distributed to other developers, as well as to staging/production. The common issue of "Well, it worked on my machine" can be avoided.
- Deploy any application to any machine without installers, incompatibilities, or breaks.
- Send containers back and forth in specific testing stages, eliminating friction between development and QA cycles and speeding up the development life cycle.

**Example:** An application built on the latest version of .NET may break if a tester or end user has a different .NET version installed. To avoid this issue, use Spoonium to package your application *with* the right .NET version into a container that will run instantly on any device with the Spoonium plugin.

#### QA

With Spoonium, testers can:

- Execute any unit or code-level integration tests within a container, ensuring the environment used in production is properly tested against.
- Pull a container down to their local machine and test against a local copy of the application; they can even run the Spooned application side-by-side against an older or beta version.
- Speed up test cycles by removing the wait time usually needed to install operating systems and application dependencies.

For web applications and sites, Spoonium also offers unlimited manual and automated browser testing. Read more about our [Browser Sandbox](/docs/test#manual+browser+testing), our [online Selenium Grid](/docs/test#selenium+testing), and our easy integration with [any CI environment](/docs/build#continuous+integration).

**Example:** Instead of installing, uninstalling, and reinstalling various dependencies onto a test machine, simply pull and run your team's application container, with all dependencies included, from a Spoonium repository.

#### Sysadmins

With Spoonium, sysadmins can:

- Take away the inconsistencies between staging and production environments, allowing their teams to quickly and routinely ship to production.
- Deploy and run any app on any Windows infrastructure quickly and reliably, even if users don't have the traditionally required dependencies or environment.

#### Open source

Spoonium is 100% free for public projects. [Contact us](http://spoonium.net/contact) to get set up.

## How does it work?

Without going too deeply into specifics, Spoonium containers are built on the **Spoon Virtual Machine** (SVM), a lightweight implementation of core operating system APIs, including the filesystem, registry, process, and threading subsystems. Applications executing within a container interact with a virtualized filesystem, registry, and process environment supplied by the SVM, rather than directly with the host machine.

#### Images - Build component

Spoonium images serve as a read-only filesystem and registry that your application will use while running in a container. They contain all of the information on a certain type of container.

Verified images (like jdk, node, mongo)  are available for download from the [Spoonium Hub](http://spoonium.net/docs/about#hub), or a custom image can be created from any container with the `spoon commit` command. Thus, you can layer multiple dependency images together, rather than having to build one on top of another.

When instructed to run a container with the `spoon run` command, Spoonium will automatically download necessary images. Read more about [working with images](http://spoonium.net/docs/build#working-with-images).

#### Repositories - Distribution component

To share your public images and containers with others, we have the [Spoonium Hub](http://spoonium.net/hub), which is filled with public repositories from both Spoonium users and the [spoonbrew team](http://spoonium.net/hub/spoonbrew).

Free Spoonium accounts come with one free private repository and unlimited public repositories. You can also host your own on-premises repositories (instructions found [here](http://spoonium.net/docs/about#spoon-server)).

Once an image is on the Hub, you can run it from another location. Read more about the [Hub](http://spoonium.net/docs/about#hub).

#### Containers - Run component

Containers are created from an image or from multiple images. They hold everything needed for applications to run, and they can be run/started/stopped/removed, and more.

You can turn a container into a custom image template using the `spoon commit` command.

[Read more](http://spoonium.net/docs/about) about how Spoonium works.

