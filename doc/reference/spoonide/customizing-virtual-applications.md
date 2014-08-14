# Customizing Virtual Applications #
## Select a Project Type ##

Spoon IDE supports two project types:
Application: A virtual application project produces an executable file output (.exe file) that can be run directly from the operating system. Application output mode is appropriate for most users and is the default selection.
Component:  A component project produces an SVM (.svm file). SVM is a Spoon file format which encode all virtual application configuration and content into a single binary file. SVMs cannot be executed directly from the operating system. SVMs are used to exchange virtual application and component data between multiple virtual applications. 
Note: In order to create SVMs for use in streaming applications on Spoon Server, the project type must be set to Component.
To set the project type, select the appropriate option from the Project Type menu under the Virtual Application tab.

## Customize Executable Metadata ##

Executable metadata provides external applications with application information, such as identity, publisher, version, preferred display icon, and description. Metadata can be viewed and edited by selecting the Properties tab in the Settings pane.
Standard Metadata
Standard metadata includes information such as product title, publisher, description, icon, web site URL, and version. By default, Spoon IDE applies metadata inherited from the virtual application startup file to the output virtual application executable. Sometimes you can override the metadata. 
Complete the following steps to manually override executable metadata:
Uncheck the Inherit Properties box.
Enter the desired metadata in the appropriate fields of the Properties area.
Tip: If you do not want to override a specific field, enter Inherit as its value.
To revert to the default settings, check the Inherit Properties option.
Custom Metadata
In addition to standard Windows shell metadata, Spoon IDE enables introduction of custom metadata. Custom metadata can be used by specialized external executable viewer applications, inventory scanners, and other asset and licensing management systems.
Complete the following steps to add or modify custom metadata:
Select Custom Metadata. This displays the Custom Metadata dialog box. 
Enter the custom metadata property names and values. Only string-type custom metadata values are supported.
For information on custom executable metadata, consult the Microsoft Windows Software Development Kit.

## Add a Startup Image ##

Spoon IDE enables you to specify a startup "splash" image to display during startup. Startup images improve application branding and are useful when your application requires several seconds to initialize.
Adding a Startup Image
Complete the following steps to add a startup splash image:
Select the Startup Settings tab in the Settings pane
Choose the Select button adjacent to the Splash Image field.
Navigate to a BMP-format image to use as the startup graphic, and select Open.
The Display Splash Until option enables you to set how long the splash image is visible.
To remove the current startup image select Reset.
Transparency Keying
Transparency keying enables the startup image to contain transparent regions. Transparencies improve the visual effectiveness of your startup image.
Complete the following steps to select the transparency key color:
Choose the Select button adjacent to the Transparency Key label. This displays the transparency key selection dialog. 
Choose the color that represents transparent regions in the startup image and select OK.
To remove the transparency key color select Reset.
Previewing the Startup Image
To preview the startup image, select the Preview button.  Previewing enables you to verify that the transparency key is set properly.




## Compile and Add a Startup Shim ##

Spoon IDE enables you to specify a compiled startup shim invoked prior to the startup file. Startup shims are used to perform customized licensing checks and other initialization tasks. The shim must conform to the Spoon IDE interface in order to validate.
The startup shim must compile with an OnInitialize method.
C-style startup shim signature
typedef BOOL (__stdcall *FnOnInititialize) (LPCWSTR pwcsInitilizationToken);
The return value indicates whether virtual machine execution proceeds.
Methods are acquired via ::LoadLibrary followed by ::GetProcAddress calls. 
Example
LPCWSTR pwcsInitToken = "VendorSpecificToken";
HMODULE hShim = ::LoadLibrary("Shim.dll");
FnOnInititialize fnOnInit = (FnOnInititialize)::GetProcAddress(hShim, "OnInitialize");
BOOL fResult = fnOnInit(pwcsInitToken);
Complete the following steps to add a compiled startup shim DLL:
Select the Startup Settings tab in the Settings pane
Choose the Select button adjacent to the Startup Shim DLL field. 
Navigate to a DLL-format file to use as the startup shim and select Open.
Use the OnInitialize Parameter field to specify parameters for your startup shim.
To remove the current startup shim select Reset.
Note: See .xappl file format for adding multiple shims using a text editor. This is not supported in the UI at this time.


## Active Directory Binding ##
Spoon IDE enables you to limit where an application will run, based on queries to an Active Directory Domain Controller.
Required: domain
Choose the DNS Domain name that a computer must be a member of to run the application.
Required: group
Choose the Active Directory security group that a user must be a member of to run the application.
Note: Enabling this feature adds an Active Directory shim to the virtual application, which will run after user specified shims. Errors communicating with Active Directory are logged to debug output.

## Sandbox Location Configuration ##

Depending on the configured isolation settings, some edit and write operations are redirected by Spoon IDE into an application sandbox: a filesystem folder where isolated modifications persist. The sandbox is located in a folder or network where users have full read and write permission, enabling users to access and modify sandbox contents without authentication or User Account Control prompts.
Sandbox Placement Considerations
By default, the sandbox is placed in the @APPDATALOCAL@\Spoon\Sandbox\@TITLE@\@VERSION@ folder, where @APPDATALOCAL@ represents the local Application Data folder, and @TITLE@ and @VERSION@ represent the application title and version. The application title and version are configured in Properties. This location is the recommended default location for sandbox contents, as end-users have full permission to this location on standard Microsoft Windows configurations. Builds of the same virtual application use the same sandbox locations by default; modify this behavior if user settings should not persist between updates.
When publishing a new version of a virtual application, assign the sandbox to the same location as the previous version. This retains user settings and data. Assign the sandbox to a different location if you want to reset user settings and data.
If deploying the virtual application on a USB device, assign the sandbox to a sub-folder of the @APPDIR@ directory. This represents the directory containing the virtual application executable. The recommended sandbox location for USB deployment is:
@APPDIR@\Spoon\Sandbox\@TITLE@\@VERSION@
If deploying the virtual application on an intranet file-share, assign the sandbox to a user-accessible sub-folder on a shared network drive. The recommended sandbox location for intranet deployment is:
\\ServerName\ShareName\%USERNAME%\Spoon\Sandbox\@TITLE@\@VERSION@
Do not assign the sandbox to privileged folders, such as @WINDIR@ or @PROGRAMFILES@.  The virtual application will not run correctly if the Spoon engine is unable to write to the sandbox location at runtime.
You can reference environment variables within the sandbox location by enclosing the variable between percent signs: %VARIABLE%.
Sandbox Location Variables
In addition to the standard root folder variables, the sandbox location can contain the following variables:
@TITLE@: Product title 
@PUBLISHER@:  Product publisher
@VERSION@:  Full version string, in dotted quad format
@WEBSITE@:  Publisher website 
@BUILDTIME@: Virtual application build time, in a format similar to 2008.02.01T08.00.
With the exception of the @BUILDTIME@ variable (set automatically), these variables are based on the values specified in the Properties section of Settings.

## Process Configuration Options ##
Spoon IDE has several options to control the startup of primary and child processes. You can access these options by selecting Settings and then choosing the Process Configuration tab.
Command Line Arguments
Command line arguments specified by the user are passed to the virtual application startup executable by default. You can override and specify a fixed set of command line arguments to pass to the startup executable. For example, you can specify Java virtual machine behavior.
Complete the following steps to specify a command-line:
Select the Settings button
Select the Process Configuration tab
Enter the command-line arguments in the Command Line textbox.  
Note: These arguments do not override any arguments specified by the end-user. 
Working Directory
Working Directory determines the active directory at the time of process launch.
Use Startup File Directory sets the working directory to the directory of the virtual application startup file. In the case of a jukeboxed application, the working directory is set to the directory of the startup file specified on the jukebox command line.
Use Current Directory sets the working directory to the directory from which the virtual application is launched.
Use Specified Path enables you to specify a working directory. This specification can include environment and well-known root folder variables.
The working directory is set to the directory of the startup file by default.
Application Type
Windows applications can run in either the GUI or console-mode subsystems. If you select an executable startup file, Spoon IDE automatically configures the virtual application to run in the same subsystem as the startup file. If you select a non-executable startup file, you must manually override the application type. Most applications execute in the GUI subsystem.
To override the application type, select the mode from the Application Type menu in the Process Configuration section of the Settings panel. The Inherit mode sets the application type based on the type of the startup file.
Target Architecture
Target Architecture matches the structure of the virtual environment to the desired host process architecture.
x86:  Use this option for applications that were packaged using the snapshot process on x86 systems. This option maps the Program Files directory to C:\Program Files on x86 systems or to C:\Program Files (x86) on x64 systems. .NET applications compiled to target any CPU architecture always run as 32-bit applications.
x64:  Use this option for applications that were packaged using the snapshot process on x64 systems. This option maps the Program Files directory to C:\Program Files on x64 systems. The Program Files (x86) directory is mapped to C:\Program Files on x86 systems and C:\Program Files (x86) on x64 systems. .NET applications compiled to target any CPU architecture run as 32-bit applications on x86 systems and 64-bit applications on x64 systems.
Any CPU:  This option maps the Program Files directory to C:\Program Files on x86 systems and C:\Program Files on x64 systems. .NET applications compiled to target any CPU architecture run as 32-bit applications on x86 systems and 64-bit applications on x64 systems.  Use this option to place a .NET application that is compiled to target any CPU architecture in the Program Files folder.
Target Architecture is automatically captured during the snapshot process and generally should not be altered for applications packaged through the snapshot process.
Environment Variables
Some applications depend on the presence of Windows environment variables. Spoon IDE enables virtualization of environment variables to support these applications.
Complete the following steps to add or modify virtual environment variables:
Select Environment Variables. This displays the Environment Variables dialog. 
Enter environment variable names and values.
Press Enter to commit the value to the environment variable list.
Most virtual environment variables overwrite any environment variables defined in the host environment. However, PATH and PATHEXT environment variables always merge with the corresponding host environment variables.
Environment variables are automatically captured and merged during the snapshot delta process.
Virtual Services
Windows services are specialized applications that run in the background. They are typically responsible for providing system services such as database services, network traffic handling, web request processing, and other server functionality. Many applications install and require specific services in order to function properly. Spoon IDE fully supports virtualization of certain Windows services. 
Select the Virtual Services button to view and modify virtual service settings. This displays the Virtual Services dialog, which contains the following fields: 
The Name field specifies the internal name of the virtual service. For example, the Windows web server would use the name w3svc.
The Friendly Name field specifies the full display name of the service displayed to end-users. For example, the Windows web server friendly name is World Wide Web Publishing Service.
The Command Line field specifies the full command line (including the service executable name and any parameters) used to launch the service.
The Auto Start flag indicates whether a virtual service starts automatically or manually.
The Keep Alive flag indicates whether the virtual service process terminates automatically when the primary application executable terminates, or whether the service (and the host virtual application executable) continues to run until the service terminates itself.
Service installation and settings are captured automatically during the snapshot process. The primary exception occurs with virtualized applications intended to run as background worker services (for example, virtualized web servers); in this case, it is often required to enable the Keep Alive option.
SVMs
You can specify additional SVM layers for applications, in the case of updates or patches.
The first field is the SVM Search field. Here users can enter the complete path to where multiple SVMs are located using a wildcard. An example of using a wildcard in the search field is @APPDIR@\patches\*.svm. This is similar to what is passed to /XLayerPath using the command line approach.
In the second field users can also specify required SVMs. In this case, the wildcard is removed and a specific file is referenced. An example of this format is  @APPDIR@\VirtualizationDependencies.svm. If the file is not found during application launch, an error will be reported.
All methods allow the use of the @VARIABLE@ format.
Multiple SVMs may be specified after the XLayerSearchPattern attribute in a semi-colon delimited list. SVMs specified first in the list will take precedence over SVMs specified later in the list. If multiple SVMs are specified in one search pattern through the use of the ' * ' wildcard, the SVMs are applied in reverse-alphabetical priority. For example, items in MSOffice_002.svm would have higher priority than items in MSOffice_001.svm.
Child processes
Some applications create new child processes while they run. Depending on the virtual application context, you can create such child processes within the virtual application, or in the host operating system.
Child processes include processes created to service COM local server requests.
Note: Child processes created outside of the virtual application cannot access virtualized filesystem or registry contents. These processes can access or modify host operating system contents, even if otherwise forbidden by the virtual application configuration.
Child processes are created within the virtual application by default. To manually create child processes outside of the virtual application, uncheck the Spawn child process within virtualized environment option.
COM servers are created outside the virtual environment by default to allow COM communication between native applications and virtual applications. To create COM servers within the virtual environment, check the Spawn COM servers within virtualized environment option.
You can determine exceptions to the child process virtualization behavior using the Child Process Exception List... Process names listed in the child process exception list behave opposite to the master child process virtualization setting. To edit the child process exception list, select the Child Process Exception List... button. Process names will match without including the filename extension.
Read-only Virtual Environments
You can use Spoon IDE to prevent users from modifying the virtual environment, including the virtual filesystem and registry. To prevent modifications to the virtual environment, check the Virtual environment is read-only box.
Automatic Sandbox Reset
You can configure the sandbox to reset automatically upon application shutdown. This ensures that any changes made to an application's settings are reverted when the application closes.
To enable the automatic sandbox reset feature, check the Delete sandbox on application shutdown box.
Shutdown Process Tree On Root Process Exit
The Shutdown process tree on root process exit option enables the shutdown of all child processes when the root process exits.
Note: The startup file is the root process by default. If a virtual service is specified in the application configuration file and is set to auto-start when the application is launched, the virtual service acts as the root process in the process tree.
Compress Payload
Both the application profiling and streaming processes require that packages be built uncompressed. To build applications without compression, leave the Compress payload option unchecked.
Startup Executable Optimization
The Enable startup executable Optimization option launches the startup executable within the initial virtual machine process. This prevents the creation of a separate application process and can be incompatible with some applications.
Spoon Command-line Arguments
Spoon supports command-line arguments of the /X[arg] form, which modify virtual application behavior at run-time. In rare instances, these arguments may conflict with command-line arguments designed for use by the virtualized application. To disable processing of these arguments, uncheck the Enable Spoon command-line arguments box.
Window Class Isolation
The Enable window class isolation option prevents viewing window classes that are registered by external processes. You can use this to prevent interaction between virtualized and non-virtualized versions of the same program when the application checks for existing class registrations.
Enhanced DEP Compatibility for Legacy Applications
The Enhanced DEP compatibility for legacy applications option enables compatibility for systems with Data Execution Protection (DEP) enabled. Use this configuration for virtual applications running on Windows 2003.
Enhanced DRM Compatibility
The Enhanced DRM compatibility option enables additional compatibility with common DRM systems, such as Armadillo.
Trace Process Starts in Debug Output
The Trace process starts in debug output option sends a notification to OutputDebugString whenever a new process is started within the virtual environment. This notification is in XML format and comes as a basic information description. It can be monitored with any debugging tool. You can also monitor the notification by a parent process within the virtual environment if a child process is being debugged.
Force Read-share Files
The Force read-share files option forces any file opened within the virtual environment to open with the READ_SHARE flag. Use this option to  resolve compatibility issues caused by sharing violations.
Always Launch Child Processes as Current User
Child processes launched by the virtual machine have reduced privileges by default. Enable the Always launch child processes as current user option to provide child processes with the same level of privileges as the virtual machine root process.
Emulate Elevated Security Privileges
The Emulate elevated security privileges option forces an application to run as if it has elevated security privileges, even if the application does not. Enabling this option eliminates UAC security prompts for elevation and subsequent application crashes.

