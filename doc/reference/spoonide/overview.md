Spoon IDE enables you to convert your Windows, .NET, Java, AIR, Flash, Shockwave, or other Windows-compatible applications into self-contained virtual applications. These applications can be delivered as standalone executables, MSIs or streamed from the web and run instantly on end-user devices. Unlike traditional deployment methods, virtual applications do not require reboots, administrative privileges, or separate setup steps for external components and runtimes. Virtual applications are isolated from other system applications, preventing DLL conflicts and other deployment nightmares.

## Supported Platforms ##
Spoon IDE supports the following platforms for virtual application build, snapshotting, and execution:

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

Spoon IDE supports both 32- and 64-bit applications. Both 32-bit (under 32-bit mode) and 64-bit executables can be run on x64-based platforms.

Spoon IDE supports these operating systems running within VMware and Microsoft hardware virtualization and hypervisor environments. Spoon IDE has limited support for the Windows Preinstallation Environment (WinPE), though certain applications (depending on operating system features unavailable in WinPE) may not function properly.

**Note:** Spoon IDE does not support creation of 16-bit executables. To run 16-bit DOS applications, virtualize an appropriate emulator with the application and launch the application through the emulator.

## User Interface ##

Using the Spoon IDE user interface enables you to configure the filesystem and registry of a virtual application, embed external runtimes and components, take application snapshots, and create Spoon Virtual Machine (SVM) or executable files. The primary interface consists of a ribbon bar along the top and several panes accessed by buttons on the left.

#### Items Located Above the Ribbon Bar ####

- The Start Menu button, or the circle at the top left of the window, enables virtual application configurations to be created, opened, saved, imported, applied, and closed.
- The Options bar provides Spoon IDE interface customization options, as well as the ability to set proxy settings and install certificates.
- The Help bar provides access to Spoon IDE documentation.

### Spoon IDE Ribbon Bar ###
- The Virtual Application tab provides access to the snapshot and build features, as well as output configuration options such as the startup file, output directory, and diagnostic-mode selection.
- The Runtimes tab provides a selection of auto-configurable runtime engines which can be embedded into your application with a single click. These include .NET Framework, Java, Flash, Shockwave, Acrobat Reader, and SQL Server 2005 Express runtimes.
- The Advanced tab provides advanced Spoon IDE functions such as Platform Merge and Streaming.

#### Left-side button panes ####

- The **Filesystem** pane displays the application virtual filesystem, and enables you to add and remove virtual files and directories.
- The **Registry** pane displays the application virtual registry, and enables you to add and remove virtual registry keys and data values.
- The **Settings** pane enables you to configure virtual application metadata, startup image and shim, and process configuration options.
- The **Components** pane enables you to layer external virtual application components, such as toolbars and optional features.
- The **Setup** pane enables you to configure the MSI setup package, shortcuts, and other shell integration options.
- The **Expiration** pane enables you to configure application expiration options.

**Note:** Spoon IDE users are responsible for any third-party licensing compliance for redistributable components included using virtualization.

## Virtual Filesystem ##
Spoon IDE enables you to embed a *virtual filesystem* into your executable. Embedded files are accessible by your Spoon-processed application as if they were present in the actual filesystem. Virtual files, unlike files on the host device, are not visible from and do not require changes to the host device. Virtual files do not require security privileges on the host device, regardless of whether the virtual files reside in a privileged directory. Because virtual files are embedded in the application executable, shared DLLs do not interfere with or are overwritten by other applications on the host device.

**Note:** When running a virtual application on Windows 7, the **All Users Directory\Application Data** and **All Users Directory** root folders will map to the same folder at runtime. To prevent one setting from overriding another, verify that the isolation settings for these folders are the same.

#### Isolation Modes ####

In the event of a conflict between a file in the virtual filesystem and a file present on the host device, the file in the virtual filesystem takes precedence.

Folders may be virtualized in **Full**, **Merge**, **Write Copy**, or **Hide** mode.

- **Full**: Full mode is used when a complete level of virtual application isolation is your desired outcome. Only files in the virtual filesystem are visible to the application, even if a corresponding directory exists on the host device, and writes are redirected to the sandbox data area. 
- **Merge**: Merge mode is generally used when some level of interaction with the host device is your desired outcome. For example, **Merge** mode can be used to enable the virtualized application to write to the host device's **My Documents** folder. Files present in a virtual folder are merged with files in the corresponding directory on the host machine, if such a directory exists. Writes to host files are passed through to the host device and writes to virtual files are redirected into the sandbox data area. 
- **Write Copy**: Write Copy mode is used when a virtual application must be read from files already present on the host device, but isolation of the host device is still desired. Files present on the host device are visible to the virtual environment, but any modifications to folder contents are redirected to the sandbox data area. 
- **Hide**: Hide mode is used when a file on the host machine could interfere with the application's ability to run properly. By adding a file or folder with **Hide** enabled, the application receives a File Not Found message, even if the file or folder exists on the host machine. Files and folders with **Hide** enabled will return a **File Not Found** message to the application at runtime. This applies to both the virtual filesystem and the host file system. 

**Tip**: To apply selected isolation modes to all subfolders, right-click on the folder, choose Isolation, select the checkbox for **Apply to Subfolders**, then select **OK**.

#### File Attributes ####

Files and folders can be hidden from shell browse dialogs and other applications. This is used to prevent internal components and data files from being displayed to the user. To hide a file or folder, select the checkbox in the **Hidden** column adjacent to the desired file or folder.

**Note**: The **Hidden Flag** is NOT the **Hide** isolation mode. Enabling the **Hidden Flag** prevents a file or folder from displaying in browse dialogs or from directory enumeration APIs; it does not prevent the application (and potentially the end-user) from accessing the folder or file contents by direct binding. To prevent the file or folder from being found by the application, enable **Hide** isolation mode.

Flagging files and folders as read-only prevents the application from modifying the file or folder contents. To make a file or folder read-only, select the checkbox in the **Read Only** column next to the desired file or folder.

#### No Upgrade ####

By default, Spoon IDE enables files in the virtual filesystem to be upgraded with patches (refer Updating Registration Settings in the [Register Virtual Applications in the Windows Shell](register-virtual-applications-in-the-windows-shell) section for more information). If there are files in the virtual filesystem that should not be upgraded, such as user data files, select the **No Upgrade** flag to prevent these files from being upgraded.

#### No Sync ####

This feature only applies to virtual applications that are delivered and managed by Spoon Virtual Desktop Server, or Spoon.net. By default, Spoon IDE enables files in the virtual filesystem to be synchronized to a user's Spoon account. This enables the application state to be maintained across different devices that are Spoon enabled. If there are folders in the virtual filesystem that should not be synchronized, but should remain only on the local device, enable the **No Sync** flag to prevent files within the folder from being synchronized. This setting is managed on a folder level and applies to all files within that folder.

### Filesystem Compression ###

To reduce executable size, Spoon IDE can compress virtual filesystem contents. This reduces virtual application size by approximately 50%, but also prevents profiling and streaming of the application. By default, the **Compress Payload** option in the **Process Configuration** area of the **Settings** panel is unchecked. Leave this box unchecked during the build process if the application will be optimized for streaming from Spoon Server.

**Note**: Disabling payload compression may significantly increase the size of the virtual application binary.

## Building from the Command-line ##


## Modify Application Behavior from the Command-line ##
