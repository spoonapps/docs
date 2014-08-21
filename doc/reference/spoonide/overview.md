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

## Virtual Registry ##
Spoon IDE enables you to embed a virtual registry into your executable. Embedded registry keys are accessible by your Spoon-processed application as if they were present in the actual registry. Unlike data present on the host device, virtual registry keys and values are not visible from and do not require changes to the host device. The use of a virtual registry does not require security privileges on the host device, even if the virtual registry entries are in a privileged section of the registry. Because virtual registry entries are embedded in the application executable, other applications are unable to disrupt application execution by inadvertent modification of registry entries.

The **Classes** root, **Current User** root, **Local Machine** root, and **Users** root folders correspond to the **HKEY\_CLASSES\_ROOT**, **HKEY\_CURRENT\_USER**, **HKEY\_LOCAL\_MACHINE**, and **HKEY\_USERS** keys on the host machine. 

Registry string values can include well-known variables such as **@WINDIR@**, **@SYSWOW64@**, **@PROGRAMFILESX86@** and **@PROGRAMFILES@**.

#### Isolation Modes ####

In the event of a conflict between a key or value in the virtual filesystem and data present on the host device registry, information in the virtual registry takes precedence. Keys may be virtualized in **Full**, **Merge**, **Write Copy**, or **Hide** mode.

- **Full**: In Full mode, values only in the virtual registry are visible to the application, even if a corresponding key exists on the host device, and writes are redirected to the user registry area.
- **Merge**: In Merge mode, values present in a virtual key are merged with values in the corresponding key on the host machine (if such a key exists). Writes to host keys are passed through to the host registry and writes to virtual keys are redirected to the user registry area.
- **Write Copy**: Write Copy mode is used when a virtual application must be read from registry keys already present on the host device, but isolation of the host device is still desired. Keys and values present on the host device are visible to the virtual environment, but any modifications to keys or values are redirected to the sandbox data area. 
- **Hide**: Keys and values in the virtual registry or the corresponding host registry will not be found by the application at runtime.

**Tip**: To apply selected isolation modes to all subkeys, right-click on the key, choose **Isolation**, select the checkbox for **Apply to Subkeys**, then **OK**.

#### No Sync ####

This feature only applies to virtual applications that are delivered and managed by Spoon Virtual Desktop Server, or Spoon.net. By default, Spoon IDE enables registry keys in the virtual registry to be synchronized to a user's Spoon account. This enables the application state to be maintained across different devices that are Spoon enabled. If there are keys in the virtual registry that should not be synchronized, but should remain only on the local device, enable the **No Sync** flag to prevent that key and any values within the key from being synchronized. This setting is managed on a registry key level and applies to all values within that key.

#### Importing Registry Hive Files ####

Spoon IDE can import registry hive (.reg) files into the virtual registry. To import a .reg file, select the **Import** button in the **Registry** panel, then choose the registry hive file to import.

## Virtual Application Settings ##

<table>
	<tr>
		<th>Setting</th>
		<th>Description</th>
	</tr>
	<tr>
		<td><b>Startup File</b></td>
		<td>The executable or viewable file that opens when the user starts the virtual application. Multiple files can be selected by clicking the <b>Multiple</b> button.</td>
	</tr>
	<tr>
		<td><b>Output File</b></td>
		<td>The name of the output file from the IDE build process.</td>
	</tr>
	<tr>
		<td nowrap><b>Project Type</b></td>
		<td><b>Application</b>: A virtual application project produces an executable file output (.exe file) that can be run directly from the operating system. Application output mode is appropriate for most users and is the default selection.<br/><br/><b>Component</b>:  A component project produces an SVM (.svm file). SVM is a Spoon file format which encode all virtual application configuration and content into a single binary file. SVMs cannot be executed directly from the operating system. SVMs are used to exchange virtual application and component data between multiple virtual applications.<br/><br/>Note: In order to create SVMs for use in streaming applications on Spoon Server, the project type must be set to Component.</td>
	</tr>
	<tr>
		<td><b>Executable Metadata</b></td>
		<td><b>Standard metadata</b> includes information such as product title, publisher, description, icon, web site URL, and version. By default, Spoon IDE applies metadata inherited from the virtual application startup file to the output virtual application executable. To override the default meta data, uncheck the <b>Inherit Properties</b> box.<br/><br/><b>Custom metadata</b> can be used by specialized external executable viewer applications, inventory scanners, and other asset and licensing management systems. For information on custom executable metadata, consult the Microsoft Windows Software Development Kit.</td>
	</tr>
	<tr>
		<td><b>Startup Image</b></td>
		<td>A startup "splash" image to display during application startup. Startup images improve application branding and are useful when the application requires several seconds to initialize.<br/><br/>Transparency keying enables the startup image to contain transparent regions. Transparencies improve the visual effectiveness of your startup image.</td>
	</tr>
	<tr>
		<td><b>Startup Shim</b></td>
		<td>Startup shims are used to perform customized licensing checks and other initialization tasks. The shim must conform to the Spoon IDE interface in order to validate.<br/><br/>The startup shim must compile with an <b>OnInitialize</b> method.<br/><br/><b>C-style startup shim signature</b><br/><br/>typedef BOOL (__stdcall *FnOnInititialize) (LPCWSTR pwcsInitilizationToken);<br/><br/>The return value indicates whether virtual machine execution proceeds.<br/><br/>Methods are acquired via <b>::LoadLibrary</b> followed by <b>::GetProcAddress</b> calls. <br/><br/><b>Example</b><pre>LPCWSTR pwcsInitToken = "VendorSpecificToken";<br/>HMODULE hShim = ::LoadLibrary("Shim.dll");<br/>FnOnInititialize fnOnInit = (FnOnInititialize)::GetProcAddress(hShim, "OnInitialize");<br/>BOOL fResult = fnOnInit(pwcsInitToken);</pre></td>
	</tr>
	<tr>
		<td><b>Directory Binding</b></td>
		<td>Spoon IDE enables you to limit where an application will run, based on queries to an Active Directory Domain Controller.</td>
	</tr>
	<tr>
		<td><b>Command Line Arguments</b></td>
		<td>Command line arguments specified by the user are passed to the virtual application startup executable by default. You can override and specify a fixed set of command line arguments to pass to the startup executable. For example, you can specify Java virtual machine behavior.</td>
	</tr>
	<tr>
		<td><b>Sandbox Location</b></td>
		<td>By default, the sandbox is placed in the <b>@APPDATALOCAL@\Spoon\Sandbox\@TITLE@\@VERSION@</b> folder, where <b>@APPDATALOCAL@</b> represents the <b>local Application Data</b> folder, and <b>@TITLE@</b> and <b>@VERSION@</b> represent the application title and version. In addition to the standard root folder variables, the sandbox location can contain the following variables:<br/><br/><b>@TITLE@</b>: Product title<br/><b>@PUBLISHER@</b>:  Product publisher<br/><b>@VERSION@</b>:  Full version string, in dotted quad format<br/><b>@WEBSITE@</b>:  Publisher website<br/><b>@BUILDTIME@</b>: Virtual application build time, in a format similar to <b>2008.02.01T08.00</b>.<br/><br/>With the exception of the <b>@BUILDTIME@</b> variable (set automatically), these variables are based on the values specified in the <b>Properties</b> section of <b>Settings</b>.</td>
	</tr>
	<tr>
		<td><b>Working Directory</b></td>
		<td><b>Working Directory</b> determines the active directory at the time of process launch. <br/><br/>Use <b>Startup File Directory</b> sets the working directory to the directory of the virtual application startup file. In the case of a jukeboxed application, the working directory is set to the directory of the startup file specified on the jukebox command line. <br/><br/>Use <b>Current Directory</b> sets the working directory to the directory from which the virtual application is launched. <br/><br/>Use <b>Specified Path</b> enables you to specify a working directory. This specification can include environment and well-known root folder variables. <br/><br/>The working directory is set to the directory of the startup file by default.</td>
	</tr>
	<tr>
		<td><b>Application Type</b></td>
		<td>If you select an executable startup file, Spoon IDE automatically configures the virtual application to run in the same subsystem as the startup file. If you select a non-executable startup file, you must manually override the application type. Most applications execute in the GUI subsystem. To override the application type, select the mode from the Application Type menu in the Process Configuration section of the Settings panel. The Inherit mode sets the application type based on the type of the startup file.</td>
	</tr>
	<tr>
		<td><b>Target Architecture</b></td>
		<td><b>Target Architecture</b> is automatically captured during the snapshot process and generally should not be altered for applications packaged through the snapshot process.<ul><li><b>x86</b>:  Use this option for applications that were packaged using the snapshot process on x86 systems. This option maps the <b>Program Files</b> directory to <b>C:\Program Files</b> on x86 systems or to <b>C:\Program Files (x86)</b> on x64 systems. .NET applications compiled to target any CPU architecture always run as 32-bit applications. </li><li><b>x64</b>:  Use this option for applications that were packaged using the snapshot process on x64 systems. This option maps the <b>Program Files</b> directory to <b>C:\Program Files</b> on x64 systems. The <b>Program Files (x86)</b> directory is mapped to <b>C:\Program Files</b> on x86 systems and <b>C:\Program Files (x86)</b> on x64 systems. .NET applications compiled to target any CPU architecture run as 32-bit applications on x86 systems and 64-bit applications on x64 systems.</li><li><b>Any CPU</b>:  This option maps the <b>Program Files</b> directory to <b>C:\Program Files</b> on x86 systems and <b>C:\Program Files</b> on x64 systems. .NET applications compiled to target any CPU architecture run as 32-bit applications on x86 systems and 64-bit applications on x64 systems.  Use this option to place a .NET application that is compiled to target any CPU architecture in the <b>Program Files</b> folder.</li></ul></td>
	</tr>
	<tr>
		<td><b>Environment Variables</b></td>
		<td>Most virtual environment variables overwrite any environment variables defined in the host environment. However, <b>PATH</b> and <b>PATHEXT</b> environment variables always merge with the corresponding host environment variables.<br/><br/>Environment variables are automatically captured and merged during the snapshot delta process.</td>
	</tr>
	<tr>
		<td><b>Virtual Services</b></td>
		<td>Windows services are specialized applications that run in the background. They are typically responsible for providing system services such as database services, network traffic handling, web request processing, and other server functionality. Many applications install and require specific services in order to function properly. Spoon IDE fully supports virtualization of certain Windows services. <br/> <br/> Service installation and settings are captured automatically during the snapshot process. The primary exception occurs with virtualized applications intended to run as background worker services (for example, virtualized web servers); in this case, it is often required to enable the <b>Keep Alive</b> option.</td>
	</tr>
	<tr>
		<td><b>SVMs</b></td>
		<td>You can specify additional SVM layers for applications, in the case of updates or patches.</td>
	</tr>
	<tr>
		<td><b>Child Process Exceptions</b></td>
		<td>Some applications create new child processes while they run. Depending on the virtual application context, you can create such child processes within the virtual application, or in the host operating system.<br/><br/>Child processes include processes created to service COM local server requests.<br/><br/><b>Note</b>: Child processes created outside of the virtual application cannot access virtualized filesystem or registry contents. These processes can access or modify host operating system contents, even if otherwise forbidden by the virtual application configuration.<br/><br/>Child processes are created within the virtual application by default. To manually create child processes outside of the virtual application, uncheck the <b>Spawn child process within virtualized environment</b> option.<br/><br/>COM servers are created outside the virtual environment by default to allow COM communication between native applications and virtual applications. To create COM servers within the virtual environment, check the <b>Spawn COM servers within virtualized environment</b> option.<br/><br/>You can determine exceptions to the child process virtualization behavior using the <b>Child Process Exception List...</b> Process names listed in the child process exception list behave <em>opposite</em> to the master child process virtualization setting. To edit the child process exception list, select the <b>Child Process Exception List... </b> button. Process names will match without including the filename extension.</td>
	</tr>
	<tr>
		<td><b>Read-only Virtual Environments </b></td>
		<td>Prevent modifications to the virtual environment.</td>
	</tr>
	<tr>
		<td><b>Automatic Sandbox Reset</b></td>
		<td>Any changes made to an application's virtual environment are reverted when the application closes.</td>
	</tr>
	<tr>
		<td><b>Shutdown Process Tree On Root Process Exit</b></td>
		<td>enables the shutdown of all child processes when the root process exits.

**Note**: The startup file is the root process by default. If a virtual service is specified in the application configuration file and is set to auto-start when the application is launched, the virtual service acts as the root process in the process tree.</td>
	</tr>
	<tr>
		<td><b>Compress Payload</b></td>
		<td>Enables compression of the output file. Note: Both the application profiling and streaming processes require that packages be built uncompressed. To build applications without compression, leave the **Compress payload** option unchecked.</td>
	</tr>
	<tr>
		<td><b>Startup Executable Optimization</b></td>
		<td>Launches the startup executable within the initial virtual machine process. This prevents the creation of a separate application process and can be incompatible with some applications.</td>
	</tr>
	<tr>
		<td><b>Spoon Command-line Arguments</b></td>
		<td>Spoon supports command-line arguments of the /X[arg] form, which modify virtual application behavior at run-time. In rare instances, these arguments may conflict with command-line arguments designed for use by the virtualized application. To disable processing of these arguments, uncheck the Enable Spoon command-line arguments box.</td>
	</tr>
	<tr>
		<td><b>Window Class Isolation</b></td>
		<td>prevents viewing window classes that are registered by external processes. You can use this to prevent interaction between virtualized and non-virtualized versions of the same program when the application checks for existing class registrations.
</td>
	</tr>
	<tr>
		<td><b>Enhanced DEP Compatibility for Legacy Applications</b></td>
		<td>enables compatibility for systems with Data Execution Protection (DEP) enabled. Use this configuration for virtual applications running on Windows 2003.</td>
	</tr>
	<tr>
		<td><b>Enhanced DRM Compatibility</b></td>
		<td>enables additional compatibility with common DRM systems, such as Armadillo.</td>
	</tr>
	<tr>
		<td><b>Trace Process Starts in Debug Output</b></td>
		<td>sends a notification to **OutputDebugString** whenever a new process is started within the virtual environment. This notification is in XML format and comes as a basic information description. It can be monitored with any debugging tool. You can also monitor the notification by a parent process within the virtual environment if a child process is being debugged.</td>
	</tr>
	<tr>
		<td><b>Force Read-share Files</b></td>
		<td>forces any file opened within the virtual environment to open with the **READ_SHARE** flag. Use this option to  resolve compatibility issues caused by sharing violations.</td>
	</tr>
	<tr>
		<td><b>Always Launch Child Processes as Current User</b></td>
		<td>provide child processes with the same level of privileges as the virtual machine root process. Child processes launched by the virtual machine have reduced privileges by default.</td>
	</tr>
	<tr>
		<td><b>Emulate Elevated Security Privileges</b></td>
		<td>forces an application to run as if it has elevated security privileges, even if the application does not. Enabling this option eliminates UAC security prompts for elevation and subsequent application crashes.</td>
	</tr>
</table>

## Runtimes and Components ##


## MSI Settings ##
<table>
	<tr>
		<th>Setting</th>
		<th>Description</th>
	</tr>
	<tr>
		<td><b>Output location</b></td>
		<td>Name and location of the MSI file output.</td>
	</tr>
	<tr>
		<td><b>Product Info</b></td>
		<td>Meta data that will go into Add/Remove Programs when the application is installed.<ul><li>Product Name</li><li>Product Version</li><li>Company Name</li></ul></td>
	</tr>
	<tr>
		<td><b>Installation Parameters</b></td>
		<td>Specifies where to install the application and if it will be installed for all users or in the current user profile.</td>
	</tr>
	<tr>
		<td><b>Shortcuts</b></td>
		<td>List of Start Menu and Desktop shortcuts that are created when the MSI is installed.</td>
	</tr>
	<tr>
		<td><b>ProgIds</b></td>
		<td>List of ProgIds that are created on the host system when the MSI is installed.</td>
	</tr>
	<tr>
		<td><b>Extensions</b></td>
		<td>List of file extensions that are configured on the host system when the MSI is installed.</td>
	</tr>
</table>

## Building from the Command-line ##


## Modify Application Behavior from the Command-line ##
