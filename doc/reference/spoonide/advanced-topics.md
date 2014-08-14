# Advanced Topics #

## Customize the Spoon Virtual Application Studio Interface ##
In this section you will learn about the different Spoon Virtual Application Studio interface customization options. You can find all of these options listed in the Options menu.
Proxy Settings
Spoon Virtual Application Studio uses the Internet to check for product updates and download update packages. If your computer is located behind a firewall, you might need a proxy server. Spoon Virtual Application Studio uses the default Internet settings configured on the host machine. However, it might be necessary for you to manually configure the proxy server settings.
Complete the following steps to manually configure proxy settings:
Select Proxy settings from the Options menu. 
Provide the proxy server address, the server port and authentication type.
Select Bypass proxy server for local addresses to bypass the proxy server when accessing resources located on the local network. Contact your network administrator for assistance configuring proxy settings.
Automatically detect associated runtimes and components
Spoon Virtual Application Studio scans the virtual filesystem at build time and verifies that the current configuration includes all available runtimes and components. This ensures maximum virtual application reliability.
If you wish to disable this scan, uncheck Automatically detect associated runtimes and components in the Options menu.
Play sound on build completion
Spoon Virtual Application Studio plays a short sound to when the virtual application build completes. To disable this sound, uncheck Play Sound on Build Completion in the Options menu.
Copy new files into the Files folder
When files are added into the virtual application configuration, they can optionally be added to the Files directory. This can be helpful for portability of the build files. However, this may not be desirable for software developers doing automated builds where each build should reference the original source location.

## Quick Snapshot Mode ##

Spoon Virtual Application Studio uses a "quick" snapshot algorithm which attempts to minimize the amount of time spent scanning the host system device. Sometimes, but rarely, use of this mode can result in an improperly configured virtual application. Use of quick snapshot mode can also increase the size of the virtual application configuration contents. Perform snapshots using the quick snapshot mode. Disabling quick snapshot mode significantly increases the amount of time required to complete the virtual application configuration process.
To disable quick snapshot mode, uncheck Quick snapshot mode in the Options menu.
Note: before and after snapshots must be taken using the same snapshot algorithm. Loading a saved snapshot image causes Spoon Virtual Application Studio to automatically configure the snapshot mode to be consistent with the algorithm used during the saved snapshot capture.

## Well-known Root Folder Variables ##

The Spoon engine remaps well-known root folders, such as My Documents and Program Files, based on the host operating system at runtime. This ensures (for example) that a virtualized My Documents folder will be mapped to \User\USER NAME\Documents when running on Microsoft Windows Vista and Windows 7 or \Documents and Settings\USER NAME\My Documents when running on Microsoft Windows 2000 and Windows XP.
Configurations are constructed using snapshots or in the graphical user interface. When manually modifying the configuration, the following well-known root folder variables may be used to configure virtual filesystem locations. Root folder variables are case sensitive. The following is a complete list of root folder variables recognized by Studio and the corresponding folder name displayed in the filesystem graphical user interface, followed by a brief description of the root folder.
@APPDIR@ (Application Directory): Folder where the virtual application executable resides.
@WINDIR@ (Windows): The operating system installation location root as in c:\windows.
@SYSDRIVE@ (System Drive): The root folder of the drive containing the operating system installation as in c:\.
@PROGRAMFILES@ (Program Files): The Program Files folder.
@PROGRAMFILESX86@ (Program Files (x86)): The Program Files folder for 32 bit applications on a 64 bit platform.
@PROGRAMFILESCOMMON@ (Program Files\Common): The Program Files\Common Files folder.
@PROGRAMFILESCOMMONX86@ (Program Files (x86)\Common): The Program Files\Common Files folder for 32 bit applications on a 64 bit platform.
@SYSTEM@ (System Drive\Windows\System32): The Windows System32 folder.
@SYSWOW64@ (Windows\SysWOW64): The Windows folder that manages compatibility with 32 bit applications on a 64 bit platform.
@APPDATALOCAL@ (Current User Directory\Local Application Data): The folder that serves as a common repository for application-specific data used by the current, non-roaming user.
@APPDATA@ (Current User Directory\Application Data): The folder that serves as a common repository for application-specific data for the current roaming user.
@STARTUP@ (Current User Directory\Start Menu\Programs\Startup): The folder containing the current user's startup items.
@PROGRAMS@ (Current User Directory\Start Menu\Programs): The folder containing the user's program groups.
@STARTMENU@ (Current User Directory\Start Menu): The folder containing the user's Start Menu contents.
@DESKTOP@ (Current User Directory\Desktop): The current user's Desktop folder.
@TEMPLATES@ (Current User Directory\Templates): The folder that serves as a common repository for the current user's document templates.
@FAVORITES@ (Current User Directory\Favorites): The current user's Favorites folder.
@DOCUMENTS@ (Current User Directory\My Documents): The current user's My Documents folder.
@MUSIC@ (Current User Directory\My Music): The current user's My Music folder.
@PICTURES@ (Current User Directory\My Pictures): The current user's My Pictures folder.
@PROFILE@ (Current User Directory): The folder that stores the current user's profile data.
@APPDATACOMMON@ (All Users Directory\Application Data): The folder that serves as a common repository for application-specific data shared by all users.
@STARTUPCOMMON@ (All Users Directory\Start Menu\Programs\Startup): The folder containing startup items for all users.
@PROGRAMSCOMMON@ (All Users Directory\Start Menu\Programs): The folder containing components shared across applications.
@STARTMENUCOMMON@ (All Users Directory\Start Menu): The folder containing the Start Menu contents for all users.
@DESKTOPCOMMON@ (All Users Directory\Desktop): The shared Desktop folder.
@TEMPLATESCOMMON@ (All Users Directory\Templates): The folder that serves as a common repository for shared document templates.
@FAVORITESCOMMON@ (All Users Directory\Favorites): The shared Favorites folder.
@DOCUMENTSCOMMON@ (All Users Directory\Documents): The shared Documents folder.
@MUSICCOMMON@ (All Users Directory\Music): The shared Music folder.
@PICTURESCOMMON@ (All Users Directory\Pictures): The shared Pictures folder.
@PROFILECOMMON@ (All Users Directory): The folder that stores shared profile data.

## Building From the Command Line ##

The command-line version of Spoon Virtual Application Studio is called XStudio.exe and can be found in the Spoon Virtual Application Studio installation directory. 
Command
Usage
Description
<path to XAPPL configuration file>	/l <path to license file> [/o <path to output>] [/component] [/d] [/compressed] [/uncompressed] [/deletesandbox] [/v <version>] [/startupfile <virtual path to file>]	
Builds the virtual application based on the application configuration file.
/l - Path the the license file. The license file needs to be stored in Unicode format.
/o - Path to the output file. This will override the setting in the XAPPL configuration file.
/component - Sets the Project Type to Component resulting in an SVM output rather than EXE output. 
/d - Enables the Generate diagnostic-mode executable setting.
/compressed - Enables the Compress payload setting.
/uncompressed - Disables the Compress payload setting. 
/deletesandbox - Enables the Delete sandbox on application shutdown setting.
/v - Sets the Version of the output exe.
/startupfile - Sets the Startup File of the virtual application. 
/before
/beforepath <path to where snapshot file is saved>	
Performs a before snapshot and saves the snapshot to the specified folder.
/beforepath - Path to the where the snapshot file is saved.
/after
/beforepath <path to where snapshot is saved> /o <path to where XAPPL configuration file is saved>
Performs an after snapshot using the specified before snapshot path.
/beforepath - Path to the before snapshot file.
/o - Path to where the XAPPL configuration file is saved.
/import
/i <path to the configuration file to be imported> /o <path to where XAPPL configuration file is saved>	
Import MSI, AXT, or ThinApp configurations.
/i - Path to the configuration file to import.
/o - Path to where the XAPPL configuration file is saved.
Note: Configuration files that are generated from the command-line using the /after flag do not have an output file specified in the XAPPL configuration file. When using scripting to do snapshots, it may be necessary to apply changes to the generated XAPPL file, either manually or programmatically.
Note: If running XStudio displays the error, "<SandboxCollision> is missing from the string table", it is because the XStudio application cannot be run while Spoon Virtual Application Studio is running. Spoon Virtual Application Studio must be closed before running XStudio via the command line.


## Import Configurations From External Tools ##

Spoon Virtual Application Studio enables configuration from certain external application virtualization tools to automatically convert to Spoon Virtual Application Studio configurations. Supported external configurations include MSI setup packages, ThinApp configurations, and Novell AXT snapshots.
Complete the following steps to import a configuration from an external tool:
Select the Start Menu control menu (or press Alt-F).
Select Import Configuration. This displays the configuration import wizard. 
Select Browse. 
Select Next.
Follow the step-by-step instructions in the wizard to complete the import process.
Note: Some applications require additional configuration following MSI import. Such applications must be imported using the snapshot capture method.
Importing ThinApp Settings 
Supported features imported from ThinApp configurations include File System, Registry, Startup Files, Diagnostic Tracing, Windows Services, Output File, Sandbox Path, Child Process Exceptions, MSI Metadata, MSI Shortcuts, Environment Variables, Command-line Arguments, and the FileList > ExcludePattern. The table below details the mapping of ThinApp settings to Spoon Studio settings.
Refer to the appropriate section under Get Started With Spoon Virtual Application Studio, Customize Virtual Applications or Build MSI Setup Packages for details on the Spoon Studio settings. 
ThinApp Configuration Setting
Spoon Studio Setting
DisableTracing	Diagnostic Mode Executable
DirectoryIsolationMode	Default Filesystem Isolation
RegistryIsolationMode 	Defaul Registry Isolation
AutoStartServices	Virtual Services > Auto Start
AutoShutdownServices	Virtual Services > Keep Alive
OutDir 	Output File
SandboxName	Sandbox Location
SandboxPath	Sandbox Location
ChildProcessEnvironmentDefault 	Spawn Child Processes in the Virtual Environment
ChildProcessEnvironmentExceptions	Child Process Exception List
MSIFilename	MSI > Output Location
MSIManufacturer	MSI > Company Name
MSIProductVersion	MSI > Product Version
MSIDefaultInstallAllUsers	MSI > All Users
MSIInstallDirectory	MSI > Application Folder
MSIProductCode	MSI > Product Name
MSIUpgradeCode	MSI > Upgrade
StartupFiles	Startup FIle (Multiple)
EnvironmentVariables	Environment Variables
MSIShortcuts	Shortcuts
CommandLines	Command-line Arguments
DirectoryIsolationMode	Directory Isolation Mode
ExcludePatterns	File > Hide Isolation Mode


## Run Native Applications in Virtual Environments ##
Configuring Startup Files
Spoon Virtual Application Studio enables natively installed applications to launch in virtual sandboxed environments. This is ideal when natively installed application utilize resources contained in a virtual package. For example, a user virtualizing a plugin for Microsoft Outlook could want enable a local version of Microsoft Outlook to run in the same virtual sandbox as the plugin. This is accomplished by setting the natively installed application as the startup file (or one of the startup files).
Complete the following steps to enable a natively installed application to launch in a virtual environment:
In the Virtual Application tab, select Multiple.
In the File column, enter the local path of the natively installed application.
Check Auto Start to automatically run the natively installed application when the virtual application launches.
Select OK.
Now your virtual application and natively installed applications will interact in the same virtual environment.
The following is a sample startup file path for Microsoft Word:
@PROGRAMFILES@\Microsoft Office\Office12\WINWORD.exe
If Auto Start is enabled, Microsoft Word launches with the virtual application in the same virtual environment.
Using Command-line Arguments
You can use the command-line argument /XShellEx, as described in Modifying Virtualization Behavior at Run-time, to specify a natively installed application to run in the virtual environment. For example:
virtualapp.exe /XShellEx=c:\system32\cmd.exe
This results in an instance of the command console running within the virtual environment, specified by virtualapp.exe.

## Modify Virtualization Behavior at Runtime ##
Virtualization behavior is specified in the virtual application configuration using the Spoon Studio interface. However, it is possible to override these settings at application run-time.
Command-line Arguments
Settings enabled via command-line will supersede those specified in the application configuration.
Example command-line with arguments added: VirtualApp.exe /XSandboxPath="C:\MySandbox" /XEnable=Diagnostics;ChildProcAsUser
Flag
Behavior
/XEnv=VariableName=Value
Specifies additional environment variables. Multiple /XEnv arguments can add additional environment variables.
/XLayerPath=LayerPath
Adds the given SVM into the virtual environment. Multiple /XLayerPath arguments can add additional virtual layers. Refer to Specify Additional SVMs for a Virtual Application for more information.
/XSandboxPath=SandboxPath
Specifies the path for the application sandbox. Example: app.exe /XSandboxPath=c:\users\me\desktop\sandbox.
/XShellEx=Command
Specifies a shell execute command to launch from within the virtual application environment. This option overrides any startup files specified in the virtual application configuration. Only one /XShellEx argument can be specified. Example: app.exe /XShellEx=c:\system32\cmd.exe.
/XShellExVerb=CommandVerb
Specifies the verb to use in conjunction with the XShellEx command. The default verb is OPEN. Example: app.exe /XShellExVerb=edit.
/XLogPath=LogPath
Specifies the destination path for generated log files (only applies to executables built in diagnostic-mode). This path can include a custom file name pattern. Example: app.exe /XLogPath=c:\logs\mylog*.log.
/XSpawnVmExceptions=ProcessExceptions
Accepts a semi-colon delimited list of processes add to the child process exception list (refer to the Child processes section of Process Configuration Options for more information). Example: app.exe /XSpawnVmExceptions=notepad.exe.
/XRegRoot=RegistryCacheRoot
Specifies an override to the runtime-registry-cache portion of the sandbox. Example: app.exe /XRegRoot=@HKCU@\Software\ACME\RegCache.
/XEnable and /XDisable
Enables or disables specific process configuration options. These options include:
ChildProcAsUser
DeleteSandbox
DEPCompat
Diagnostics
DRMCompat
ExeOptimization
IndicateElevated
IndicateVirtualization
IsolateWindowClasses
NotifyProcStarts
ReadOnly
ReadShare
ShutdownProctree
SpawnComServers
SpawnVM
SuppressCollisionCheck
All of these options correspond to specific options in the Process Configuration tab described in Process Configuration Options. For example: /XEnable=SpawnVm;DEPCompat. You can specify Diagnostics to enable or disable diagnostic logs in executables.
/XCollisionCheck=FALSE
Disables detection of multiple apps attempting to use the same sandbox at the same time. This should only be used to support legacy behavior.
Environment Variables
There is one environment variable that can be used to enable diagnostic logging.
Environment Variable
Value
Behavior
__VMDIAGNOSTICS
t	
Enables diagnostic logging.

## Capture Updates to an Application via Snapshot ##

Virtual application updates can be captured within Spoon Virtual Application Studio via snapshots.
Complete the following steps to capture an update via snapshots:
Install the native version of the application on a clean machine.
Select Capture Before.
Install necessary updates to the native application.
Select Capture and Diff to create the after snapshot. This captures the deltas between the original and updated versions.
Set the Project Type to Component, then select Build to create the SVM.
This process only captures changes between the original executable and installed updates. You can then apply the resulting SVM to the original virtual package.
For more information on updating virtual applications using SVMs, refer to Create and Use Shared Virtual Components and Specify Additional SVMs for a Virtual Application.

## Specify Additional SVMs for a Virtual Application ##

When you have updates or patches you can use Spoon Virtual Application Studio to specify additional SVMs for applications. Spoon Virtual Application Studio provides the following three mechanisms to accomplish this:
The first mechanism is via the command line using the /XLayerPath= syntax. This syntax takes a path with optional wildcards to additional SVMs to load. 
An example of a specified SVM path using full path:
virtual-app.exe /XLayerPath=@APPDIR@\patches.svm
An example of specifying SVMs from multiple locations:
virtual-app.exe /XLayerPath=@APPDIR@\patches.svm /XLayerPath=@APPDIR@\officepatches.svm
An example of specifying SVMs on a network share:
virtual-app.exe /XLayerPath=\\network\share\patches.svm
An example using Microsoft Office with wildcard:
MSOffice.exe /XLayerPath=c:\Patches\MSOffice\*.svm
This performs a wildcard match finding any files, such as MSOffice_001.svm, in the c:\Patches directory. 
Note: SVMs are applied in reverse-alphabetical priority. For example, items in MSOffice_002.svm have higher priority than items in MSOffice_001.svm.
The second mechanism is a XAPPL file specified way to load additional SVMs. It is via the <XLayers> portion of the XAPPL file and has the following elements:
Attribute or Element
Description
xlayerSearchPattern
Attribute to provide the default search pattern, similar to what would be passed to /XLayerPath.
RequiredXLayer
Sub-elements specifying which SVM is loaded. Otherwise an error is reported.
The following is an example XAPPL configuration:
<XLayers xlayerSearchPattern="@APPDIR@\StudioDependencies.svm">
  <RequiredXLayer name="StudioDependencies.svm" />
</XLayers>
The third mechanism is available in the Spoon Virtual Application Studio interface. To access this method:
Click on the Settings button
Click on the Process Configuration tab
Click on the SVM button
The first field is the SVM Search field.  Here users can enter the complete path to where multiple SVMs are located using a wildcard.  An example of using a wildcard in the search field is @APPDIR@\patches\*.svm.  This is similar to what is passed to /XLayerPath using the command line approach.  
In the second field users can also specify required SVMs.  In this case, the wildcard is removed and a specific file is referenced.  An example of this format is @APPDIR@\StudioDependencies.svm.  If the file is not found during application launch, an error will be reported.
All methods allow the use of the @VARIABLE@ format.
Multiple SVMs may be specified after the XLayerSearchPattern attribute in a semi-colon delimited list. SVMs specified first in the list will take precedence over SVMs specified later in the list. If multiple SVMs are specified in one search pattern through the use of the '*' wildcard, the SVMs are applied in reverse-alphabetical priority. For example, items in MSOffice_002.svm would have higher priority than items in MSOffice_001.svm.
Note: Newer versions of Spoon Virtual Application Studio use SVMs instead of XLayer files. You must rebuild old XLayer files as SVMs; currently there is no supported conversion utility. SVMs function in the same way as XLayer files in that they auto-integrate with a virtual executable when placed in a patch matching the XLayerSearchPattern.

## Merge Platforms ##

The Merge Platforms feature enables you to combine virtual application configurations snapshot on multiple operating systems (Microsoft Windows XP, Microsoft Vista, etc.) into a single configuration. The virtualization engine applies configuration options appropriate for the different operating systems at runtime.
Tip: The most common platform merge scenario is a merge of snapshots taken on Microsoft Windows XP and Microsoft Windows Vista. Some newer applications use operating system features specific to Microsoft Windows Vista.
Complete the following steps to merge configurations from multiple platforms:
Select Merge Platforms from the Advanced tab.
Select Browse and open the appropriate configuration for each different operating system.
For operating systems without a configuration, choose which configuration it should use by using the Inherit option.
When all configurations are or set, navigate to Browse under Merge Settings, choose where to save the merged configuration, and select Merge.
Complete the following steps to display or edit a specific operating system from a merged configuration:
Open the merged configuration.
From the Advanced tab, select the Display drop-down menu.
Choose the operating system to display or edit. 
The Filesystem and Registry panels only display settings specific to the selected operating system. You cannot edit configurations inherited from other platforms; to edit inherited configurations, you must select and edit the master configuration.
Complete the following steps to change the inheritance of an operating system in a merged configuration:
Open a merged configuration.
From the Advanced tab, select the Display drop-down menu.
Select the operating system to modify.
Select the platform from which to inherit using the Inherit drop-down menu.


## Create Application Streaming Models ##

The Streaming option on the Advanced tab enables you to profile and build streaming models for a virtual application.
The Profile feature generates transcripts, or profiles, which are used to create a streaming model for the virtual application. Selecting Profile launches the application and creates a single-transcript file based on observed user behavior from that run. Create multiple transcripts before creating a streaming model. Using multiple transcripts enables the streaming system to consider different use cases for the application. Create at least one transcript for each operating system.
Note: Only uncompressed virtual applications can be profiled and streamed. Compression is automatically disabled during the model build process.
Complete the following steps to profile virtual applications:
Build the virtual application.
Select Profile from the Advanced tab.
Select the application to profile.
Choose the output location for transcripts and select OK.
After the virtual application launches use the application for approximately one minute, as if you were a typical end-user.
Close the application. After the application terminates, the transcript is created in the selected output location.
Create additional transcripts as needed.
Once the necessary profiles are created the streaming model is ready to build. The model build process uses transcripts and Connection Speed parameters to compute a model of execution. After the model build process is complete, the streaming files are written to the selected output folder. The Connection Speed setting optimizes delivery of application content to the end-user.
Complete the following steps to create a streaming model:
Select the Connection Speed (1.5Mbps is recommended for most scenarios).
Select Build Model.
Select the profiled application.
Choose the folder where the transcripts are located and select OK.
Choose the folder where the streaming model will be created and select OK.


## Application Expiration ##
The Expiration feature enables you to set expiration dates for virtual applications. 
Complete the following steps to set a virtual application to expire after a specific number of days:
Select Expiration.
Check the Disallow execution after number of days box.
Select the number of days it will take to expire after initial execution.
Choose the Time Source the virtual application will use to validate the date.
Complete the following steps to set a virtual application to expire after a certain date:
Select Expiration.
Check the Disallow execution after date box.
Select virtual application expiration date.
Choose the Time Source the virtual application will use to validate the date.
For all expiration modes, the System clock setting uses the host system clock to validate the date. The Web server clock setting validates the date against an HTTPS-based web server. Check the Disallow execution if web server is unreachable box to prevent offline application execution.
The Web server clock setting is more secure than the System clock setting; it prevents circumvention of the expiration mechanism by modifying the system clock. This setting will also prevent applications from executing on devices which cannot connect to the time server source.
You can set an Expiration warning to notify users when the virtual application is about to expire. The message will display each time the virtual application is executed within the specified threshold.


## Apply Virtual Application Configurations to the Host Device ##

Spoon Virtual Application Studio enables you to configure the virtual application to the host system. Apply the virtual application configuration to the host system when creating SVM updates for virtual applications.
Complete the following steps to apply the virtual application configuration to the host system:
Select Apply Configuration in the Start Menu.
Select Yes to acknowledge that the Apply Configuration process cannot be undone.
Note: The Apply Configuration feature is not intended as an installation process for virtual applications.
For example, complete the following steps to create an SVM update to the Firefox virtual application template:
Use the Configuration Wizard to create a Firefox virtual application.
When the Firefox configuration is loaded, run Apply Configuration.
Open a new virtual application configuration.
Capture a before snapshot.
Open Firefox, select Help>Check for updates, and apply updates.
Capture an after snapshot.
Build the captured updates as an SVM.
Execute the built SVM on top of the original virtual Firefox browser and verify that the updates are applied. 


## Enable Shared Object Isolation ##
Spoon Virtual Application Studio enables you to isolate shared objects in memory. Certain applications refer to objects in memory by a specific name, which can cause runtime errors. Shared object isolation creates unique names for memory objects at runtime; this enables a virtual application and a natively installed version of the same application to run side-by-side without conflict.
Shared object isolation can only be enabled by manually editing the XAPPL file. A global setting to enables/disables named object isolation. The global setting controls whether named objects are renamed by default. There are exceptions to the global setting which take regular expression values. Any shared object having a name matching an exception is given the opposite behavior of the default. The regular expressions can also be replaced by a replacement value. The first match of the regular expression in a named object will be replaced by the replacement value.
The following example, OBJECTN (of the form OBJECT1, OBJECT2, ... OBJECT99), includes named objects used by a virtual application that conflict with identically-named objects used by a natively installed application. Common named objects include mutexes and named pipes. The second example, Test Value.* (of the form "Test Value 1612"), will be changed to simply "Test Value", but also appended with a unique signature for the application.
Complete the following steps to enable shared object isolation for OBJECTN in a virtual application:
Open the XAPPL file in a text editor.
Replace the <NamedObjectIsolation ../> element with the following example:
<NamedObjectIsolation enabled="False">
   <Exception regex="OBJECT\d+" />
   <Exception regex="Test Value.*" replacement="Test Value" />
</NamedObjectIsolation>
Reload the XAPPL file in Spoon Virtual Application Studio and build the application.
The resulting virtual application should have shared object isolation enabled. Multiple objects in memory can be isolated simultaneously.

## Virtual DNS ##
Spoon Virtual Application Studio supports adding virtual DNS entries. Applications such as web-browsers use DNS to resolve domain names, like www.spoon.net, to IP addresses, in either IPv4 or IPv6 format.
The virtual DNS settings are configured manually in the XAPPL configuration file. When editing the virtual DNS a domain name is mapped to its target, which could be:
Another domain name
An IPv4 address
An IPv6 address (supported XP and forward)
The following is an example of how to configure the virtual DNS:
Open the XAPPL file in a text editor.
Replace the <Dns /> element with the following:
<Dns>
   <Entry name="www.spoon.net" redirect="localhost"/>
   <Entry name="www.xenocode.com" redirect="www.spoon.net"/>
   <Entry name="acme.com" redirect="192.168.10.1" />
   <Entry name="acmeipv6.com" redirect="fe80::d51f:d3ef:bd07:a16f%10" />
</Dns>
Reload the XAPPL file in Spoon Virtual Application Studio and build the application.
Test the application to verify that the DNS settings are working.

## Example Startup Shim DLL ##
Below is an example of a startup shim that would be put in place to verify if an external service or application was already running before the virtual application could be launched. Click here to download the the sample project.
Note: This example is a 32 bit DLL. If the application is a 64 bit application, the shim should be compiled as 64 bit.
Setup
Use Visual Studio 2010 (or install Visual C++ 2010 Express for free)
Create Project
Create a new project and select Visual C++ > General > Empty Project and give it a name (SpoonShim)
Edit project properties
Right click on the Project and select Properties
Set Configurations to All Configurations
Go to Configuration Properties > General > Project Defaults > Configuration Type and select Dynamic Library (.dll)
Go to Configuration Properties > C/C++ > Code Generation > Runtime Library and select Multi-threaded (/MT)
If you need to debug, set this to Multi-threaded Debug (/MTd) for the Debug configuration
Click OK
Create Header Files
Right Click on Header Files and click Add > New Item
Select Header File (.h) and give it a name (SpoonShim)
// SpoonShim.h
#ifdef SPOONSHIM_EXPORTS
 
#define SPOONSHIM_API __declspec(dllexport)
 
#else
 
#define SPOONSHIM_API __declspec(dllimport)
 
#endif BOOL __stdcall OnInitialize(LPCWSTR pwcsInitializationToken);
Right Click on Header Files and click Add > New Item
Select Header File (.h) and name it stdafx
// stdafx.h : include file for standard system include files,
// or project specific include files that are used frequently,
// but are changed infrequently
 
#pragma once
Create a Module Definition File
Right Click on Header Files and click Add > New Item
Select any file type, but name the file Exports.def
Note that the DLL name is in the code after LIBRARY this should correspond to the name of the DLL (SpoonShim)
LIBRARY "SpoonShim"
 
EXPORTS
OnInitialize
Edit project properties (again)
Right click on the Project and select Properties
Set Configurations to All Configurations
Go to Configuration Properties > Linker > Input > Module Definition File and type in Exports.def
Click OK
Create main C++ file
Right click Source Files and click Add > New Item
Select C++ File (.cpp) and give it a name (SpoonShim)
// This is the main DLL file.
 
#include "stdafx.h"
 
#define WIN32_LEAN_AND_MEAN
#include <windows.h>
 
#include "SpoonShim.h"
 
#include <ShellAPI.h>
 
 
/// Main dll entry point
BOOL APIENTRY DllMain( HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved)
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
     
    return TRUE;
}
/// Function called when the virtual app is being initialized
BOOL __stdcall OnInitialize(LPCWSTR pwcsInitializationToken)
{
    BOOL fLaunchApp = FALSE;
 
    /// perform operation to check if app should launch
 
    if (!fLaunchApp)
    /// let the user know that the application is unable to launch
    MessageBox(NULL, "Unable to launch the application.  Please check with your administrator.", NULL, NULL);
 
    /// return whether to launch the app
    return fLaunchApp;
}
Build and test
Now you can build the DLL and test it by selecting the DLL in Spoon Virtual Application Studio under Settings > Startup Settings > Startup shim DLL.


## XAPPL File Format ##
Overview
XAPPLfile is an XML representation of virtual application configuration settings.
All paths in the XAPPL file are relative to where it resides. For example, the source attribute of a file element begins with ".\Files". The "." directory is the path where the XAPPL file should reside; this ensures that Spoon Virtual Application Studio can locate the physical source files during the build process.
XAPPL files must adhere to XML syntax rules. If there are syntax errors in the XAPPL file, Spoon Virtual Application Studio cannot load the file.
XAPPL Configuration Elements and Attributes
The following table contains the different elements/attributes and their descriptions:
Element/Attribute
Description
OutputLocation
Path to the folder where the virtual application executable is created. This can be a local path, a UNC path, or a mapped drive.
OutputFile
File name of the virtual application executable.
Project-Type
Denotes whether configuration is for a virtual application (Application) or an SVM (Component).
Licensing
Contains information about the license used to build the virtual application.
Output
The DiagnosticMode attribute denotes when the application output should log diagnostic information (True) or not (False). If true, the virtual application will create diagnostic logs in the directory where it was executed from. 
The SourcePackage attribute is not used.
MSI
All sub-elements contain settings pertaining to the configuration of the MSI setup file:
The outputMsiPath attribute indicates the location where the setup MSI is built.
The title attribute indicates the value of the MSI title property.
The subject attribute indicates the value of the MSI subject property.
The keywords attribute indicates the value of the MSI keywords property.
The productName attribute indicates the value of the MSI product name property.
The productVersion attribute indicates the value of the MSI product version property.
The manufacturer attribute indicates the value of the MSI manufacturer property.
The productLanguage attribute indicates the value of the MSI product language property.
The author attribute indicates the value of the MSI author property.
The description attribute indicates the value of the MSI description property.
The manufacturerUrl attribute indicates the value of the MSI manufacturer URL property.
The autoBuild attribute denotes whether the MSI should build when the virtual application build completes successfully (True) or not (False).
The isolatePerUser attribute denotes whether the MSI setup should be installed on a per-user basis (True) or installed for all users (False). When installing per-user, the install root path is Application Data. When installing for all users, the install root path is Program Files.
The applicationFolder attribute indicates the subfolders into which the virtual application should be installed (Company Name\Product Name).
The upgradePreviousVersion attribute denotes whether the setup should maintain the same Upgrade code when it builds (True) or change the Upgrade code for each build (False). This allows the setup to upgrade previous versions when it is installed, or to exist side by side.
The productCode attribute indicates the value of MSI product code property.
The upgradeCode attribute indicates the value of MSI upgrade code property.
The componentId attribute indicates the value of the MSI component id property.
Packages
All sub-elements contain settings pertaining to the configuration of the packages included in the virtual application.
Clr
The .NET Clr runtime element and all sub-elements contain settings pertaining to the configuration of the virtual .NET Framework runtime.
Direct X
The DirectX element and all sub-elements contain settings pertaining to the configuration of the virtual DirectX runtime.
Java
All sub-elements contain settings pertaining to the configuration of the virtual java runtime.
RunTime
The name attribute indicates the name of the java runtime (Java).  
The platform attribute indicates the platform that the java runtime is designed for (x86). 
The version attribute indicates the version of the java runtime. The available versions are Java 5 (1.5.0.140) and Java 6 (1.6.0.30).
Settings
The startupType attribute denotes whether to use the jar file (JAR) or class path (Class) command line parameters for java.exe to launch the application. 
The startup attribute indicates the jar file path or class name depending on the StartupType. 
The classpath attribute indicates the path to the class files of the Java runtime. 
The options attribute denotes any additional command line parameter.
Package
The name attribute indicates the name of the component or runtime. 
The platform attribute indicates the platforms that the component or runtime is supported on. The following are the only available values:
Any platform (Any)
x86 platform (x86) 
The version attribute indicates the version of the component or runtime.
Virtualization Settings
All sub-elements contain settings pertaining to the configuration of the virtual operating system.
The suppressBranding attribute controls the branding pop-up that is displayed (False), or not displayed (True) in the lower right-hand corner during application startup.
The isolateWindowClasses attribute is used to isolate windows classes, as registered via the Windows ::RegisterClass or ::RegisterClassEx APIs. For example, this allows a virtualized Firefox instance to run while a non-virtualized instance is running.
The readOnlyVirtualization attribute denotes whether the virtual application has the ability to modify virtual files and registry settings (False) or not (True). Setting this attribute to True will prevent modification to the virtual filesystem and virtual registry.
The disableXenocodeCommandLine attribute controls the ability to execute (False) any file from within the virtual filesystem.
The subsystem attribute indicates the application output type. It can be inherited from the startup file (Inherit) or set explicitly to be a Windows application (GUI) or console application (Console). If Inherit is set, but the startup file is either not in the virtual filesystem or not an executable, then the output will be a Windows application.
The ie6Emulation attribute denotes a special mode required for the Internet Explorer 6 template (True). For all other apps, this should be disabled (False).
The sandboxPath attribute indicates the base path of the application sandbox 
@APPDATALOCAL@\Spoon\Sandbox\@TITLE\@\@VERSION@. The workingDirectory attribute defines what directory the application will run in.
The compressPayload attribute controls whether the output executable will be compressed (True) or not (False).
The trimUACManifest attribute removes items from the manifest that may require elevation (True).
The enableDRMCompatibility attribute ensures compatibility (True) with applications protected by software formerly known as "Armadillo" and other DRM software.
The deleteSandbox attribute will cause the sandbox to be reset automatically when the virtual application is shutdown (True).
The shutdownProcessTree attribute will cause the all child processes spawned within the virtual environment to be shutdown when the root process exits. By default, the root process is specified by setting the startup file.
The exeOptimization attribute will attempt to launch the startup executable with the initial virtual machine process, preventing the creation of a separate application process (True).
The enhancedDEPCompatibility attribute provides compatibility for systems with Data Execution Protection enabled (True). This setting is used primarily for virtual applications running on Windows 2003.
The notifyProcessStarts attribute causes a notification to be sent as a debugging output string whenever a new process is started within the virtual environment (True).
The forceReadShareFiles attribute forces any file opened by any process within the virtual environment to do so with the READ_SHARE flag set (True).
The launchChildProcsAsUser attribute causes all child processes to be provided with the same level of privileges as the virtual machine root process (True).
The forceIndicateRunningElevated attribute forces the application to run as if it has elevated security privileges (True).
The suppressPopups attribute will prevent an error dialog popup if the virtual application encounters a fatal startup error, and will cause the application to exit silently (True).
The minSandboxSpaceAvail attribute allows specifying a size in MBs. If set, the virtual application will enforce at startup that the sandbox volume has at least this much space available to the user. A value of -1 disables this enforcement.
The suppressSandboxCollisionCheck attribute will enable or disable the ability to detect when multiple applications are trying to access the same sandbox at the same time. This attribute is set to "False" by default.
XLayers
Additional SVM's that will be loaded when the application starts
The xlayerSearchPattern attribute to provide the default search pattern, similar to what would be passed to /XLayerPath
The RequiredXLayer sub-element specifies which SVMs are required to be loaded. Otherwise an error is reported. Further details are located in the Specify Additional SVMs for a Virtual Application section.
NamedObjectIsolation
Allows users to isolate select objects in the application from the host machine that may use the same name. Details on how to use this feature can be found in the Enable Shared Object Isolation section.
Dns
Allows users to add explicit dns mappings which are reflected within the virtual environment. Details on how to use this feature can be found in the Virtual DNS section.
WorkingDirectory
Specifies which directory the virtual application will execute from.
The option sub-element can be set to "StartupFileDirectory", "CurrentDirectory" or "specifiedDirectory".
The specifiedDirectory sub-element lists the specified path selected for the application.
ChildProcessVirtualization
The spawnExternalComServers attribute controls whether the virtual application launches ComServers in the virtual environment (True) or the external environment (False).
The spawnVm attribute denotes whether the spawned external applications are spawned inside the virtual environment (True) or outside the virtual environment (False).
ChildProcessException
The name attribute indicates the name of the executable file (extension included) to except from the effects of the spawnVm attribute.
CustomMetadata
All sub-elements contain settings pertaining to the configuration of the individual custom metadata items.
CustomMetadataItem
The property attribute indicates the name of the custom metadata item.
The value attribute indicates the value of the custom metadata item.
StandardMetadata
All sub-elements contain settings pertaining to the configuration of the individual standard metadata items.
StandardMetadataIte
The property attribute indicates the name of the standard metadata item.  The following are the available standard metadata:
Product Title (Title)
Publisher (Publisher)
Description (Description)
Website (Website)
Product Version (Version)
SplashImage
The path attribute indicates the source path to the splash image displayed at application startup. 
The transparency attribute indicates the color in the splash image that should be made transparent when the image is displayed (E.g. Magenta).
StartupFiles
All sub-elements contain configuration pertaining to the individual startup files.
StartupFile
The node attribute indicates the path of the startup file. 
The tag attribute indicates the command line trigger used to specify this entry as the startup to use. 
The commandLine attribute indicates the command line arguments to pass to the startup file. 
The default attribute denotes whether this entry is executed automatically when no tag is specified (True) or not (False).
StartupShims
All sub-elements contain configuration pertaining to the individual startup shims.
StartupShim
The startup shim is a virtualized binary that is invoked prior to the startup file. Startup shims are used to perform customized licensing checks or other initialization tasks.
The shimDllPath attribute indicates the path to the virtual shim DLL implementation. This field is required.
The paramOnInitialize attribute indicates a string to be passed to the shim OnInitialize function.
The startup shim signature is typedef BOOL (__stdcall *FnOnInititialize) LPCWSTR pwcsInitilizationToken). The return value indicates whether virtual machine execution should proceed.
Layers
All sub-elements are individual virtual layers.
Layer
The Layer element and all sub-elements contain settings pertaining to the configuration of this layer of the virtual operating system.
The name attribute indicates the name of the layer. The default layer (Default) is the only layer for whom the name matters. All other layer names are purely informational.
Condition
The variable attribute indicates the host system setting that will be evaluated. The operating system version (OS) is the only available option. 
The operator attribute indicates the Boolean operation that will be used to evaluate the host system. The available Boolean operations are:
greater than or equal to (GREATEREQUAL)
greater than (GREATER)
equal to (EQUAL)
not equal to (NOTEQUAL)
less than (LESS)
less than or equal to (LESSEQUAL) 
The value attribute indicates the value against which the host system will be evaluated, using the Boolean operation. The available values in ascending order are:  
Windows 2000 (Win2k) 
Windows XP (WinXP) 
Windows 2003 (Win2k3) 
Windows Vista (Vista)
Filesystem
All sub-elements contain settings pertaining to the configuration of the virtual filesystem.
Directory
All sub-elements contain settings pertaining to the configuration of this directory of the virtual filesystem.
The rootType attribute indicates the root system folder that this virtual folder is mapped to on the host filesystem. Directory elements with the rootType attribute are always directly beneath the Filesystem element.  The following are the available rootTypevalues:
Application Directory (Application)
Windows\System32 (System)
Windows (OS)
System Drive Root Directory (SysDrive)
Program Files\Common (AllProgramsCommon)
Program Files (AllPrograms)
Current User - Start Menu (StartMenu)
Current User - Start Menu\Programs (Programs)
Current User - Start Menu\Programs\Startup (Startup)
Current User - Application Data (AppData)
Current User - LocalSetting\Application Data (AppDataLocal)
Current User - Desktop (Desktop)
Current User - Templates (Templates)
Current User - Favorites (Favorites)
Current User - Music (Music)
Current User - Pictures (Pictures)
Current User - My Documents (Documents)
%PROFILE%  (Profile)
All Users - Start Menu (StartMenuCommon)
All Users - Start Menu\Programs (ProgramsCommon)
All Users - Start Menu\Programs\Startup (StartupCommon)
All Users - Application Data (AppDataCommon)
All Users - Desktop (DesktopCommon)
All Users - Templates (TemplatesCommon)
All Users - Favorites (FavoritesCommon)
All Users - Music (MusicCommon)
All Users - Pictures (PicturesCommon)
All Users - My Documents (DocumentsCommon)
%ALLUSERSPROFILE% (ProfileCommon)
The isolationattribute indicates the isolation setting of the virtual folder. The available values are:
Full isolation (Full)
WriteCopy isolation (WriteCopy)
Merge isolation (Merge)
The name attribute indicates the name of the virtual directory.
The hide attribute denotes whether the directory is marked as hidden (True) or visible (False).
File
The name attribute indicates the name of the file. 
The hide attribute denotes whether the file is marked as hidden (True) or visible (False). 
The source attribute indicates the source path to the file
Registry
All sub-elements contain settings pertaining to the configuration of the virtual registry.
Key
All sub-elements contain settings pertaining to the configuration of this key of the virtual filesystem.
The rootType attribute indicates the root system folder that this virtual folder is mapped to on the host filesystem. Key elements with the rootType attribute are always directly beneath the Registry element. The following are the available rootTypevalues:
HKEY_CLASSES (ClassesRoot)
HKEY_CURRENT_USER (CurrentUser)
HKEY_LOCAL_MACHINE (CurrentUser)
HKEY_USERS (Users)
The name attribute indicates the name of the key.
The namePathInformationTuples indicates that there is a path in the name or value of the registry item. There are 3 comma delimited integers for each path found in the name/value.1. Flags that indicate the state of the path (valid combinations: 0x0, 0x1, 0x2, 0x4, 0x5, 0x6) 
0x1 - All Uppercase 
0x2 - All Lowercase 
0x4 - Uses Short Path Names 
2. Start index of the path 
3. Length of the path
The isolationattribute indicates the isolation setting of the virtual folder. The available values are:
Full isolation (Full)
Merge isolation (Merge)
Value
The name attribute indicates the name of the value. 
The type attribute indicates the type of the value. The available values are:
REG_SZ and REG_EXPAND_SZ (String)
REG_DWORD (DWORD)
REG_QWORD (QWORD)
REB_BINARY (Binary)
REG_MULTI_STRING (StringArray) 
The namePathInformationTuples indicates that there is a path in the name or value of the registry item. There are 3 comma delimited integers for each path found in the name/value. 
Flags that indicate the state of the path (valid combinations: 0x0, 0x1, 0x2, 0x4, 0x5, 0x6) 
0x1 - All Uppercase 
0x2 - All Lowercase 
0x4 - Uses Short Path Names
Start index of the path
Length of the path 
The value attribute indicates the value of the value. This is true for all types, except StringArray, which contains the String sub-element.
Environment Variables
The name attribute indicates the name of the environment variable. 
The value attribute indicates the value of the environment variable.
Services
The name attribute indicates the name of the windows service. 
The autoStart attribute denotes whether the windows service starts when the virtual application starts (True) or not (False). 
The commandLine attribute indicates the startup command line of the windows service. 
The friendlyName attribute indicates the friendly name of the windows service. 
The description attribute indicates the description of the windows service. 
The objectName attribute indicates the account under which the windows service ran when not virtualized. 
The keepAlive attribute denotes whether the windows service should continue running after the startup application has closed (True) or not (False). 
The start attribute indicates the value of the Start DWORD value in the Windows Services registry key. 
The type attribute indicates the value of the Type DWORD value in the Windows Services registry key. 
The errorControl attribute indicates the value of the ErrorControl DWORD value in the Services registry key.
Shortcuts
All sub-elements contain settings pertaining to the configuration of the MSI shortcuts.
Folder
All sub-elements contain settings pertaining to the configuration of the MSI shortcuts in this folder. 
The name attribute indicates the name of the folder. The two top level folders represent the Desktop (Desktop) and the Programs menu on the Start menu (Programs Menu).
Shortcut
The name attribute indicates the name of the shortcut. 
The targetPath attribute indicates the path of the StartupFile that is the target of the shortcut. 
The targetParameter attribute indicates the Trigger or Tag of the StartupFile that is the target of the shortcut. 
The arguments attribute indicates the arguments passed to the target of the shortcut at runtime. 
The showCmd attribute denotes whether the application should start in a maximized (3), minimized (7) or regular (1) window state. 
The description attribute indicates the description of the shortcut.
IconResource
The IconResource sub-element contains an identifier of the icon that is used for the Shortcut.
ProgIds
All sub-elements contain settings pertaining to the configuration of the ProgId.
The name attribute indicates the name of the ProgId.
The description attribute indicates the description of the ProgId.
IconResource
The IconResource sub-element contains an identifier of the icon that is used for the file association.
HarvestSettings
The HarvestSettings element only appears in Desktop Scan configurations, or recipes. This section tells the configuration which files, folders, and registry keys to add or delete from the build.
Extension
All sub-elements contain settings pertaining to the configuration of the file extensions for the ProgId.
The extension attribute indicates the file extension that is associated with the ProgId.
The mimeType attribute indicates the MIME type of all files with the extension.
DefaultPrograms
For the DefaultPrograms element, specify the following parameters:
name – Name of the application (e.g. Thunderbird, Firefox).
friendlyName – Friendly name (e.g. Thunderbird, Firefox).
description – Description (e.g. Mail Client, Web Browser).
clientType – Type of Default Program (e.g. Browser, Mail, StartMenuInternet). This can be found under Current user root/Software/Clients or Local machine root/Software/Clients.
hidden – This should be set to false.
default – This should be set to true.   
  
The sub-elements of the DefaultPrograms are:
IconResource – This is the program icon and can be copied from the ProgId section of the XAPPL.
data – This contains data to render the icon.
Extension – These are the file extensions that use this DefaulProgram (e.g. .eml, .html, .htm).
name – This is the extension (e.g. .eml, .html, .htm).
progId – This is a reference to which ProgId to use to handle this type of file extension.
Protocol – These are the protocols that use the DefaultProgram (e.g. mailto, http, https).
name – This is the name of the protocol (e.g. mailto, http, https, news).
progId – This is a reference to the ProgId that will handle this protocol.
clientType – This is the name of the client under Current user root/Software/Clients or Local machine root/Software/Clients.
SimpleMapi – This is specific to the mail clientType.
mapiDllPath – Path to the DLL to use for MAPI for this mail client.
mailClientPath – Path to the main exe of the application.
Verb
All sub-elements contain settings pertaining to the configuration of the Verb for the file extension.
The title attribute indicates the title of the verb.
The verb attribute indicates the verb value.
The arguments attribute indicates the arguments passed to the target of the verb at runtime.
The default attribute denotes whether this verb is the default verb (True) or not (False).

## Snapshot Settings ##

Description
Snapshot settings are defined within a file called SnapshotSettings.xml. This file is auto-created upon first snapshot under the [AppDataLocal]\Spoon\Spoon Virtual Application Studio\ folder. The file contains two major sections: Filesystem and Registry
Under each, one can specify the following settings: Root paths, Include paths, Exclude paths, AllOrNothing roots, and Isolation overrides.
Child elements
Root: Allows the specifying of snapshot roots. Possible values include the standard special folder values, such as @PROGRAMFILES@ and @SYSTEM@. NOTE: these roots should be specified in order from deepest to shallowest in a filesystem.
Include: Allows specifying a force-include path which overrides any exclude paths. Useful when you want exceptions to a wildcard exclude path.
Exclude: Allows specifying a path which should be excluded from snapshot. Wildcards may be used in the last element, such as @PROGRAMFILES@\Acme\Cache_*
AllOrNothing: Used to indicate a root under which new or modified sub-folders/keys are added in an all-or-nothing fashion. Useful under certain areas of the registry for example where COM is configured. 
Isolation: Used to override isolation settings for a given path and below. Use the isolation attribute with possible values: Full, Merge, or WriteCopy.
All elements take a path attribute to specify the path for the given setting.
Abbreviated Sample Settings File
<?xml version="1.0" encoding="utf-8"?>
<SnapshotSettings>
  <!--Filesystem snapshot settings-->
  <Filesystem>
 
    <!--Set of snapshot starting-point root folders.  Removing any of these
        will cause it to be removed from the set of starting points.  But
        note that sometimes we can still arrive at a deeper root by way of
        a shallower root, unless the path to the deeper root is excluded
        at some point.
         
        NOTE: Should order these from deepest to shallowest-->
    <Root path="@PROGRAMFILESCOMMON@" />
    <Root path="@PROGRAMFILES@" />
    <Root path="@PROGRAMFILESCOMMONX86@" />
    <Root path="@PROGRAMFILESX86@" />
    <Root path="@SYSTEM@" />
    <Root path="@SYSWOW64@" />
    <Root path="@WINDIR@" />
    <Root path="@SYSDRIVE@" />
 
    <Exclude path="@SYSDRIVE@\Pagefile.sys" />
    <Exclude path="@SYSDRIVE@\Boot" />
    <Exclude path="@SYSDRIVE@\$Recycle.Bin" />
    <Exclude path="@APPDATA@\Microsoft\Windows NT" />
    <Exclude path="@APPDATA@\Microsoft\Internet Explorer" />
    <Exclude path="@PROFILE@\AppData" />
    <Exclude path="@APPDATALOCAL@\Microsoft\Internet Explorer" />
    <Exclude path="@APPDATACOMMON@\Microsoft\Windows Defender" />
    <Exclude path="@WINDIR@\WinSXS\ManifestCache" />
    <Exclude path="@SYSTEM@\vpc-s3.cfg" />
    <Exclude path="@SYSTEM@\CatRoot2" />
    <Exclude path="@SYSTEM@\NtmsData" />
 
    <Isolation path="@SYSTEM@\mui" isolation="Merge" />
    <Isolation path="@SYSWOW64@\mui" isolation="Merge" />
    <Isolation path="@DOCUMENTS@" isolation="Merge" />
    <Isolation path="@PICTURES@" isolation="Merge" />
    <Isolation path="@MUSIC@" isolation="Merge" />
 
  </Filesystem>
 
  <!--Registry snapshot settings-->
  <Registry>
 
    <!--Set of snapshot starting point root folders.  Removing any of these
        will cause it to be removed from the set of starting points.  But
        note that sometimes we can still arrive at a deeper root by way of
        a shallower root, unless the path to the deeper root is excluded
        at some point.-->
    <Root path="@HKCU@" />
    <Root path="@HKLM@" />
 
    <!--Excluded HKLM subkeys by default, we will select what we want
        NOTE:  wow64If="true" (the default) causes both path flavors to be added as in:
            HKEY_LOCAL_MACHINE\Software\Classes\AppId and
            HKEY_LOCAL_MACHINE\Software\Classes\Wow6432Node\AppId -->
    <Exclude path="HKEY_LOCAL_MACHINE\*" />
    <Include path="HKEY_LOCAL_MACHINE\Software" wow64If="false" />
    <Include path="HKEY_LOCAL_MACHINE\System" wow64If="false" />
    <Exclude path="HKEY_LOCAL_MACHINE\Software\Classes\Local Settings" />
    <Exclude path="HKEY_LOCAL_MACHINE\Software\Microsoft\Rpc" />
    <Exclude path="HKEY_LOCAL_MACHINE\Software\Microsoft\DrWatson" />
    <Exclude path="HKEY_LOCAL_MACHINE\System\*" />
    <Include path="HKEY_LOCAL_MACHINE\System\CurrentControlSet" />
    <Exclude path="HKEY_LOCAL_MACHINE\System\CurrentControlSet\*"/>
    <Include path="HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services" />
 
    <!--AllOrNothing mean that any immediate subkey of the given root is added in
        all-or-nothing fashion.  Any add/modify under one of these locations causes the
        entire sub-tree to be added.  One can also configure names for subkey exceptions.
        Setting wow64iIf="True" (the default) will cause both flavors of the path to be added, as
        in: HKEY_LOCAL_MACHINE\Software\Classes\AppId and
            HKEY_LOCAL_MACHINE\Software\Classes\Wow6432Node\AppId -->
    <AllOrNothing path="HKEY_CURRENT_USER\Software\Classes\Applications" />
    <AllOrNothing path="HKEY_LOCAL_MACHINE\Software\Classes\Applications" />
    <AllOrNothing path="HKEY_CURRENT_USER\Software\Classes\AppID" />
    <AllOrNothing path="HKEY_LOCAL_MACHINE\Software\Classes\AppID" />
 
  </Registry>
 
</SnapshotSettings>

## Specifying a Virtual Mapped Drive ##

A virtual mapped drive can be added to your XAPPL file in the FileSystem section. This is not available through the Spoon Studio UI, but can be added manually in a text editor. To do this:
Open the XAPPL file in your text editor of choice
Navigate to the FileSystem section of the XAPPL file
This section is enclosed by the tags <FileSystem> and </FileSystem>
Add your virtual file to the filesystem
See the example, below for a sample code snippet
The @DRIVE_X@ variable in the snippet represents the virtual drive. Any letter can be specified by changing the letter of this variable (for example, if your virtual drive was M:, you would use name="@DRIVE_M@"
The example shown, below, is for adding the virtual file X:\AppData\Settings.txt to the configuration. When added in this way, the virtual mapped drive will not be visible in Windows Explorer or through File browse dialogs, but it will be visible via command window or if teh application does a file lookup using standard Windows APIs.
<Directory rootType="VirtualDrive" name="@DRIVE_X@" isolation="Merge">
    <Directory name="AppData" hide="False" readOnly="False" isolation="Full">
        <File name="Settings.txt" hide="False" readOnly="False" source=".\Files\X_Drive\AppData\Settings.txt" />
    </Directory>
</Directory>
