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