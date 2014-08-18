# Benefits

## Simplify Application Deployment

It's happened to us all – an application that was working on your development machine gets moved to another machine and suddenly breaks. With Spoonium, that issue is no more. Developers can containerize and share their development stack through Spoonium. When the application is ready for primetime, their entire environment can be containerized and deployed to a production machine.

## Easier Bug Tracking and QA

Any unit or code-level integration tests can be executed within a container, ensuring the same environment that will be used in production is properly tested against. When an application is ready for manual testing, a Spoonium container can be pushed to a remote hub where it can be shared with testers. Manual testers can pull the application down to their local machine and test against their local copy of the container. This ensures that testers see the same environment as the developer who will need to reproduce and patch any reported issues.

For **web applications**, Spoonium also offers unlimited manual and automated browser testing. Spoonium's Selenium service has containerized versions of all major browsers which are built to self-configure a Selenium Grid on any Windows computer. These same browsers are also available without Selenium Grid networking for manual testing. 

## Effectively Leverage Hardware

Containers can be spun up or down instantly through the Spoon CLI. Multiple server-database instances can run in parallel on the same computer. Spoon's port remapping will allow multiple server-datbase applications to bind to the same port on the same computer, allowing for load distribution across multiple servers without the need for multiple physical machines. 