## What is Spoonium?

Spoonium is a container platform built on top of the Spoon virtual machine. Spoonium allows developers and systems administrators to isolate their applications from any underlying infrastructure, so that the same application runs the same way on any computer.

The Spoon virtualization machine, or Spoon VM, acts as a lightweight virtualization layer that sits between your application and the operating system. Applications run in a container interact with a virtual filesystem and registry, while the Spoon VM handles internal requests while selectively deferring certain commands to the underlying operating system. The Spoon VM also acts as a compatibility layer, allowing the same application to run the same way on any Windows NT 5.0+ OS.
Why Use Spoonium?

## Benefits

#### Simplify Application Deployment

It's happened to us all – an application that was working on your development machine gets moved to another machine and suddenly breaks. With Spoonium, that issue is no more. Developers can containerize and share their development stack through Spoonium. When the application is ready for primetime, their entire environment can be containerized and deployed to a production machine.

#### Easier Bug Tracking and QA

Any unit or code-level integration tests can be executed within a container, ensuring the same environment that will be used in production is properly tested against. When an application is ready for manual testing, a Spoonium container can be pushed to a remote hub where it can be shared with testers. Manual testers can pull the application down to their local machine and test against their local copy of the container. This ensures that testers see the same environment as the developer who will need to reproduce and patch any reported issues.

For **web applications**, Spoonium also offers unlimited manual and automated browser testing. Spoonium's Selenium service has containerized versions of all major browsers which are built to self-configure a Selenium Grid on any Windows computer. These same browsers are also available without Selenium Grid networking for manual testing. 

#### Effectively Leverage Hardware

Containers can be spun up or down instantly through the Spoon CLI. Multiple server-database instances can run in parallel on the same computer. Spoon's port remapping will allow multiple server-datbase applications to bind to the same port on the same computer, allowing for load distribution across multiple servers without the need for multiple physical machines. 

## Use Cases

**Binary Version Control**

Spoonium can be used as a version control system for your entire application. Similar to how Git or Mercurial can be used as a VCS for your application's source code, Spoonium can be used as a VCS for your application, *itself*. 

**Testing and QA**

Simplify **multi-step development cycles**. Ensure that the same code the developer writes is the same code the QA team tests and that the ops team deploys.

**Cross-Version Deployment**

Spoon containers **isolate **your application from the underlying operating system. This means that a containerized application can run on any of the platforms supported by the Spoon VM. The Spoon VM also boasts a *compatibility layer* that ensures the same application executes in the same fashion on any platform. Bottom line: you can support any Windows operating system without making any changes to your code. 

Currently, the supported platforms are:

- Microsoft Windows 8.1
- Microsoft Windows 8
- Microsoft Windows Server 2012
- Microsoft Windows 7
- Microsoft Windows Server 2008, all editions
- Microsoft Windows Server 2003, all editions
- Microsoft Windows Vista, all editions
- Microsoft Windows XP Professional
- Microsoft Windows Embedded XP
- Microsoft Windows 2000 Professional
- Microsoft Windows 2000 Server

Both 32 (x86) and 64-bit architectures are supported.

**Bundling Dependencies into An Application**

Application dependencies, such as .NET, Java, or Flash can be packaged into an application container. The containerized application will then use *this* dependency -- eliminating the need for the end-user to have that dependency installed natively. 

Take, for example, a requirement for your .NET application to support Windows XP. Traditionally, if you wanted to write your app using the .NET 4.0 framework, you would need to require all of your users to have a native .NET 4.0 install. This would probably packaging the .NET 4.0 installer in with your app and *hoping* that the user didn't have an unorthodox configuration on her machine that would break the installer or your application. 

With Spoon, supporting this scenario is as easy as packaging a .NET 4.0 image (trusted build available through the **spoonbrew** user account) alongside a containerized version of your application. You can then deploy this *single binary* to all of your end-users.  