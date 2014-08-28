## What is Spoonium?

Spoonium is a Windows containerization platform for developers and sysadmins to build, test, and deploy applications. Containerized ("Spooned") applications run exactly the same way no matter the underlying infrastructure - eliminating installs, conflicts, breaks, and dependencies.

#### Made for Developers

With Spoonium, developers can deploy any application to any machine without installers, incompatibilities, or breaks. Packaging applications into containers with their dependencies ensures that those applications run as intended wherever they go.

Containers also eliminate friction between development and QA cycles, as teams can send application containers back and forth in specific states for rapid debugging and iteration. No more wasting time reproducing an issue; just have your QA team send you the application container in its current state.

#### Made for QA

Any unit or code-level integration tests can be executed within a container, ensuring the environment used in production is properly tested against. Testers can pull a container down to their local machine and test against a local copy of the application; they can even run the Spooned application side-by-side against an older or beta version.

Spoonium effectively makes every environment clean, as application containers run isolated from the host machine. This eliminates the need to reimage machines in between tests and allows for rapid testing of multiple containers at once.

Find a bug? No need to have your development team reproduce it: just share the application container in its broken state.

For web applications, Spoonium also offers unlimited manual and automated browser testing. Read more about our [Browser Sandbox](/docs/test#manual+browser+testing), our [online Selenium Grid](/docs/test#selenium+testing), and our easy integration with [any CI environment](/docs/build#continuous+integration).

#### Made for DevOps

By packaging applications and their dependencies into a container, sysadmins take away the inconsistencies between staging and production environments, allowing their teams to quickly and routinely ship to production.

Additionally, using Spoonium as a deployment standard massively simplifies getting software to end users. Instead of traditional installation with multiple points of failure, end users can run any Spooned application straight from their command prompt, or directly from the web in one click via the [Spoonium Hub](http://spoonium.net/hub) - even if they don't have the required dependencies.

#### Made for open source

Spoonium is 100% free for public projects. [Contact us](http://spoonium.net/contact) to get set up.