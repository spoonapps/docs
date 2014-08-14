# Deploy Virtual Applications #

This section describes methods for deploying applications built in Spoon IDE.

## Deploy Using Spoon Server ##
Spoon Server enables you to launch your applications instantly from websites, portals and client desktops. A typical Spoon Server setup consists of an Administration site (where the server is managed) and a Portal site (where virtual applications are hosted and streamed). Virtual applications are uploaded through the Spoon Server Administration site, and are then available on the Portal site. Applications can be launched from the Portal site with a single-click from within the web browser using the Spoon Plugin, a small browser extension. In addition to simple web-based distribution, Spoon's unique delivery technology enables most applications to launch five to twenty times faster than a traditional download.

For more information on deploying applications using Spoon Server, refer to the Spoon Server User Guide. Visit [http://Spoon.net/Server](http://Spoon.net/Server) for details on Spoon Server pricing and licensing.

### Spoon Delivery Technology ###

Spoon uses machine learning technology to automatically break down complex applications into smaller functional data units. Spoon does not require streaming servers or specialized protocols, and works with no infrastructure changes.

Spoon automatically identifies a *prefetch*, consisting of the components that must load in order for you to use an application. The *prefetch* is generally around ten percent of the total application size, though this can vary depending on the application. The application launches immediately after the *prefetch* is transferred.

Applications can be registered to the local device. Registration creates Start Menu icons, Desktop shortcuts, and file associations for the application. After  applications are fully cached on the local device they are available offline.

To learn more about Spoon, visit [http://spoon.net](http://spoon.net).

### Supported Platforms ###

The Spoon Plugin works with most Internet browsers, including Microsoft Internet Explorer, Firefox, Safari, Google Chrome, Opera, and all other browsers built using the Gecko API.

## Register Virtual Applications in the Windows Shell ##

### Introduction to the SpoonReg Registration Tool ###
SpoonReg is a tool that provides a command-line interface for deploying virtual applications and managing the virtual desktop environment. Users and administrators can use SpoonReg to register virtual applications for a single user or, in the case of administrators, a group of users or devices. SpoonReg can be used to deploy and manage virtual applications and layers built using Spoon IDE. 

After virtualizing an application with Spoon IDE, you can make the Start Menu icons, shortcuts, and file associations available on a user's desktop. SpoonReg enables you to register Spoon virtual applications in the shell, creating associations that generally are created during a standard installation process. Unlike an installation, registration and un-registration are performed instantaneously.

SpoonReg also enables you to create, reset, and remove application sandboxes: virtual environment "bubbles" where virtualized applications reside. Sandbox management provides control over application linking and intercommunication.

Spoon Server users and administrators can use SpoonReg to register applications to the desktop. For specialized deployment scenarios, contact your Spoon representative to learn how to obtain your own version of the SpoonReg.exe utility.

### Registering Virtual Applications Using SpoonReg ###

SpoonReg provides a command-line interface for managing the virtual desktop environment. This section describes basic SpoonReg command-line syntax, including steps for registering, updating, and unregistering virtual applications.

### Command-Line Syntax ###

The following table lists the different naming conventions used with SpoonReg:
<table>
  <tr>
	<th>Parameter</th>
	<th>Description</th>
  </tr>
  <tr>
    <td>AppSpec</td>
	<td>Path (relative or fully-qualified) to a virtual executable or layer built with Spoon IDE</td>
  </tr>
  <tr>
    <td>SandboxSpec</td>
	<td>Name or path of a virtual sandbox</td>
  </tr>
</table>

### Registering a Virtual Application ###

To register an application, use the following command:

    SpoonReg.exe AppSpec

This command creates all Start Menu items, Desktop shortcuts and file associations used with the virtual application executable.

By default, registration creates a local cached copy of the virtual application executable and uses the local profile as the sandbox location.

**Note**: The sandbox location specified during the virtual application build is ignored when registering applications using the SpoonReg tool.

### Advanced Registration Options ###

Command-line parameters control caching behavior and sandbox where the virtual application should be registered:

    SpoonReg.exe [Options] AppSpec[@SandboxSpec]

<table>
  <tr>
	<th>Parameter</th>
	<th>Behavior</th>
  </tr>
  <tr>
    <td>/nocache</td>
	<td>The virtual application executable will not be copied to a client machine. All shortcuts and file associations point to the full path as given by <strong>AppSpec</strong>.</td>
  </tr>
  <tr>
    <td>/id {00000000-0000-0000-0000-000000000000}</td>
	<td>Specify the internal guid used to uniquely identify the application.  There are no published uses for this value today.</td>
  </tr>
  <tr>
    <td>SandboxSpec</td>
	<td>Name and path to an existing sandbox. If this parameter is specified and a sandbox with that name exists, the application will register into that sandbox.</td>
  </tr>
</table>

### Updating Registration Settings ###

Application registration settings can be changed by re-executing the registration command with the desired options:

    SpoonReg.exe [Option] AppSpec[@SandboxSpec]

<table>
  <tr>
	<th>Parameter</th>
	<th>Behavior</th>
  </tr>
  <tr>
    <td>/nocache</td>
	<td>Disable caching of the specified application (reverses the /cache setting).</td>
  </tr>
  <tr>
    <td>/cache</td>
	<td>Enable caching of the specified application (reverses the /nocache setting).</td>
  </tr>
</table>

### Un-registering a Virtual Application ###

Un-registering a virtual application reverses the registration process, removing the virtual application, Start Menu icons, shortcuts, and file associations.

To un-register a virtual application, use the following command:


    SpoonReg.exe /unregister AppSpec[@SandboxSpec]

You can also un-register all applications with the single command:

    SpoonReg.exe /unregisterall

## Client Profiles ##
You can apply the SpoonReg command to **Local**, **All Users** or **Roaming** Microsoft Windows profiles. These profiles correspond to the user profiles available in Microsoft Windows. 

### Local Profile ###

Each user on a Microsoft Windows device has a local user profile. Any changes to the local profile affect only that user on that device. The **Local** profile is the default profile used by SpoonReg if no profile is specified on the SpoonReg command line.

### All Users Profile ###

Each device has a single **All Users** profile. Any changes made to the **All Users** profile affect all users on the device. To register an application to the All Users profile, run the SpoonReg command with the **/allusers** command-line flag. You must have administrative permissions on the device to register applications to the **All Users** profile.

**Note**: If the **/allusers** flag is used when registering an application, it must also be used when unregistering.

### Roaming Profile ###

Each user in an Active Directory environment can have a roaming profile which is mirrored to other machines according to directory policy. Typically, the roaming profile is stored on a network server and is available from all devices on a network. To register an application to the **Roaming** profile, run the SpoonReg command with the **/roaming** flag.

**Note**: There is no roaming profile for All Users. The **/roaming** flag has no impact when used in conjunction with the **/allusers** flag.

**Note**: Because SpoonReg is applied to specific user profiles, it cannot be used for the **LocalSystem** account.

## Sandbox Management ##

The SpoonReg tool enables you to create and manage one or more virtual environment sandboxes.
 
A *sandbox* contains all of a virtual application's data and settings (as determined by the virtual application's isolation configuration settings). Applications registered to the same sandbox can view and modify each other's virtualized data and settings.

All applications are registered into a single default sandbox named **Default**. You can group related applications into a sandbox that is treated as a single management unit. When a sandbox is reset, all application content and data stored in that sandbox is purged and it reverts back to the default state.

### Creating a Sandbox ###

If no sandbox is specified during registration, the application is registered to the default sandbox (**Default**). 

To create an additional sandbox, use one of the following commands:

    SpoonReg.exe [Profile] /create [SandboxName] [SandboxPath]
    SpoonReg.exe [Profile] /c [SandboxName] [SandboxPath]
    
If no path is provided, a default path is created in the **AppData** folder under the specified profile.

### Resetting a Sandbox ###

Resetting a sandbox reverses all changes made to the sandbox, including any changes to data or settings made by the user. This restores all applications registered to the sandbox to their default state.
 
To reset a sandbox, use one of the following commands:

    SpoonReg.exe [Profile] /reset [SandboxSpec]
    SpoonReg.exe [Profile] /r [SandboxSpec]

If a **SandboxSpec** is not supplied, the default sandbox is reset.

### Deleting a Sandbox ###

Deleting a sandbox removes all applications, data, and settings from the sandbox.
 
To delete a sandbox, use one of the following commands:

    SpoonReg.exe [Profile] /delete [SandboxSpec]
    SpoonReg.exe [Profile] /d [SandboxSpec]

If a **SandboxSpec** is not supplied, the default sandbox is reset (the default sandbox cannot be deleted). Any applications registered to the deleted sandbox are moved to the default sandbox.

### Moving a Sandbox ###

You can use SpoonReg to move the sandbox location to a given path. 

Use the following command to move a sandbox:

    SpoonReg.exe [Profile] /move [SandboxSpec] [SandboxPath]

## Deploy in Active Directory Environments ##

This section you will learn how to leverage Microsoft's Active Directory infrastructure with SpoonReg to deploy Spoon virtual applications. 

### Active Directory ###

Active Directory enables the network administrator to manage users and groups within an organization. Many organizations use Active Directory to manage their network services. By combining Active Directory with SpoonReg, administrators can deploy virtual applications easily and reliably to one or more users in their organization.

### SpoonReg ###

SpoonReg manages the virtual desktop environment for a given user by registering and unregistering virtual applications. The following is a typical SpoonReg command to register an application (in this case, Firefox):

    \\VirtualAppServer\Tools\SpoonReg.exe \\VitualAppServer\Apps\Firefox.exe

SpoonReg copies the virtual application executable, creates Start Menu items, Desktop shortcuts and file associations.
 
### Using SpoonReg with Active Directory ###

Organizations tend to manage a group of users rather than single users one at a time. By combining Active Directory with SpoonReg you can manage the virtual environment for a user, group, or organizational unit.

**Note**: In order to manage virtual applications using Active Directory, the users must have access to a shared network drive where the virtual application executable files exist. This can be specified by a full UNC path, or by using a mapped network drive.

### Linking an Organizational Unit (OU) to a Group Policy Object (GPO) ###

Active Directory offers many ways to manage network services for an organization. In this section you will learn how to use an OU in combination with a GPO to manage a virtual application environment for a set of users.

#### Organizational Unit (OU) ####

In Active Directory, OUs are containers where you can place users, groups and other OUs. Using these containers, the administrator can create a structure that models hierarchical or logical structures within the organization. By setting up OUs you can isolate different groups of users that receive their own set of virtual applications. This is ideal for Accounting, Sales, Marketing, etc.

#### Group Policy Object (GPO) ####

GPOs are a way of applying a set of rules and features to a targeted set of users. GPOs handle security, application installation, logon/logoff scripts, Microsoft Internet Explorer settings and more. A GPO is applied when a user logs on to a domain. Based on the profile, various GPOs are applied.

#### SpoonReg and the GPO ####

For virtual application deployment, you can configure the GPO to run SpoonReg commands to register a given set of virtual applications. You can create and edit GPOs using the **Group Policy Object Editor**. This is an add-on to Microsoft's Active Directory. Create a logon script that registers the virtual applications for a particular group in the organization. Do this under User **Configuration > Windows Settings > Scripts in the Group Policy Object Editor**. 

For an accounting group you might add the following logon script:
    
    \\VirtualAppServer\Tools\SpoonReg.exe \\VirtualAppServer\AllVirtualApps\Excel.exe
    \\VirtualAppServer\Tools\SpoonReg.exe \\VirtualAppServer\AllVirtualApps\Firefox.exe
    \\VirtualAppServer\Tools\SpoonReg.exe \\VirtualAppServer\AllVirtualApps\AcrobatReader.exe
    
For a graphic design group you might add the following logon script:
    
    \\VirtualAppServer\Tools\SpoonReg.exe \\VirtualAppServer\AllVirtualApps\AdobeIllustrator.exe
    \\VirtualAppServer\Tools\SpoonReg.exe \\VirtualAppServer\AllVirtualApps\Firefox.exe
    \\VirtualAppServer\Tools\SpoonReg.exe \\VirtualAppServer\AllVirtualApps\AcrobatReader.exe 
    
### Linking the GPO to the OU ###

After you set up the OU and the GPO, link them through the Group Policy Object Editor. After they are linked, any users in that OU have the linked GPOs applied when they logon. All of their virtual applications will appear when they logon to any machine on the domain where the GPO applies.

**Note**: SpoonReg has additional capabilities that can be applied in the GPO logon script, such as unregistering applications or registering applications to a specific sandbox.

### Using Startup Scripts with GPOs to Deploy Virtual Applications ###

This section describes how to use Startup Scripts to deploy virtual applications to the All Users profile on a host system.

#### Create a GPO With the Startup Script ####

You can configure the GPO to run SpoonReg commands to register a given set of virtual applications to the All Users Profile. This enables any user who logs into a host system to have access to registered virtual applications.

Complete the following steps to create a new GPO with the Group Policy Management Console (GPMC):

1. Open the **GPMC**.
2. Right-click on the OU to which you want to link a GPO.
3. Select **Create and Link a GPO Here** and give it a name.
4. Right-click the GPO and select **Edit**. This opens the **Group Policy Object Editor**.
5. Navigate to **Computer Configuration > Windows Settings > Scripts**.
6. Open the **Startup** item.
7. Select **Show Files**. A directory will display. Using that directory, create a **.bat** file. This file serves as the **Startup Script** that deploys your virtual applications to all the computers in the specified OU.

The following examples serve as a guide to creating the startup script:

**Example 1**: Register virtual applications to the default sandbox in the **All Users** profile:
    
    \\VirtualAppServer\Tools\SpoonReg.exe /allusers \\VirtualAppServer\AllVirtualApps\Excel.exe
    \\VirtualAppServer\Tools\SpoonReg.exe /allusers \\VirtualAppServer\AllVirtualApps\Firefox.exe
    \\VirtualAppServer\Tools\SpoonReg.exe /allusers \\VirtualAppServer\AllVirtualApps\AcrobatReader.exe
    
**Example 2**: Register virtual applications to the specified sandbox in the **All Users** profile:
    
    \\VirtualAppServer\Tools\SpoonReg.exe /allusers /c sandboxname
    \\VirtualAppServer\Tools\SpoonReg.exe /allusers \\VirtualAppServer\AllVirtualApps\Excel.exe
    \\VirtualAppServer\Tools\SpoonReg.exe /allusers \\VirtualAppServer\AllVirtualApps\Firefox.exe
    \\VirtualAppServer\Tools\SpoonReg.exe /allusers :\\VirtualAppServer\AllVirtualApps\AcrobatReader.exe 

After creating the startup script, add it to the GPO:

1. Navigate to **Computer Configuration > Windows Settings > Scripts** in the **GPMC**.
2. Open the **Startup** item.
3. Select **Add**.
4. Select **Browse**.
5. Select the **Startup Script**.
6. Select **Open**.
7. Select **OK**.
8. Select **OK**.

## Deploy Virtual Applications Using MSI Setup Packages ##

Spoon IDE enables you to deploy virtual applications and components using legacy MSI setup package technology.

### Create MSI Setup Packages Directly Within Studio ###

Spoon IDE enables you to create standalone MSI packages directly within the Studio environment. Generated MSI setup packages can include Start Menu items, Desktop shortcuts, file associations, and other custom shell integration behaviors.

Deployment using generated MSI packages is appropriate in situations where existing MSI package deployment mechanisms are in place, or for deploying applications with shell integration without the SpoonReg tool.

Virtual application and component shell integration settings are shared between MSI and SpoonReg based deployment, enabling easy migration between deployment models.

For more information refer to [Building MSI Setup Packages](#building-msi-setup-packages).

### Deploy Virtual Applications into Legacy MSI Setup Packages ###

Spoon IDE supports deployment of virtual application executables into legacy MSI setup packages.

### Import Legacy MSI Setup Packages ###

Spoon IDE supports one-click import of legacy MSI setup packages into the Spoon IDE environment. Following import, you can customize and deploy the application as a Spoon virtual application or **SVM**.

## Deploy Virtual Applications Using Microsoft Terminal Services RemoteApp ##

In this section you will learn how to deploy Spoon virtual applications using Microsoft Windows 2008 Terminal Services RemoteApp server.

### Terminal Services RemoteApp ###

Terminal Services RemoteApp is a server-side program that provides remote access to applications on a terminal server. Applications configured with TS RemoteApp appear as if they are running on a user's machine. End-users can run RemoteApps side-by-side with local programs or other RemoteApps.

Complete the following steps to utilize virtual applications created in Spoon IDE with Microsoft TS RemoteApp:

1. On the TS RemoteApp server, open the TS RemoteApp Manager. Choose **Add RemoteApp Programs** by right-clicking inside the **RemoteApp Programs** list or through the **Action** drop down menu.
2. Select **Next** in the **RemoteApp Wizard**.
3. Select **Browse** and choose the virtual application executable.
4. After the virtual application is added to the list, select it and choose **Properties**.
5. If the virtual application has multiple Startup Files, configure the RemoteApp Program **Name** and **Alias**.; otherwise the TS RemoteApp server will not distinguish between the separate applications in the suite.
6. Choose **Always Use the Following Command-line Argument**, enter the **Trigger** for the Startup File, and select **OK**.
7. In the **RemoteApp Programs** list, right-click the program you added and choose **Create .rdp File**. There are no special requirements for the .rdp files.

If there are multiple Startup Files, repeat these steps and deploy the shortcuts on the host systems.


## Deploy Using the Publish to Spoon Server Feature ##
This section describes how to deploy virtual applications to Spoon Server using the Publish to Spoon Server button in Spoon Studio.

There are some basic requirements for using the Publish to Spoon Server feature:

1. The Spoon Server must be configured to use login authentication and there must be at least on user in the **Server Administrators** group.
2. A startup file must be specified in the Spoon Studio configuration.

After completing the application build process, click the Publish to Spoon Server button located on the ribbon bar. In the login form, enter the URL for the Spoon Server and login as a server administrator. On the next screen confirm the application details and click OK. This will upload the application to the Spoon Server and create a new application version.

The new version will not be visible to users until the **Publish** flag is set. To make the application visible, login to the Spoon Server

**Note**: When publishing to Spoon Server, the portal *cannot* be set to **Anonymous** access.
