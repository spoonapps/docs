### Create Applications

In this section you will learn how to create Spoon applications that can deploy from Spoon Server. Spoon applications are created from existing applications by converting them into **SVM** file format. For more information about adding an existing **SVM** file to Spoon Server, refer to Managing Applications.

#### Virtualize Application with Spoon Studio

To be hosted on Spoon Server applications must be converted into Spoon Virtual Applications (**SVM** files) using the Spoon Studio. The Spoon Studio monitors the installation of your application, analyzes the installation, and constructs a virtual package which you can upload to Spoon Server. Experienced users can convert most applications for Spoon in minutes.

To create an **SVM** using Spoon Studio, Project Type must be set to **Component**. Virtual applications with compressed payloads **cannot** be optimized for streaming using Spoon Server. To build a streaming virtual application, **Compress Payload** in Settings must remain unchecked during the build process.

Refer to the Spoon Studio help documentation for detailed instructions on how to create a Spoon application.