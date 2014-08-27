Spoonium supports deploying containers as standalone executables, MSIs and Spoon Virtual Machines (SVMs). Read this section to find out more about which deployment option and tools best fit your needs.

## With IDE

Enterprise customers and Spoon.net users that are deploying containers to end users should use the IDE to package and deploy applications. Once the build process is complete, see [Working with IDE](/docs/build#working+with+ide), the container can be deployed as an SVM, EXE or MSI. For more in depth information about the IDE see the [reference](/docs/reference) section.

#### SVM Output

An SVM, sometimes referred to as **Component** or **Layer**, is a Spoon Virtual Machine. The SVM houses the virtual filesystem and virtual registry and is the basic building block of a container. All Spoonium outputs are built on the SVM architecture. SVMs can be deployed directly to Spoon.net or a Spoon Server using the **Publish to Spoon.net** option on the ribbon menu.

SVMs are commonly used as components that can be combined together to build a more complex application runtime environment. For example, if you wanted to build a browser like Internet Explorer 8 and you wanted to add Java support to the application, you can include a Java component in the build. 

SVMs are also the building blocks of containers. When creating a container, each image that is pulled from a repository is an SVM file. For example, the following Spoon command will create a container composed of three SVMs.

```> spoon run spoonbrew/jdk;spoonbrew/node;spoonbrew/git```

This creates a container with Java, Node and Git support, each feature added to the container via an SVM file. 

#### EXE Output

Standalone executables are portable containers that can be deployed to any desktop. This is a popular deployment option for organizations that have an existing endpoint management solution like LANDesk Management Suite, Microsoft System Center Configuration Manager, or Novell ZENworks. To output an executable, set the **Project Type** to **Application**.  

#### MSI Output

MSI outputs simply wrap the portable container into an MSI package to add support for shell integration like file associations, Start Menu shortcuts and ProgIds. MSIs are a common deployment option for organizations that are using Admin Studio or for integrating with existing desktop management solutions. To build and MSI, go to the **Setup** section, enter the MSI details and click **Build MSI**.
 