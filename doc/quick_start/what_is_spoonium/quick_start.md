## What is Spoonium?

Spoonium is a Windows containerization platform for developers and sysadmins to build, test, and deploy applications. Containerized ("Spooned") applications run exactly the same way no matter the underlying infrastructure - eliminating installs, conflicts, and dependencies.

#### Made for Developers

With Spoonium, developers can deploy any application to any machine without installers, incompatibilities, or breaks. Packaging applications into containers with their dependencies ensures that applications run as intended wherever they go.

#### Made for QA

By standardizing development and QA environments, containers make reproducing issues and patching bugs a cinch. Any unit or code-level integration tests can be executed within a container, ensuring the environment used in production is properly tested against. Manual testers can pull a container down to their local machine and test against a local copy of the application; they can even run the Spooned application side-by-side against an old version.

Beyond that, Spoonium commands have a variety of uses for QA. For example, `spoon revert` "turns back time" by reverting your container to a fresh image whenever you want to run a new test; you can even change the state of the app back to a specific point in time.

For web applications, Spoonium also offers unlimited manual and automated browser testing. Read more about our [Browser Sandbox](/docs/test#manual+browser+testing), our [online Selenium Grid](/docs/test#selenium+testing), and our easy integration with [any CI environment](/docs/build#continuous+integration).

#### Made for DevOps

By packaging applications and their dependencies into a container, sysadmins take away the inconsistencies between staging and production environments, allowing their teams to quickly and routinely ship to production.

Additionally, using Spoonium as a deployment standard massively simplifies getting software to end users. Instead of traditional installation with multiple points of failure, end users can run any Spooned application straight from their command prompt, or directly from the web in one click via the [Spoonium Hub](http://spoonium.net/hub) - even if they don't have the required dependencies.

#### Made for open source

Spoonium is 100% free for public projects. [Contact us](http://spoonium.net/contact) to get set up.