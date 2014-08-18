# Use Cases

## Binary Version Control

Spoonium can be used as a version control system for your entire application. Similar to how Git or Mercurial can be used as a VCS for your application's source code, Spoonium can be used as a VCS for your application, *itself*. 

## Testing and QA

Simplify **multi-step development cycles**. Ensure that the same code the developer writes is the same code the QA team tests and that the ops team deploys.

## Cross-Version Deployment

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

## Bundling Dependencies into An Application

Application dependencies, such as .NET, Java, or Flash can be packaged into an application container. The containerized application will then use *this* dependency -- eliminating the need for the end-user to have that dependency installed natively. 

Take, for example, a requirement for your .NET application to support Windows XP. Traditionally, if you wanted to write your app using the .NET 4.0 framework, you would need to require all of your users to have a native .NET 4.0 install. This would probably packaging the .NET 4.0 installer in with your app and *hoping* that the user didn't have an unorthodox configuration on her machine that would break the installer or your application. 

With Spoon, supporting this scenario is as easy as packaging a .NET 4.0 image (trusted build available through the **spoonbrew** user account) alongside a containerized version of your application. You can then deploy this *single binary* to all of your end-users.  