
## What is Spoonium?

Spoonium is a container platform built on top of the Spoon virtual machine. Spoonium allows developers and systems administrators to isolate their applications from any underlying infrastructure, so that the same application runs the same way on any computer.

The Spoon virtualization machine, or Spoon VM, acts as a lightweight virtualization layer that sits between your application and the operating system. Applications run in a container interact with a virtual filesystem and registry, while the Spoon VM handles internal requests while selectively deferring certain commands to the underlying operating system. The Spoon VM also acts as a compatibility layer, allowing the same application to run the same way on any Windows NT 5.0+ OS.
Why Use Spoonium?

#### Write once, run anywhere.

1. **Simplify application deployment**

It's happened to us all – an application that was working on your development machine gets moved to another machine and suddenly breaks. With Spoonium, that issue is no more. Developers can containerize and share their development stack through Spoonium. When the application is ready for primetime, their entire environment can be containerized and deployed to a production machine.

2. **Easier bug tracking and QA**

Any unit or code-level integration tests can be executed within a container, ensuring the same environment that will be used in production is properly tested against. When an application is ready for manual testing, a Spoonium container can be pushed to a remote hub where it can be shared with testers. Manual testers can pull the application down to their local machine and test against their local copy of the container. This ensures that testers see the same environment as the developer who will need to reproduce and patch any reported issues.
For web applications, Spoonium also offers unlimited manual and automated browser testing. Spoonium's Selenium service has containerized versions of all major browsers which are built to self-configure a Selenium Grid on any Windows computer. These browsers are also available in their native, unaltered form at http://spoonium.net/manual for manual testing.

#### Popular Use Cases

- Spoonium can be used as a version control system for your entire application.
- Simplify **multi-step development cycles**. Ensure that the same code the developer writes is the same code the QA team tests and that the ops team deploys.
- **Isolate **your application from the underlying operating system.

