## What is Spoonium?

Spoonium is a Windows containerization platform for developers and sysadmins to build, test, and deploy applications. Containerized ("Spooned") applications run exactly the same way no matter the underlying infrastructure - eliminating installs, conflicts, breaks, and dependencies.

#### Made for Developers

Packaging applications into containers with their dependencies ensures that those applications run as intended on any Windows environment. With Spoonium, developers can deploy any application to any machine without installers, incompatibilities, or breaks.

For example, an application built on the latest version of .NET may break if a tester or end user has a different .NET version installed. Instead of rolling the dice or hoping they can figure it out, pull the right .NET from Spoonium, package it into a container with your application, and send that container off. That's it! No more breaks.

Additionally, teams can send application containers back and forth in specific states for rapid debugging and iteration, eliminating friction between development and QA cycles. Tester finds a bug? Ship the container straight to the development team in its broken state for instant repro.

#### Made for QA

Any unit or code-level integration tests can be executed within a container, ensuring the environment used in production is properly tested against. Testers can pull a container down to their local machine and test against a local copy of the application; they can even run the Spooned application side-by-side against an older or beta version.

Spoonium effectively makes every environment clean, as application containers run isolated from the host machine. This eliminates the need to reimage test machines and allows for testing of multiple containers at once.

Find a bug? No need to have your development team reproduce it: just share the application container in its broken state so they can find a fix immediately.

For web applications and sites, Spoonium also offers unlimited manual and automated browser testing. Read more about our [Browser Sandbox](/docs/test#manual+browser+testing), our [online Selenium Grid](/docs/test#selenium+testing), and our easy integration with [any CI environment](/docs/build#continuous+integration).

#### Made for DevOps

By packaging applications and their dependencies into a container, sysadmins take away the inconsistencies between staging and production environments, allowing their teams to quickly and routinely ship to production.

Additionally, using Spoonium as a deployment standard massively simplifies getting software to end users. Instead of traditional installation with multiple points of failure, end users can run any Spooned application straight from their command prompt, or directly from the web in one click via the [Spoonium Hub](http://spoonium.net/hub) - even if they don't have the required dependencies.

#### Made for open source

Spoonium is 100% free for public projects. [Contact us](http://spoonium.net/contact) to get set up.