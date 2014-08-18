# Advanced Topics #

## Customize the Spoon IDE Interface ##
In this section you will learn about the different Spoon IDE interface customization options. You can find all of these options listed in the **Options** menu.

### Proxy Settings ###

Spoon IDE uses the Internet to check for product updates and download update packages. If your computer is located behind a firewall, you might need a proxy server. Spoon IDE uses the default Internet settings configured on the host machine. However, it might be necessary for you to manually configure the proxy server settings.

Complete the following steps to manually configure proxy settings:

1. Select **Proxy settings** from the **Options** menu. 
2. Provide the proxy server address, the server port and authentication type.
3. Select **Bypass proxy server for local addresses** to bypass the proxy server when accessing resources located on the local network. Contact your network administrator for assistance configuring proxy settings.

### Automatically detect associated runtimes and components ###

Spoon IDE scans the virtual filesystem at build time and verifies that the current configuration includes all available runtimes and components. This ensures maximum virtual application reliability.

If you wish to disable this scan, uncheck **Automatically detect associated runtimes and components** in the Options menu.

### Play sound on build completion ###

Spoon IDE plays a short sound to when the virtual application build completes. To disable this sound, uncheck **Play Sound on Build Completion** in the **Options** menu.

### Copy new files into the Files folder ###

When files are added into the virtual application configuration, they can optionally be added to the Files directory. This can be helpful for portability of the build files. However, this may not be desirable for software developers doing automated builds where each build should reference the original source location.

## Quick Snapshot Mode ##

Spoon IDE uses a "quick" snapshot algorithm which attempts to minimize the amount of time spent scanning the host system device. Sometimes, but rarely, use of this mode can result in an improperly configured virtual application. Use of quick snapshot mode can also increase the size of the virtual application configuration contents. Perform snapshots using the quick snapshot mode. Disabling quick snapshot mode significantly increases the amount of time required to complete the virtual application configuration process.

To disable quick snapshot mode, uncheck **Quick snapshot mode** in the **Options** menu.

**Note**: before and after snapshots must be taken using the same snapshot algorithm. Loading a saved snapshot image causes Spoon IDE to automatically configure the snapshot mode to be consistent with the algorithm used during the saved snapshot capture.

## Well-known Root Folder Variables ##

The Spoon engine remaps well-known root folders, such as My Documents and Program Files, based on the host operating system at runtime. This ensures (for example) that a virtualized My Documents folder will be mapped to \User\USER NAME\Documents when running on Microsoft Windows Vista and Windows 7 or \Documents and Settings\USER NAME\My Documents when running on Microsoft Windows 2000 and Windows XP.

Configurations are constructed using snapshots or in the graphical user interface. When manually modifying the configuration, the following well-known root folder variables may be used to configure virtual filesystem locations. Root folder variables are case sensitive. The following is a complete list of root folder variables recognized by Studio and the corresponding folder name displayed in the filesystem graphical user interface, followed by a brief description of the root folder.

- @APPDIR@ (Application Directory): Folder where the virtual application executable resides.
- @WINDIR@ (Windows): The operating system installation location root as in c:\windows.
- @SYSDRIVE@ (System Drive): The root folder of the drive containing the operating system installation as in c:\.
- @PROGRAMFILES@ (Program Files): The Program Files folder.
- @PROGRAMFILESX86@ (Program Files (x86)): The Program Files folder for 32 bit applications on a 64 bit platform.
- @PROGRAMFILESCOMMON@ (Program Files\Common): The Program Files\Common Files folder.
- @PROGRAMFILESCOMMONX86@ (Program Files (x86)\Common): The Program Files\Common Files folder for 32 bit applications on a 64 bit platform.
- @SYSTEM@ (System Drive\Windows\System32): The Windows System32 folder.
- @SYSWOW64@ (Windows\SysWOW64): The Windows folder that manages compatibility with 32 bit applications on a 64 bit platform.
- @APPDATALOCAL@ (Current User Directory\Local Application Data): The folder that serves as a common repository for application-specific data used by the current, non-roaming user.
- @APPDATA@ (Current User Directory\Application Data): The folder that serves as a common repository for application-specific data for the current roaming user.
- @STARTUP@ (Current User Directory\Start Menu\Programs\Startup): The folder containing the current user's startup items.
- @PROGRAMS@ (Current User Directory\Start Menu\Programs): The folder containing the user's program groups.
- @STARTMENU@ (Current User Directory\Start Menu): The folder containing the user's Start Menu contents.
- @DESKTOP@ (Current User Directory\Desktop): The current user's Desktop folder.
- @TEMPLATES@ (Current User Directory\Templates): The folder that serves as a common repository for the current user's document templates.
- @FAVORITES@ (Current User Directory\Favorites): The current user's Favorites folder.
- @DOCUMENTS@ (Current User Directory\My Documents): The current user's My Documents folder.
- @MUSIC@ (Current User Directory\My Music): The current user's My Music folder.
- @PICTURES@ (Current User Directory\My Pictures): The current user's My Pictures folder.
- @PROFILE@ (Current User Directory): The folder that stores the current user's profile data.
- @APPDATACOMMON@ (All Users Directory\Application Data): The folder that serves as a common repository for application-specific data shared by all users.
- @STARTUPCOMMON@ (All Users Directory\Start Menu\Programs\Startup): The folder containing startup items for all users.
- @PROGRAMSCOMMON@ (All Users Directory\Start Menu\Programs): The folder containing components shared across applications.
- @STARTMENUCOMMON@ (All Users Directory\Start Menu): The folder containing the Start Menu contents for all users.
- @DESKTOPCOMMON@ (All Users Directory\Desktop): The shared Desktop folder.
- @TEMPLATESCOMMON@ (All Users Directory\Templates): The folder that serves as a common repository for shared document templates.
- @FAVORITESCOMMON@ (All Users Directory\Favorites): The shared Favorites folder.
- @DOCUMENTSCOMMON@ (All Users Directory\Documents): The shared Documents folder.
- @MUSICCOMMON@ (All Users Directory\Music): The shared Music folder.
- @PICTURESCOMMON@ (All Users Directory\Pictures): The shared Pictures folder.
- @PROFILECOMMON@ (All Users Directory): The folder that stores shared profile data.

## Building From the Command Line ##

The command-line version of Spoon IDE is called `XStudio.exe` and can be found in the Spoon IDE installation directory. 

<table border="1" cellpadding="2" cellspacing="2">
	<tr>
		<th>Command</th>
		<th>Usage</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>&lt;path to XAPPL configuration file></td>
		<td>/l &lt;path to license file> [/o &lt;path to output>] [/component] [/d] [/compressed] [/uncompressed] [/deletesandbox] [/v &lt;version>] [/startupfile &lt;virtual path to file>]</td>
		<td>Builds the virtual application based on the application configuration file.<br/><br/>/l - Path the the license file. The license file needs to be stored in Unicode format.<br/><br/>/o - Path to the output file. This will override the setting in the XAPPL configuration file.<br/><br/>/component - Sets the Project Type to Component resulting in an SVM output rather than EXE output.<br/><br/>/d - Enables the Generate diagnostic-mode executable setting.<br/><br/>/compressed - Enables the Compress payload setting.<br/><br/>/uncompressed - Disables the Compress payload setting. <br/><br/>/deletesandbox - Enables the Delete sandbox on application shutdown setting.<br/><br/>/v - Sets the Version of the output exe.<br/><br/>/startupfile - Sets the Startup File of the virtual application.</td>
	</tr>
	<tr>
		<td><b>/before</b></td>
		<td>/beforepath &lt;path to where snapshot file is saved></td>
		<td>Performs a before snapshot and saves the snapshot to the specified folder. <br/><br/>/beforepath - Path to the where the snapshot file is saved.</td>
	</tr>
	<tr>
		<td><b>/after</b></td>
		<td>/beforepath &lt;path to where snapshot is saved> /o &lt;path to where XAPPL configuration file is saved></td>
		<td nowrap>Performs an after snapshot using the specified before snapshot path.<br/><br/>/beforepath - Path to the before snapshot file.<br/><br/>/o - Path to where the XAPPL configuration file is saved.</td>
	</tr>
	<tr>
		<td>/import</td>
		<td>/i &lt;path to the configuration file to be imported> /o &lt;path to where XAPPL configuration file is saved></td>
		<td>Import MSI, AXT, or ThinApp configurations.<br/><br/>/i - Path to the configuration file to import.<br/><br/>/o - Path to where the XAPPL configuration file is saved.</td>
	</tr>
</table>

**Note**: Configuration files that are generated from the command-line using the **/after** flag do not have an output file specified in the **XAPPL** configuration file. When using scripting to do snapshots, it may be necessary to apply changes to the generated **XAPPL** file, either manually or programmatically.

**Note**: If running XStudio displays the error, "&lt;SandboxCollision> is missing from the string table", it is because the XStudio application cannot be run while Spoon IDE is running. Spoon IDE must be closed before running XStudio via the command line.


## Import Configurations From External Tools ##

Spoon IDE enables configuration from certain external application virtualization tools to automatically convert to Spoon IDE configurations. Supported external configurations include MSI setup packages, ThinApp configurations, and Novell AXT snapshots.

Complete the following steps to import a configuration from an external tool:

1. Select the Start Menu control menu (or press Alt-F).
2. Select Import Configuration. This displays the configuration import wizard. 
3. Select Browse. 
4. Select Next.
5. Follow the step-by-step instructions in the wizard to complete the import process.

**Note**: Some applications require additional configuration following MSI import. Such applications must be imported using the snapshot capture method.

### Importing ThinApp Settings  ###

Supported features imported from ThinApp configurations include File System, Registry, Startup Files, Diagnostic Tracing, Windows Services, Output File, Sandbox Path, Child Process Exceptions, MSI Metadata, MSI Shortcuts, Environment Variables, Command-line Arguments, and the FileList > ExcludePattern. The table below details the mapping of ThinApp settings to Spoon Studio settings.

Refer to the appropriate section under [Get Started With Spoon IDE](#get-started-with-spoon-ide), [Customize Virtual Applications](#customize-virtual-applications) or [Build MSI Setup Packages](#build-msi-setup-packages) for details on the Spoon Studio settings.

<table border="1" cellpadding="2" cellspacing="2">
	<tr>
		<th>ThinApp Configuration Setting</th>
		<th>Spoon IDE Setting</th>
	</tr>
	<tr>
		<td>DisableTracing</td>
		<td>Diagnostic Mode Executable</td>
	</tr>
	<tr>
		<td>DirectoryIsolationMode</td>
		<td>Default Filesystem Isolation</td>
	</tr>
	<tr>
		<td>RegistryIsolationMode</td>
		<td>Defaul Registry Isolation</td>
	</tr>
	<tr>
		<td>AutoStartServices</td>
		<td>Virtual Services > Auto Start</td>
	</tr>
	<tr>
		<td>AutoShutdownServices</td>
		<td>Virtual Services > Keep Alive</td>
	</tr>
	<tr>
		<td>OutDir</td>
		<td>Output File</td>
	</tr>
	<tr>
		<td>SandboxName</td>
		<td>Sandbox Location</td>
	</tr>
	<tr>
		<td>SandboxPath</td>
		<td>Sandbox Location</td>
	</tr>
	<tr>
		<td>ChildProcessEnvironmentDefault</td>
		<td>Spawn Child Processes in the Virtual Environment</td>
	</tr>
	<tr>
		<td>ChildProcessEnvironmentExceptions</td>
		<td>Child Process Exception List</td>
	</tr>
	<tr>
		<td>MSIFilename</td>
		<td>MSI > Output Location</td>
	</tr>
	<tr>
		<td>MSIManufacturer</td>
		<td>MSI > Company Name</td>
	</tr>
	<tr>
		<td>MSIProductVersion</td>
		<td>MSI > Product Version</td>
	</tr>
	<tr>
		<td>MSIDefaultInstallAllUsers</td>
		<td>MSI > All Users</td>
	</tr>
	<tr>
		<td>MSIInstallDirectory</td>
		<td>MSI > Application Folder</td>
	</tr>
	<tr>
		<td>MSIProductCode</td>
		<td>MSI > Product Name</td>
	</tr>
	<tr>
		<td>MSIUpgradeCode</td>
		<td>MSI > Upgrade</td>
	</tr>
	<tr>
		<td>StartupFiles</td>
		<td>Startup FIle (Multiple)</td>
	</tr>
	<tr>
		<td>EnvironmentVariables</td>
		<td>Environment Variables</td>
	</tr>
	<tr>
		<td>MSIShortcuts</td>
		<td>Shortcuts</td>
	</tr>
	<tr>
		<td>CommandLines</td>
		<td>Command-line Arguments</td>
	</tr>
	<tr>
		<td>DirectoryIsolationMode</td>
		<td>Directory Isolation Mode</td>
	</tr>
	<tr>
		<td>ExcludePatterns</td>
		<td>File > Hide Isolation Mode</td>
	</tr>
</table>

## Run Native Applications in Virtual Environments ##

### Configuring Startup Files ###

Spoon IDE enables natively installed applications to launch in virtual sandboxed environments. This is ideal when natively installed application utilize resources contained in a virtual package. For example, a user virtualizing a plugin for Microsoft Outlook could want enable a local version of Microsoft Outlook to run in the same virtual sandbox as the plugin. This is accomplished by setting the natively installed application as the startup file (or one of the startup files).

Complete the following steps to enable a natively installed application to launch in a virtual environment:

1. In the **Virtual Application** tab, select **Multiple**.
2. In the **File** column, enter the local path of the natively installed application.
3. Check **Auto Start** to automatically run the natively installed application when the virtual application launches.
4. Select OK.

Now your virtual application and natively installed applications will interact in the same virtual environment.
The following is a sample startup file path for Microsoft Word:

    @PROGRAMFILES@\Microsoft Office\Office12\WINWORD.exe

If Auto Start is enabled, Microsoft Word launches with the virtual application in the same virtual environment.

### Using Command-line Arguments ###

You can use the command-line argument /XShellEx, as described in [Modifying Virtualization Behavior at Run-time](#modify-virtualization-behavior-at-run-time), to specify a natively installed application to run in the virtual environment. For example:

    virtualapp.exe /XShellEx=c:\system32\cmd.exe

This results in an instance of the command console running within the virtual environment, specified by virtualapp.exe.

## Modify Virtualization Behavior at Runtime ##
Virtualization behavior is specified in the virtual application configuration using the Spoon Studio interface. However, it is possible to override these settings at application run-time.

### Command-line Arguments ###

Settings enabled via command-line will supersede those specified in the application configuration.

Example command-line with arguments added: 

    VirtualApp.exe /XSandboxPath="C:\MySandbox" /XEnable=Diagnostics;ChildProcAsUser

<table border="1" cellpadding="2" cellspacing="2">
	<tr>
		<th>Flag</th>
		<th>Behavior</th>
	</tr>
	<tr>
		<td>/XEnv=VariableName=Value</td>
		<td>Specifies additional environment variables. Multiple /XEnv arguments can add additional environment variables.</td>
	</tr>
	<tr>
		<td>/XLayerPath=LayerPath</td>
		<td>Adds the given SVM into the virtual environment. Multiple /XLayerPath arguments can add additional virtual layers. Refer to <a href="#specify-additional-svms-for-a-virtual-application">Specify Additional SVMs for a Virtual Application</a> for more information.</td>
	</tr>
	<tr>
		<td>/XSandboxPath=SandboxPath</td>
		<td>Specifies the path for the application sandbox. Example: app.exe /XSandboxPath=c:\users\me\desktop\sandbox.</td>
	</tr>
	<tr>
		<td>/XShellEx=Command</td>
		<td>Specifies a shell execute command to launch from within the virtual application environment. This option overrides any startup files specified in the virtual application configuration. Only one /XShellEx argument can be specified. Example: <pre>app.exe /XShellEx=c:\system32\cmd.exe</pre></td>
	</tr>
	<tr>
		<td>/XShellExVerb=CommandVerb</td>
		<td>Specifies the verb to use in conjunction with the XShellEx command. The default verb is OPEN. Example: <pre>app.exe /XShellExVerb=edit</pre></td>
	</tr>
	<tr>
		<td>/XLogPath=LogPath</td>
		<td>Specifies the destination path for generated log files (only applies to executables built in diagnostic-mode). This path can include a custom file name pattern. Example: <pre>app.exe /XLogPath=c:\logs\mylog*.log</pre></td>
	</tr>
	<tr>
		<td>/XSpawnVmExceptions=ProcessExceptions</td>
		<td>Accepts a semi-colon delimited list of processes add to the child process exception list (refer to the Child processes section of Process Configuration Options for more information). Example: <pre>app.exe /XSpawnVmExceptions=notepad.exe</pre></td>
	</tr>
	<tr>
		<td>/XRegRoot=RegistryCacheRoot</td>
		<td>Specifies an override to the runtime-registry-cache portion of the sandbox. Example: <pre>app.exe /XRegRoot=@HKCU@\Software\ACME\RegCache</pre></td>
	</tr>
	<tr>
		<td>/XEnable and /XDisable</td>
		<td>Enables or disables specific process configuration options. These options include:<ul><li>ChildProcAsUser</li><li>DeleteSandbox</li><li>DEPCompat</li><li>Diagnostics</li><li>DRMCompat</li><li>ExeOptimization</li><li>IndicateElevated</li><li>IndicateVirtualization</li><li>IsolateWindowClasses</li><li>NotifyProcStarts</li><li>ReadOnly</li><li>ReadShare</li><li>ShutdownProctree</li><li>SpawnComServers</li><li>SpawnVM</li><li>SuppressCollisionCheck</li></ul>All of these options correspond to specific options in the Process Configuration tab described in Process Configuration Options. For example: <pre>/XEnable=SpawnVm;DEPCompat</pre> You can specify Diagnostics to enable or disable diagnostic logs in executables.</td>
	</tr>
	<tr>
		<td>/XCollisionCheck=FALSE</td>
		<td>Disables detection of multiple apps attempting to use the same sandbox at the same time. This should only be used to support legacy behavior.</td>
	</tr>
</table>

### Environment Variables ###

There is one environment variable that can be used to enable diagnostic logging.
<table border="1" cellpadding="2" cellspacing="2">
	<tr>
		<th>Environment Variable</th>
		<th>Value</th>
		<th>Behavior</th>
	</tr>
	<tr>
		<td>__VMDIAGNOSTICS</td>
		<td>t</td>
		<td>Enables diagnostic logging.</td>
	</tr>
</table>

## Capture Updates to an Application via Snapshot ##

Virtual application updates can be captured within Spoon IDE via snapshots.

Complete the following steps to capture an update via snapshots:

1. Install the native version of the application on a clean machine.
2. Select **Capture Before**.
3. Install necessary updates to the native application.
4. Select **Capture and Diff** to create the after snapshot. This captures the deltas between the original and updated versions.
5. Set the **Project Type** to **Component**, then select **Build** to create the **SVM**.

This process only captures changes between the original executable and installed updates. You can then apply the resulting **SVM** to the original virtual package.

For more information on updating virtual applications using **SVMs**, refer to [Create and Use Shared Virtual Components](#create-and-use-shared-virtual-components) and [Specify Additional SVMs for a Virtual Application](#specify-additional-svms-for-a-virtual-application).

<a name="specify-additional-svms-for-a-virtual-application"></a>
## Specify Additional SVMs for a Virtual Application ##

When you have updates or patches you can use Spoon IDE to specify additional **SVMs** for applications. Spoon IDE provides the following three mechanisms to accomplish this.

The first mechanism is via the command line using the **/XLayerPath=** syntax. This syntax takes a path with optional wildcards to additional **SVMs** to load. 

An example of a specified **SVM** path using full path:

    virtual-app.exe /XLayerPath=@APPDIR@\patches.svm

An example of specifying **SVMs** from multiple locations:

    virtual-app.exe /XLayerPath=@APPDIR@\patches.svm /XLayerPath=@APPDIR@\officepatches.svm

An example of specifying **SVMs** on a network share:

    virtual-app.exe /XLayerPath=\\network\share\patches.svm

An example using Microsoft Office with wildcard:

    MSOffice.exe /XLayerPath=c:\Patches\MSOffice\*.svm

This performs a wildcard match finding any files, such as `MSOffice_001.svm`, in the `c:\Patches` directory. 

**Note**: **SVMs** are applied in reverse-alphabetical priority. For example, items in `MSOffice_002.svm` have higher priority than items in `MSOffice_001.svm`.

The second mechanism is a XAPPL file specified way to load additional SVMs. It is via the <XLayers> portion of the XAPPL file and has the following elements:

<table border="1" cellpadding="2" cellspacing="2">
	<tr>
		<th>Attribute or Element</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>xlayerSearchPattern</td>
		<td>Attribute to provide the default search pattern, similar to what would be passed to /XLayerPath.</td>
	</tr>
	<tr>
		<td>RequiredXLayer</td>
		<td>Sub-elements specifying which SVM is loaded. Otherwise an error is reported.</td>
	</tr>
</table>

The following is an example XAPPL configuration:
    
    <XLayers xlayerSearchPattern="@APPDIR@\StudioDependencies.svm">
      <RequiredXLayer name="StudioDependencies.svm" />
    </XLayers>
    
The third mechanism is available in the Spoon IDE interface. To access this method:

1. Click on the Settings button
2. Click on the Process Configuration tab
3. Click on the SVM button
 
The first field is the **SVM Search** field.  Here users can enter the complete path to where multiple **SVMs** are located using a wildcard.  An example of using a wildcard in the search field is `@APPDIR@\patches\*.svm`.  This is similar to what is passed to **/XLayerPath** using the command line approach.  

In the second field users can also specify required **SVMs**.  In this case, the wildcard is removed and a specific file is referenced.  An example of this format is `@APPDIR@\StudioDependencies.svm`.  If the file is not found during application launch, an error will be reported.

All methods allow the use of the `@VARIABLE@` format.

Multiple **SVMs** may be specified after the **XLayerSearchPattern** attribute in a semi-colon delimited list. **SVMs** specified first in the list will take precedence over **SVMs** specified later in the list. If multiple **SVMs** are specified in one search pattern through the use of the '*' wildcard, the **SVMs** are applied in reverse-alphabetical priority. For example, items in `MSOffice_002.svm` would have higher priority than items in `MSOffice_001.svm`.

**Note**: Newer versions of Spoon IDE use **SVMs** instead of **XLayer** files. You must rebuild old **XLayer** files as **SVMs**; currently there is no supported conversion utility. **SVMs** function in the same way as **XLayer** files in that they auto-integrate with a virtual executable when placed in a patch matching the **XLayerSearchPattern**.

## Merge Platforms ##

The **Merge Platforms** feature enables you to combine virtual application configurations snapshot on multiple operating systems (Microsoft Windows XP, Microsoft Vista, etc.) into a single configuration. The virtualization engine applies configuration options appropriate for the different operating systems at runtime.

**Tip**: The most common platform merge scenario is a merge of snapshots taken on Microsoft Windows XP and Microsoft Windows Vista. Some newer applications use operating system features specific to Microsoft Windows Vista.

Complete the following steps to merge configurations from multiple platforms:

1. Select **Merge Platforms** from the **Advanced** tab.
2. Select **Browse** and open the appropriate configuration for each different operating system.
3. For operating systems without a configuration, choose which configuration it should use by using the **Inherit** option.
4. When all configurations are or set, navigate to **Browse** under **Merge Settings**, choose where to save the merged configuration, and select **Merge**.

Complete the following steps to display or edit a specific operating system from a merged configuration:

1. Open the merged configuration.
2. From the **Advanced** tab, select the **Display** drop-down menu.
3. Choose the operating system to display or edit.

The **Filesystem** and **Registry** panels only display settings specific to the selected operating system. You cannot edit configurations inherited from other platforms; to edit inherited configurations, you must select and edit the master configuration.

Complete the following steps to change the inheritance of an operating system in a merged configuration:

1. Open a merged configuration.
2. From the **Advanced** tab, select the **Display** drop-down menu.
3. Select the operating system to modify.
4. Select the platform from which to inherit using the **Inherit** drop-down menu.


## Create Application Streaming Models ##

The **Streaming** option on the **Advanced** tab enables you to profile and build streaming models for a virtual application.

The **Profile** feature generates transcripts, or *profiles*, which are used to create a streaming model for the virtual application. Selecting **Profile** launches the application and creates a single-transcript file based on observed user behavior from that run. Create multiple transcripts before creating a streaming model. Using multiple transcripts enables the streaming system to consider different use cases for the application. Create at least one transcript for each operating system.

**Note**: Only uncompressed virtual applications can be profiled and streamed. Compression is automatically disabled during the model build process.

Complete the following steps to profile virtual applications:

1. Build the virtual application. 
2. Select **Profile** from the **Advanced** tab. 
3. Select the application to profile.
4. Choose the output location for transcripts and select OK.
5. After the virtual application launches use the application for approximately one minute, as if you were a typical end-user.
6. Close the application. After the application terminates, the transcript is created in the selected output location.
7. Create additional transcripts as needed.

Once the necessary profiles are created the streaming model is ready to build. The model build process uses transcripts and **Connection Speed** parameters to compute a model of execution. After the model build process is complete, the streaming files are written to the selected output folder. The **Connection Speed** setting optimizes delivery of application content to the end-user.

Complete the following steps to create a streaming model:

1. Select the **Connection Speed** (1.5Mbps is recommended for most scenarios). 
2. Select **Build Model**.
3. Select the profiled application.
4. Choose the folder where the transcripts are located and select **OK**.
5. Choose the folder where the streaming model will be created and select **OK**.


## Application Expiration ##
The **Expiration** feature enables you to set expiration dates for virtual applications. 

Complete the following steps to set a virtual application to expire after a specific number of days:

1. Select **Expiration**.
2. Check the **Disallow execution after number of days** box.
3. Select the number of days it will take to expire after initial execution.
4. Choose the **Time Source** the virtual application will use to validate the date.

Complete the following steps to set a virtual application to expire after a certain date:

1. Select **Expiration**.
2. Check the **Disallow execution after date** box.
3. Select virtual application expiration date.
4. Choose the **Time Source** the virtual application will use to validate the date.

For all expiration modes, the **System clock** setting uses the host system clock to validate the date. The **Web server clock** setting validates the date against an HTTPS-based web server. Check the **Disallow execution if web server is unreachable** box to prevent offline application execution.

The **Web server clock** setting is more secure than the **System clock** setting; it prevents circumvention of the expiration mechanism by modifying the system clock. This setting will also prevent applications from executing on devices which cannot connect to the time server source.

You can set an **Expiration warning** to notify users when the virtual application is about to expire. The message will display each time the virtual application is executed within the specified threshold.


## Apply Virtual Application Configurations to the Host Device ##

Spoon IDE enables you to configure the virtual application to the host system. Apply the virtual application configuration to the host system when creating **SVM** updates for virtual applications.

Complete the following steps to apply the virtual application configuration to the host system:

1. Select **Apply Configuration** in the **Start Menu**.
2. Select **Yes** to acknowledge that the **Apply Configuration** process cannot be undone.

**Note**: The **Apply Configuration** feature is not intended as an installation process for virtual applications.

## Enable Shared Object Isolation ##
Spoon IDE enables you to isolate shared objects in memory. Certain applications refer to objects in memory by a specific name, which can cause runtime errors. Shared object isolation creates unique names for memory objects at runtime; this enables a virtual application and a natively installed version of the same application to run side-by-side without conflict.

Shared object isolation can only be enabled by manually editing the **XAPPL** file. A global setting to enables/disables named object isolation. The global setting controls whether named objects are renamed by default. There are exceptions to the global setting which take regular expression values. Any shared object having a name matching an exception is given the opposite behavior of the default. The regular expressions can also be replaced by a replacement value. The first match of the regular expression in a named object will be replaced by the replacement value.

The following example, *OBJECTN* (of the form OBJECT1, OBJECT2, ... OBJECT99), includes named objects used by a virtual application that conflict with identically-named objects used by a natively installed application. Common named objects include mutexes and named pipes. The second example, Test Value.* (of the form "Test Value 1612"), will be changed to simply "Test Value", but also appended with a unique signature for the application.

Complete the following steps to enable shared object isolation for OBJECTN in a virtual application:

1. Open the XAPPL file in a text editor.
2. Replace the `<NamedObjectIsolation ../>` element with the following example:<pre>
&lt;NamedObjectIsolation enabled="False">
   &lt;Exception regex="OBJECT\d+" />
   &lt;Exception regex="Test Value.*" replacement="Test Value" />
&lt;/NamedObjectIsolation>
</pre>
3. Reload the **XAPPL** file in Spoon IDE and build the application.

The resulting virtual application should have shared object isolation enabled. Multiple objects in memory can be isolated simultaneously.

## Virtual DNS ##
Spoon IDE supports adding virtual DNS entries. Applications such as web-browsers use DNS to resolve domain names, like `www.spoon.net`, to IP addresses, in either IPv4 or IPv6 format.

The virtual DNS settings are configured manually in the **XAPPL** configuration file. When editing the virtual DNS a domain name is mapped to its target, which could be:

- Another domain name
- An IPv4 address
- An IPv6 address (supported XP and forward)

The following is an example of how to configure the virtual DNS:

- Open the **XAPPL** file in a text editor.
- Replace the `<Dns />` element with the following:
<pre>
    &lt;Dns>
       &lt;Entry name="www.spoon.net" redirect="localhost"/>
       &lt;Entry name="www.xenocode.com" redirect="www.spoon.net"/>
       &lt;Entry name="acme.com" redirect="192.168.10.1" />
       &lt;Entry name="acmeipv6.com" redirect="fe80::d51f:d3ef:bd07:a16f%10" />
    &lt;/Dns>
</pre>
- Reload the **XAPPL** file in Spoon IDE and build the application.
- Test the application to verify that the DNS settings are working.

## Example Startup Shim DLL ##
Below is an example of a startup shim that would be put in place to verify if an external service or application was already running before the virtual application could be launched. Click here to download the the sample project.

**Note**: This example is a 32 bit DLL. If the application is a 64 bit application, the shim should be compiled as 64 bit.

### Setup ###
Use Visual Studio 2010 (or install Visual C++ 2010 Express for free)

### Create Project ###

- Create a new project and select Visual C++ > General > Empty Project and give it a name (SpoonShim)
- Edit project properties
- Right click on the Project and select Properties
- Set Configurations to All Configurations
- Go to Configuration Properties > General > Project Defaults > Configuration Type and select Dynamic Library (.dll)
- Go to Configuration Properties > C/C++ > Code Generation > Runtime Library and select Multi-threaded (/MT)
- If you need to debug, set this to Multi-threaded Debug (/MTd) for the Debug configuration
- Click OK

### Create Header Files ###
- Right Click on Header Files and click Add > New Item
- Select Header File (.h) and give it a name (SpoonShim)
<pre>    
    // SpoonShim.h
    #ifdef SPOONSHIM_EXPORTS
     
    #define SPOONSHIM_API __declspec(dllexport)
     
    #else
     
    #define SPOONSHIM_API __declspec(dllimport)
     
    #endif BOOL __stdcall OnInitialize(LPCWSTR pwcsInitializationToken);
</pre>
- Right Click on Header Files and click Add > New Item
- Select Header File (.h) and name it stdafx
<pre>    
    // stdafx.h : include file for standard system include files,
    // or project specific include files that are used frequently,
    // but are changed infrequently

    #pragma once
</pre>    

### Create a Module Definition File ###
- Right Click on Header Files and click Add > New Item
- Select any file type, but name the file Exports.def
- Note that the DLL name is in the code after LIBRARY this should correspond to the name of the DLL (SpoonShim)
<pre>    
LIBRARY "SpoonShim"
 
EXPORTS
OnInitialize
</pre>    

### Edit project properties (again) ###
- Right click on the Project and select Properties
- Set Configurations to All Configurations
- Go to Configuration Properties > Linker > Input > Module Definition File and type in Exports.def
- Click OK

### Create main C++ file ###
- Right click Source Files and click Add > New Item
- Select C++ File (.cpp) and give it a name (SpoonShim)
<pre>    
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
</pre>    

### Build and test ###

Now you can build the DLL and test it by selecting the DLL in Spoon IDE under Settings > Startup Settings > Startup shim DLL.


## XAPPL File Format ##

### Overview ###

XAPPLfile is an XML representation of virtual application configuration settings.

All paths in the XAPPL file are relative to where it resides. For example, the source attribute of a file element begins with ".\Files". The "." directory is the path where the XAPPL file should reside; this ensures that Spoon IDE can locate the physical source files during the build process.
XAPPL files must adhere to XML syntax rules. If there are syntax errors in the XAPPL file, Spoon IDE cannot load the file.

### XAPPL Configuration Elements and Attributes ###

The following table contains the different elements/attributes and their descriptions:

<table border="1" cellpadding="2" cellspacing="2">
	<tr>
		<th>Element/Attribute</th>
		<th>Description</th>
	</tr>

</tr>
<tr>
<td>OutputLocation</td><td>Path to the folder where the virtual application executable is created. This can be a local path, a UNC path, or a mapped drive.</td>
</tr>
<tr>
<td>OutputFile</td><td>File name of the virtual application executable.</td>
</tr>
<tr>
<td>Project-Type</td><td>Denotes whether configuration is for a virtual application (Application) or an <strong>SVM</strong> (Component).</td>
</tr>
<tr>
<td>Licensing</td><td>Contains information about the license used to build the virtual application.</td>
</tr>
<tr>
<td>Output</td><td>The <strong>DiagnosticMode</strong> attribute denotes when the application output should log diagnostic information (<strong>True</strong>) or not (<strong>False</strong>). If true, the virtual application will create diagnostic logs in the directory where it was executed from. <br class="atl-forced-newline" /> The <strong>SourcePackage</strong> attribute is not used.</td>
</tr>
<tr>
<td>MSI</td><td>All sub-elements contain settings pertaining to the configuration of the MSI setup file:
<ul>
<li>The <strong>outputMsiPath</strong> attribute indicates the location where the setup MSI is built.</li>
<li>The <strong>title</strong> attribute indicates the value of the MSI title property.</li>
<li>The <strong>subject</strong> attribute indicates the value of the MSI subject property.</li>
<li>The <strong>keywords</strong> attribute indicates the value of the MSI keywords property.</li>
<li>The <strong>productName</strong> attribute indicates the value of the MSI product name property.</li>
<li>The <strong>productVersion</strong> attribute indicates the value of the MSI product version property.</li>
<li>The <strong>manufacturer</strong> attribute indicates the value of the MSI manufacturer property.</li>
<li>The <strong>productLanguage</strong> attribute indicates the value of the MSI product language property.</li>
<li>The <strong>author</strong> attribute indicates the value of the MSI author property.</li>
<li>The <strong>description</strong> attribute indicates the value of the MSI description property.</li>
<li>The <strong>manufacturerUrl</strong> attribute indicates the value of the MSI manufacturer URL property.</li>
<li>The <strong>autoBuild</strong> attribute denotes whether the MSI should build when the virtual application build completes successfully (<strong>True</strong>) or not (<strong>False</strong>).</li>
<li>The <strong>isolatePerUser</strong> attribute denotes whether the MSI setup should be installed on a per-user basis (<strong>True</strong>) or installed for all users (<strong>False</strong>). When installing per-user, the install root path is Application Data. When installing for all users, the install root path is <strong>Program Files</strong>.</li>
<li>The <strong>applicationFolder</strong> attribute indicates the subfolders into which the virtual application should be installed (<strong>Company Name\Product Name</strong>).</li>
<li>The <strong>upgradePreviousVersion</strong> attribute denotes whether the setup should maintain the same Upgrade code when it builds (<strong>True</strong>) or change the Upgrade code for each build (<strong>False</strong>). This allows the setup to upgrade previous versions when it is installed, or to exist side by side.</li>
<li>The <strong>productCode</strong> attribute indicates the value of MSI product code property.</li>
<li>The <strong>upgradeCode</strong> attribute indicates the value of MSI upgrade code property.</li>
<li>The <strong>componentId</strong> attribute indicates the value of the MSI component id property.</li>
</ul>
</td>
</tr>
<tr>
<td>Packages</td><td>All sub-elements contain settings pertaining to the configuration of the packages included in the virtual application.</td>
</tr>
<tr>
<td>Clr</td><td>The .NET <em>Clr</em> runtime element and all sub-elements contain settings pertaining to the configuration of the virtual .NET Framework runtime.</td>
</tr>
<tr>
<td>Direct X</td><td>The DirectX element and all sub-elements contain settings pertaining to the configuration of the virtual DirectX runtime.</td>
</tr>
<tr>
<td>Java</td><td>All sub-elements contain settings pertaining to the configuration of the virtual java runtime.</td>
</tr>
<tr>
<td>RunTime</td><td>The <strong>name</strong> attribute indicates the name of the java runtime (Java).  <br class="atl-forced-newline" /> The <strong>platform</strong> attribute indicates the platform that the java runtime is designed for (x86). <br class="atl-forced-newline" /> The <strong>version</strong> attribute indicates the version of the java runtime. The available versions are Java 5 (1.5.0.140) and Java 6 (1.6.0.30).</td>
</tr>
<tr>
<td>Settings</td><td>The <strong>startupType</strong> attribute denotes whether to use the jar file (JAR) or class path (Class) command line parameters for java.exe to launch the application. <br class="atl-forced-newline" /> The <strong>startup</strong> attribute indicates the jar file path or class name depending on the StartupType. <br class="atl-forced-newline" /> The <strong>classpath</strong> attribute indicates the path to the class files of the Java runtime. <br class="atl-forced-newline" /> The <strong>options</strong> attribute denotes any additional command line parameter.</td>
</tr>
<tr>
<td>Package</td><td>The <strong>name</strong> attribute indicates the name of the component or runtime. <br class="atl-forced-newline" /> The <strong>platform</strong> attribute indicates the platforms that the component or runtime is supported on. The following are the only available values:
<ul>
<li>
<strong>Any platform (Any)</strong>
</li>
<li>
<strong>x86 platform (x86)</strong> <br class="atl-forced-newline" /> The <strong>version</strong> attribute indicates the version of the component or runtime.</li>
</ul>
</td>
</tr>
<tr>
<td>Virtualization Settings</td><td>All sub-elements contain settings pertaining to the configuration of the virtual operating system.
<ul>
<li>The <strong>suppressBranding</strong> attribute controls the branding pop-up that is displayed (<strong>False</strong>), or not displayed (<strong>True</strong>) in the lower right-hand corner during application startup.</li>
<li>The <strong>isolateWindowClasses</strong> attribute is used to isolate windows classes, as registered via the <strong>Windows ::RegisterClass</strong> or <strong>::RegisterClassEx</strong> APIs. For example, this allows a virtualized Firefox instance to run while a non-virtualized instance is running.</li>
<li>The <strong>readOnlyVirtualization</strong> attribute denotes whether the virtual application has the ability to modify virtual files and registry settings (<strong>False</strong>) or not (<strong>True</strong>). Setting this attribute to <strong>True</strong> will prevent modification to the virtual filesystem and virtual registry.</li>
<li>The <strong>disableXenocodeCommandLine</strong> attribute controls the ability to execute (<strong>False</strong>) any file from within the virtual filesystem.</li>
<li>The <strong>subsystem</strong> attribute indicates the application output type. It can be inherited from the startup file (<strong>Inherit</strong>) or set explicitly to be a Windows application (<strong>GUI</strong>) or console application (<strong>Console</strong>). If <strong>Inherit</strong> is set, but the startup file is either not in the virtual filesystem or not an executable, then the output will be a Windows application.</li>
<li>The <strong>ie6Emulation</strong> attribute denotes a special mode required for the Internet Explorer 6 template (<strong>True</strong>). For all other apps, this should be disabled (<strong>False</strong>).</li>
<li>The <strong>sandboxPath</strong> attribute indicates the base path of the application sandbox <br class="atl-forced-newline" /> <strong>@APPDATALOCAL@\Spoon\Sandbox\@TITLE\@\@VERSION@</strong>. The <strong>workingDirectory</strong> attribute defines what directory the application will run in.</li>
<li>The <strong>compressPayload</strong> attribute controls whether the output executable will be compressed (<strong>True</strong>) or not (<strong>False</strong>).</li>
<li>The <strong>trimUACManifest</strong> attribute removes items from the manifest that may require elevation (<strong>True</strong>).</li>
<li>The <strong>enableDRMCompatibility</strong> attribute ensures compatibility (<strong>True</strong>) with applications protected by software formerly known as &quot;Armadillo&quot; and other DRM software.</li>
<li>The <strong>deleteSandbox</strong> attribute will cause the sandbox to be reset automatically when the virtual application is shutdown (<strong>True</strong>).</li>
<li>The <strong>shutdownProcessTree</strong> attribute will cause the all child processes spawned within the virtual environment to be shutdown when the root process exits. By default, the root process is specified by setting the startup file.</li>
<li>The <strong>exeOptimization</strong> attribute will attempt to launch the startup executable with the initial virtual machine process, preventing the creation of a separate application process (<strong>True</strong>).</li>
<li>The <strong>enhancedDEPCompatibility</strong> attribute provides compatibility for systems with Data Execution Protection enabled (<strong>True</strong>). This setting is used primarily for virtual applications running on Windows 2003.</li>
<li>The <strong>notifyProcessStarts</strong> attribute causes a notification to be sent as a debugging output string whenever a new process is started within the virtual environment (<strong>True</strong>).</li>
<li>The <strong>forceReadShareFiles</strong> attribute forces any file opened by any process within the virtual environment to do so with the READ_SHARE flag set (<strong>True</strong>).</li>
<li>The <strong>launchChildProcsAsUser</strong> attribute causes all child processes to be provided with the same level of privileges as the virtual machine root process (<strong>True</strong>).</li>
<li>The <strong>forceIndicateRunningElevated</strong> attribute forces the application to run as if it has elevated security privileges (<strong>True</strong>).</li>
<li>The <strong>suppressPopups</strong> attribute will prevent an error dialog popup if the virtual application encounters a fatal startup error, and will cause the application to exit silently (<strong>True</strong>).</li>
<li>The <strong>minSandboxSpaceAvail</strong> attribute allows specifying a size in MBs. If set, the virtual application will enforce at startup that the sandbox volume has at least this much space available to the user. A value of -1 disables this enforcement.</li>
<li>The <strong>suppressSandboxCollisionCheck</strong> attribute will enable or disable the ability to detect when multiple applications are trying to access the same sandbox at the same time. This attribute is set to &quot;False&quot; by default.</li>
</ul>
</td>
</tr>
<tr>
<td>XLayers</td><td>Additional SVM's that will be loaded when the application starts
<ul>
<li>The <strong>xlayerSearchPattern</strong> attribute to provide the default search pattern, similar to what would be passed to <strong>/XLayerPath</strong>
</li>
<li>The <strong>RequiredXLayer</strong> sub-element specifies which SVMs are required to be loaded. Otherwise an error is reported. Further details are located in the <a href="/display/spoondoc201403/Specify+Additional+SVMs+for+a+Virtual+Application">Specify Additional SVMs for a Virtual Application</a> section.</li>
</ul>
</td>
</tr>
<tr>
<td>NamedObjectIsolation</td><td>Allows users to isolate select objects in the application from the host machine that may use the same name. Details on how to use this feature can be found in the <a href="/display/spoondoc201403/Enable+Shared+Object+Isolation">Enable Shared Object Isolation</a> section.</td>
</tr>
<tr>
<td>Dns</td><td>Allows users to add explicit dns mappings which are reflected within the virtual environment. Details on how to use this feature can be found in the <a href="/display/spoondoc201403/Virtual+DNS">Virtual DNS</a> section.</td>
</tr>
<tr>
<td>WorkingDirectory</td><td>Specifies which directory the virtual application will execute from.
<ul>
<li>The <strong>option</strong> sub-element can be set to &quot;StartupFileDirectory&quot;, &quot;CurrentDirectory&quot; or &quot;specifiedDirectory&quot;.</li>
<li>The <strong>specifiedDirectory</strong> sub-element lists the specified path selected for the application.</li>
</ul>
</td>
</tr>
<tr>
<td>ChildProcessVirtualization</td><td>
<ul>
<li>The <strong>spawnExternalComServers</strong> attribute controls whether the virtual application launches ComServers in the virtual environment (<strong>True</strong>) or the external environment (<strong>False</strong>).</li>
<li>The <strong>spawnVm</strong> attribute denotes whether the spawned external applications are spawned inside the virtual environment (<strong>True</strong>) or outside the virtual environment (<strong>False</strong>).</li>
</ul>
</td>
</tr>
<tr>
<td>ChildProcessException</td><td>The <strong>name</strong> attribute indicates the name of the executable file (extension included) to except from the effects of the <strong>spawnVm</strong> attribute.</td>
</tr>
<tr>
<td>CustomMetadata</td><td>All sub-elements contain settings pertaining to the configuration of the individual custom metadata items.</td>
</tr>
<tr>
<td>CustomMetadataItem</td><td>
<ul>
<li>The <strong>property</strong> attribute indicates the name of the custom metadata item.</li>
<li>The <strong>value</strong> attribute indicates the value of the custom metadata item.</li>
</ul>
</td>
</tr>
<tr>
<td>StandardMetadata</td><td>All sub-elements contain settings pertaining to the configuration of the individual standard metadata items.</td>
</tr>
<tr>
<td>StandardMetadataIte</td><td>The <strong>property</strong> attribute indicates the name of the standard metadata item.  The following are the available standard metadata:
<ul>
<li>Product Title (<strong>Title</strong>)</li>
<li>Publisher (<strong>Publisher</strong>)</li>
<li>Description (<strong>Description</strong>)</li>
<li>Website (<strong>Website</strong>)</li>
<li>Product Version (<strong>Version</strong>)</li>
</ul>
</td>
</tr>
<tr>
<td>SplashImage</td><td>The <strong>path</strong> attribute indicates the source path to the splash image displayed at application startup. <br class="atl-forced-newline" /> The <strong>transparency</strong> attribute indicates the color in the splash image that should be made transparent when the image is displayed (E.g. <strong>Magenta).</td>
</tr>
<tr>
<td>StartupFiles</td><td>All sub-elements contain configuration pertaining to the individual startup files.</td>
</tr>
<tr>
<td>StartupFile</td><td>The <strong>node</strong> attribute indicates the path of the startup file. <br class="atl-forced-newline" /> The <strong>tag</strong> attribute indicates the command line trigger used to specify this entry as the startup to use. <br class="atl-forced-newline" /> The <strong>commandLine</strong> attribute indicates the command line arguments to pass to the startup file. <br class="atl-forced-newline" /> The <strong>default</strong> attribute denotes whether this entry is executed automatically when no tag is specified (<strong>True</strong>) or not (<strong>False</strong>).</td>
</tr>
<tr>
<td>StartupShims</td><td>All sub-elements contain configuration pertaining to the individual startup shims.</td>
</tr>
<tr>
<td>StartupShim</td><td>The startup shim is a virtualized binary that is invoked prior to the startup file. Startup shims are used to perform customized licensing checks or other initialization tasks.
<ul>
<li>The <strong>shimDllPath</strong> attribute indicates the path to the virtual shim DLL implementation. This field is required.</li>
<li>The <strong>paramOnInitialize</strong> attribute indicates a string to be passed to the shim <strong>OnInitialize</strong> function.</li>
<li>The startup shim signature is <strong>typedef</strong> <strong>BOOL (__</strong>
<strong>stdcall</strong> *<strong>FnOnInititialize) LPCWSTR pwcsInitilizationToken)</strong>. The return value indicates whether virtual machine execution should proceed.</li>
</ul>
</td>
</tr>
<tr>
<td>Layers</td><td>All sub-elements are individual virtual layers.</td>
</tr>
<tr>
<td>Layer</td><td>The <strong>Layer</strong> element and all sub-elements contain settings pertaining to the configuration of this layer of the virtual operating system.
<ul>
<li>The <strong>name</strong> attribute indicates the name of the layer. The default layer (<strong>Default</strong>) is the only layer for whom the name matters. All other layer names are purely informational.</li>
</ul>
</td>
</tr>
<tr>
<td>Condition</td><td>The <strong>variable</strong> attribute indicates the host system setting that will be evaluated. The operating system version (<strong>OS</strong>) is the only available option. <br class="atl-forced-newline" /> The <strong>operator</strong> attribute indicates the Boolean operation that will be used to evaluate the host system. The available Boolean operations are:
<ul>
<li>greater than or equal to (<strong>GREATEREQUAL</strong>)</li>
<li>greater than (<strong>GREATER</strong>)</li>
<li>equal to (<strong>EQUAL</strong>)</li>
<li>not equal to (<strong>NOTEQUAL</strong>)</li>
<li>less than (<strong>LESS</strong>)</li>
<li>less than or equal to (<strong>LESSEQUAL</strong>) <br class="atl-forced-newline" /> The <strong>value</strong> attribute indicates the value against which the host system will be evaluated, using the Boolean operation. The available values in ascending order are:  <br class="atl-forced-newline" /> Windows 2000 (<strong>Win2k</strong>) <br class="atl-forced-newline" /> Windows XP (<strong>WinXP</strong>) <br class="atl-forced-newline" /> Windows 2003 (<strong>Win2k3</strong>) <br class="atl-forced-newline" /> Windows Vista (<strong>Vista</strong>)</li>
</ul>
</td>
</tr>
<tr>
<td>Filesystem</td><td>All sub-elements contain settings pertaining to the configuration of the virtual filesystem.</td>
</tr>
<tr>
<td>Directory</td><td>All sub-elements contain settings pertaining to the configuration of this directory of the virtual filesystem.
<ul>
<li>The <strong>rootType</strong> attribute indicates the root system folder that this virtual folder is mapped to on the host filesystem. Directory elements with the <strong>rootType</strong> attribute are always directly beneath the <strong>Filesystem</strong> element.  The following are the available <strong>rootType</strong>values:<ul>
<li>Application Directory (<strong>Application</strong>)</li>
<li>Windows\System32 (<strong>System</strong>)</li>
<li>Windows (<strong>OS</strong>)</li>
<li>System Drive Root Directory (<strong>SysDrive</strong>)</li>
<li>Program Files\Common (<strong>AllProgramsCommon</strong>)</li>
<li>Program Files (<strong>AllPrograms</strong>)</li>
<li>Current User - Start Menu (<strong>StartMenu</strong>)</li>
<li>Current User - Start Menu\Programs (<strong>Programs</strong>)</li>
<li>Current User - Start Menu\Programs\Startup (<strong>Startup</strong>)</li>
<li>Current User - Application Data (<strong>AppData</strong>)</li>
<li>Current User - LocalSetting\Application Data (<strong>AppDataLoca</strong>l)</li>
<li>Current User - Desktop (<strong>Desktop</strong>)</li>
<li>Current User - Templates (<strong>Templates</strong>)</li>
<li>Current User - Favorites (<strong>Favorites</strong>)</li>
<li>Current User - Music (<strong>Music</strong>)</li>
<li>Current User - Pictures (<strong>Pictures</strong>)</li>
<li>Current User - My Documents (<strong>Documents</strong>)</li>
<li>%PROFILE%  (<strong>Profile</strong>)</li>
<li>All Users - Start Menu (<strong>StartMenuCommon</strong>)</li>
<li>All Users - Start Menu\Programs (<strong>ProgramsCommon</strong>)</li>
<li>All Users - Start Menu\Programs\Startup (<strong>StartupCommon</strong>)</li>
<li>All Users - Application Data (<strong>AppDataCommon</strong>)</li>
<li>All Users - Desktop (<strong>DesktopCommon</strong>)</li>
<li>All Users - Templates (<strong>TemplatesCommon</strong>)</li>
<li>All Users - Favorites (<strong>FavoritesCommon</strong>)</li>
<li>All Users - Music (<strong>MusicCommon</strong>)</li>
<li>All Users - Pictures (<strong>PicturesCommon</strong>)</li>
<li>All Users - My Documents (<strong>DocumentsCommon</strong>)</li>
<li>%ALLUSERSPROFILE% (<strong>ProfileCommon</strong>)</li>
</ul>
</li>
<li>The <strong>isolation</strong>attribute indicates the isolation setting of the virtual folder. The available values are:<ul>
<li>Full isolation (<strong>Full</strong>)</li>
<li>WriteCopy isolation (<strong>WriteCopy</strong>)</li>
<li>Merge isolation (<strong>Merge</strong>)</li>
</ul>
</li>
<li>The <strong>name</strong> attribute indicates the name of the virtual directory.</li>
<li>The <strong>hide</strong> attribute denotes whether the directory is marked as hidden (<strong>True</strong>) or visible (<strong>False</strong>).</li>
</ul>
</td>
</tr>
<tr>
<td>File</td><td>The <strong>name</strong> attribute indicates the name of the file. <br class="atl-forced-newline" /> The <strong>hide</strong> attribute denotes whether the file is marked as hidden (<strong>True</strong>) or visible (<strong>False</strong>). <br class="atl-forced-newline" /> The <strong>source</strong> attribute indicates the source path to the file</td>
</tr>
<tr>
<td>Registry</td><td>All sub-elements contain settings pertaining to the configuration of the virtual registry.</td>
</tr>
<tr>
<td>Key</td><td>All sub-elements contain settings pertaining to the configuration of this key of the virtual filesystem.
<ul>
<li>The <strong>rootType</strong> attribute indicates the root system folder that this virtual folder is mapped to on the host filesystem. Key elements with the <strong>rootType</strong> attribute are always directly beneath the <strong>Registry</strong> element. The following are the available <strong>rootType</strong>values:<ul>
<li>HKEY_CLASSES (<strong>ClassesRoot</strong>)</li>
<li>HKEY_CURRENT_USER (<strong>CurrentUser</strong>)</li>
<li>HKEY_LOCAL_MACHINE (<strong>CurrentUser</strong>)</li>
<li>HKEY_USERS (<strong>Users</strong>)</li>
</ul>
</li>
<li>The <strong>name</strong> attribute indicates the name of the key.</li>
<li>The <strong>namePathInformationTuples</strong> indicates that there is a path in the name or value of the registry item. There are 3 comma delimited integers for each path found in the name/value.1. Flags that indicate the state of the path (valid combinations: 0x0, 0x1, 0x2, 0x4, 0x5, 0x6) <br class="atl-forced-newline" /> 0x1 - All Uppercase <br class="atl-forced-newline" /> 0x2 - All Lowercase <br class="atl-forced-newline" /> 0x4 - Uses Short Path Names <br class="atl-forced-newline" /> 2. Start index of the path <br class="atl-forced-newline" /> 3. Length of the path</li>
<li>The <strong>isolation</strong>attribute indicates the isolation setting of the virtual folder. The available values are:<ul>
<li>Full isolation (<strong>Full</strong>)</li>
<li>Merge isolation (<strong>Merge</strong>)</li>
</ul>
</li>
</ul>
</td>
</tr>
<tr>
<td>Value</td><td>The <strong>name</strong> attribute indicates the name of the value. <br class="atl-forced-newline" /> The <strong>type</strong> attribute indicates the type of the value. The available values are:
<ul>
<li>REG_SZ and REG_EXPAND_SZ (<strong>String</strong>)</li>
<li>REG_DWORD (<strong>DWORD</strong>)</li>
<li>REG_QWORD (<strong>QWORD</strong>)</li>
<li>REB_BINARY (<strong>Binary</strong>)</li>
<li>REG_MULTI_STRING (<strong>StringArray</strong>) <br class="atl-forced-newline" /> The <strong>namePathInformationTuples</strong> indicates that there is a path in the name or value of the registry item. There are 3 comma delimited integers for each path found in the name/value. <br class="atl-forced-newline" />
<ol>
<li>Flags that indicate the state of the path (valid combinations: 0x0, 0x1, 0x2, 0x4, 0x5, 0x6) <br class="atl-forced-newline" /> 0x1 - All Uppercase <br class="atl-forced-newline" /> 0x2 - All Lowercase <br class="atl-forced-newline" /> 0x4 - Uses Short Path Names</li>
<li>Start index of the path</li>
<li>Length of the path <br class="atl-forced-newline" /> The <strong>value</strong> attribute indicates the value of the value. This is true for all types, except <strong>StringArray</strong>, which contains the String sub-element.</li>
</ol>
</li>
</ul>
</td>
</tr>
<tr>
<td>Environment Variables</td><td>The <strong>name</strong> attribute indicates the name of the environment variable. <br class="atl-forced-newline" /> The <strong>value</strong> attribute indicates the value of the environment variable.</td>
</tr>
<tr>
<td>Services</td><td>The <strong>name</strong> attribute indicates the name of the windows service. <br class="atl-forced-newline" /> The <strong>autoStart</strong> attribute denotes whether the windows service starts when the virtual application starts (<strong>True</strong>) or not (<strong>False</strong>). <br class="atl-forced-newline" /> The <strong>commandLine</strong> attribute indicates the startup command line of the windows service. <br class="atl-forced-newline" /> The <strong>friendlyName</strong> attribute indicates the friendly name of the windows service. <br class="atl-forced-newline" /> The <strong>description</strong> attribute indicates the description of the windows service. <br class="atl-forced-newline" /> The <strong>objectName</strong> attribute indicates the account under which the windows service ran when not virtualized. <br class="atl-forced-newline" /> The <strong>keepAlive</strong> attribute denotes whether the windows service should continue running after the startup application has closed (<strong>True</strong>) or not (<strong>False</strong>). <br class="atl-forced-newline" /> The <strong>start</strong> attribute indicates the value of the <strong>Start</strong> <strong>DWORD</strong> value in the Windows Services registry key. <br class="atl-forced-newline" /> The <strong>type</strong> attribute indicates the value of the <strong>Type</strong> <strong>DWORD</strong> value in the Windows Services registry key. <br class="atl-forced-newline" /> The <strong>errorControl</strong> attribute indicates the value of the <strong>ErrorControl</strong> <strong>DWORD</strong> value in the Services registry key.</td>
</tr>
<tr>
<td>Shortcuts</td><td>All sub-elements contain settings pertaining to the configuration of the MSI shortcuts.</td>
</tr>
<tr>
<td>Folder</td><td>All sub-elements contain settings pertaining to the configuration of the MSI shortcuts in this folder. <br class="atl-forced-newline" /> The <strong>name</strong> attribute indicates the name of the folder. The two top level folders represent the Desktop (<strong>Desktop</strong>) and the Programs menu on the Start menu (<strong>Programs Menu</strong>).</td>
</tr>
<tr>
<td>Shortcut</td><td>The <strong>name</strong> attribute indicates the name of the shortcut. <br class="atl-forced-newline" /> The <strong>targetPath</strong> attribute indicates the path of the StartupFile that is the target of the shortcut. <br class="atl-forced-newline" /> The <strong>targetParameter</strong> attribute indicates the Trigger or Tag of the StartupFile that is the target of the shortcut. <br class="atl-forced-newline" /> The <strong>arguments</strong> attribute indicates the arguments passed to the target of the shortcut at runtime. <br class="atl-forced-newline" /> The <strong>showCmd</strong> attribute denotes whether the application should start in a maximized (<strong>3</strong>), minimized (<strong>7</strong>) or regular (<strong>1</strong>) window state. <br class="atl-forced-newline" /> The <strong>description</strong> attribute indicates the description of the shortcut.</td>
</tr>
<tr>
<td>IconResource</td><td>The <strong>IconResource</strong> sub-element contains an identifier of the icon that is used for the Shortcut.</td>
</tr>
<tr>
<td>ProgIds</td><td>All sub-elements contain settings pertaining to the configuration of the ProgId.
<ul>
<li>The <strong>name</strong> attribute indicates the name of the ProgId.</li>
<li>The <strong>description</strong> attribute indicates the description of the ProgId.</li>
</ul>
</td>
</tr>
<tr>
<td>IconResource</td><td>The <strong>IconResource</strong> sub-element contains an identifier of the icon that is used for the file association.</td>
</tr>
<tr>
<td>HarvestSettings</td><td>The <strong>HarvestSettings</strong> element only appears in Desktop Scan configurations, or recipes. This section tells the configuration which files, folders, and registry keys to add or delete from the build.</td>
</tr>
<tr>
<td>Extension</td><td>All sub-elements contain settings pertaining to the configuration of the file extensions for the ProgId.
<ul>
<li>The <strong>extension</strong> attribute indicates the file extension that is associated with the ProgId.</li>
<li>The <strong>mimeType</strong> attribute indicates the MIME type of all files with the extension.</li>
</ul>
</td>
</tr>
<tr>
<td>DefaultPrograms</td><td>For the <strong>DefaultPrograms</strong> element, specify the following parameters:
<ul>
<li>
<strong>name</strong> – Name of the application (e.g. Thunderbird, Firefox).</li>
<li>
<strong>friendlyName</strong> – Friendly name (e.g. Thunderbird, Firefox).</li>
<li>
<strong>description</strong> – Description (e.g. Mail Client, Web Browser).</li>
<li>
<strong>clientType</strong> – Type of Default Program (e.g. Browser, Mail, StartMenuInternet). This can be found under <em>Current user root/Software/Clients</em> or <em>Local machine root/Software/Clients</em>.</li>
<li>
<strong>hidden</strong> – This should be set to <em>false</em>.</li>
<li>
<strong>default</strong> – This should be set to <em>true</em>.   <br class="atl-forced-newline" />   <br class="atl-forced-newline" /> The sub-elements of the <strong>DefaultPrograms</strong> are:</li>
<li>
<strong>IconResource</strong> – This is the program icon and can be copied from the ProgId section of the XAPPL.</li>
<li>
<strong>data</strong> – This contains data to render the icon.</li>
<li>
<strong>Extension</strong> – These are the file extensions that use this DefaulProgram (e.g. .eml, .html, .htm).</li>
<li>
<strong>name</strong> – This is the extension (e.g. .eml, .html, .htm).</li>
<li>
<strong>progId</strong> – This is a reference to which ProgId to use to handle this type of file extension.</li>
<li>
<strong>Protocol</strong> – These are the protocols that use the DefaultProgram (e.g. mailto, http, https).</li>
<li>
<strong>name</strong> – This is the name of the protocol (e.g. mailto, http, https, news).</li>
<li>
<strong>progId</strong> – This is a reference to the ProgId that will handle this protocol.</li>
<li>
<strong>clientType</strong> – This is the name of the client under <em>Current user root/Software/Clients</em> or <em>Local machine root/Software/Clients</em>.</li>
<li>
<strong>SimpleMapi</strong> – This is specific to the mail clientType.</li>
<li>
<strong>mapiDllPath</strong> – Path to the DLL to use for MAPI for this mail client.</li>
<li>
<strong>mailClientPath</strong> – Path to the main exe of the application.</li>
</ul>
</td>
</tr>
<tr>
<td>Verb</td><td>All sub-elements contain settings pertaining to the configuration of the Verb for the file extension.
<ul>
<li>The <strong>title</strong> attribute indicates the title of the verb.</li>
<li>The <strong>verb</strong> attribute indicates the verb value.</li>
<li>The <strong>arguments</strong> attribute indicates the arguments passed to the target of the verb at runtime.</li>
<li>The <strong>default</strong> attribute denotes whether this verb is the default verb (<strong>True</strong>) or not (<strong>False</strong>).</li>
</ul>
</td>
</tr>
</table>


## Snapshot Settings ##

### Description ###
Snapshot settings are defined within a file called SnapshotSettings.xml. This file is auto-created upon first snapshot under the [AppDataLocal]\Spoon\Spoon IDE\ folder. The file contains two major sections: **Filesystem** and 
**Registry**

Under each, one can specify the following settings: *Root* paths, *Include* paths, *Exclude* paths, *AllOrNothing* roots, and *Isolation* overrides.

### Child elements ###

- **Root**: Allows the specifying of snapshot roots. Possible values include the standard special folder values, such as **@PROGRAMFILES@** and **@SYSTEM@**. 

	**Note**: these roots should be specified in order from deepest to shallowest in a filesystem.

- **Include**: Allows specifying a force-include path which overrides any exclude paths. Useful when you want exceptions to a wildcard exclude path.

- **Exclude**: Allows specifying a path which should be excluded from snapshot. Wildcards may be used in the last element, such as `@PROGRAMFILES@\Acme\Cache_*`

- **AllOrNothing**: Used to indicate a root under which new or modified sub-folders/keys are added in an all-or-nothing fashion. Useful under certain areas of the registry for example where COM is configured. 

- **Isolation**: Used to override isolation settings for a given path and below. Use the isolation attribute with possible values: *Full*, *Merge*, or *WriteCopy*.

All elements take a path attribute to specify the path for the given setting.

### Sample SnapshotSettings File (abbreviated) ###
<pre>
<?xml version="1.0" encoding="utf-8"?>

&lt;SnapshotSettings>
  &lt;!--Filesystem snapshot settings-->
  &lt;Filesystem>
  &lt;!--Set of snapshot starting-point root folders.  Removing any of these
        will cause it to be removed from the set of starting points.  But
        note that sometimes we can still arrive at a deeper root by way of
        a shallower root, unless the path to the deeper root is excluded
        at some point.
        NOTE: Should order these from deepest to shallowest-->
    &lt;Root path="@PROGRAMFILESCOMMON@" />
    &lt;Root path="@PROGRAMFILES@" />
    &lt;Root path="@PROGRAMFILESCOMMONX86@" />
    &lt;Root path="@PROGRAMFILESX86@" />
    &lt;Root path="@SYSTEM@" />
    &lt;Root path="@SYSWOW64@" />
    &lt;Root path="@WINDIR@" />
    &lt;Root path="@SYSDRIVE@" />
    &lt;Exclude path="@SYSDRIVE@\Pagefile.sys" />
    &lt;Exclude path="@SYSDRIVE@\Boot" />
    &lt;Exclude path="@SYSDRIVE@\$Recycle.Bin" />
    &lt;Exclude path="@APPDATA@\Microsoft\Windows NT" />
    &lt;Exclude path="@APPDATA@\Microsoft\Internet Explorer" />
    &lt;Exclude path="@PROFILE@\AppData" />
    &lt;Exclude path="@APPDATALOCAL@\Microsoft\Internet Explorer" />
    &lt;Exclude path="@APPDATACOMMON@\Microsoft\Windows Defender" />
    &lt;Exclude path="@WINDIR@\WinSXS\ManifestCache" />
    &lt;Exclude path="@SYSTEM@\vpc-s3.cfg" />
    &lt;Exclude path="@SYSTEM@\CatRoot2" />
    &lt;Exclude path="@SYSTEM@\NtmsData" />
    &lt;Isolation path="@SYSTEM@\mui" isolation="Merge" />
    &lt;Isolation path="@SYSWOW64@\mui" isolation="Merge" />
    &lt;Isolation path="@DOCUMENTS@" isolation="Merge" />
    &lt;Isolation path="@PICTURES@" isolation="Merge" />
    &lt;Isolation path="@MUSIC@" isolation="Merge" />
  &lt;/Filesystem>
  &lt;!--Registry snapshot settings-->
  &lt;Registry>
    &lt;!--Set of snapshot starting point root folders.  Removing any of these
        will cause it to be removed from the set of starting points.  But
        note that sometimes we can still arrive at a deeper root by way of
        a shallower root, unless the path to the deeper root is excluded
        at some point.-->
    &lt;Root path="@HKCU@" />
    &lt;Root path="@HKLM@" />
    &lt;!--Excluded HKLM subkeys by default, we will select what we want
        NOTE:  wow64If="true" (the default) causes both path flavors to be added as in:
            HKEY_LOCAL_MACHINE\Software\Classes\AppId and
            HKEY_LOCAL_MACHINE\Software\Classes\Wow6432Node\AppId -->
    &lt;Exclude path="HKEY_LOCAL_MACHINE\*" />
    &lt;Include path="HKEY_LOCAL_MACHINE\Software" wow64If="false" />
    &lt;Include path="HKEY_LOCAL_MACHINE\System" wow64If="false" />
    &lt;Exclude path="HKEY_LOCAL_MACHINE\Software\Classes\Local Settings" />
    &lt;Exclude path="HKEY_LOCAL_MACHINE\Software\Microsoft\Rpc" />
    &lt;Exclude path="HKEY_LOCAL_MACHINE\Software\Microsoft\DrWatson" />
    &lt;Exclude path="HKEY_LOCAL_MACHINE\System\*" />
    &lt;Include path="HKEY_LOCAL_MACHINE\System\CurrentControlSet" />
    &lt;Exclude path="HKEY_LOCAL_MACHINE\System\CurrentControlSet\*"/>
    &lt;Include path="HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services" />
    &lt;!--AllOrNothing mean that any immediate subkey of the given root is added in
        all-or-nothing fashion.  Any add/modify under one of these locations causes the
        entire sub-tree to be added.  One can also configure names for subkey exceptions.
        Setting wow64iIf="True" (the default) will cause both flavors of the path to be added, as
        in: HKEY_LOCAL_MACHINE\Software\Classes\AppId and
            HKEY_LOCAL_MACHINE\Software\Classes\Wow6432Node\AppId -->
    &lt;AllOrNothing path="HKEY_CURRENT_USER\Software\Classes\Applications" />
    &lt;AllOrNothing path="HKEY_LOCAL_MACHINE\Software\Classes\Applications" />
    &lt;AllOrNothing path="HKEY_CURRENT_USER\Software\Classes\AppID" />
    &lt;AllOrNothing path="HKEY_LOCAL_MACHINE\Software\Classes\AppID" />
  &lt;/Registry>
&lt;/SnapshotSettings>
</pre>

## Specifying a Virtual Mapped Drive ##

A virtual mapped drive can be added to your **XAPPL** file in the **FileSystem** section. This is not available through the Spoon IDE UI, but can be added manually in a text editor. To do this:

1. Open the **XAPPL** file in your text editor of choice
2. Navigate to the **FileSystem** section of the **XAPPL** file
	- This section is enclosed by the tags `<FileSystem>` and `</FileSystem>`
3. Add your virtual file to the filesystem
	- See the example, below for a sample code snippet
	- The `@DRIVE_X@` variable in the snippet represents the virtual drive. Any letter can be specified by changing the letter of this variable (for example, if your virtual drive was M:, you would use `name="@DRIVE_M@"`

The example shown, below, is for adding the virtual file `X:\AppData\Settings.txt` to the configuration. When added in this way, the virtual mapped drive will *not* be visible in Windows Explorer or through File browse dialogs, but it will be visible via command window or if the application does a file lookup using standard Windows APIs.
<pre>
&lt;Directory rootType="VirtualDrive" name="@DRIVE_X@" isolation="Merge">
    &lt;Directory name="AppData" hide="False" readOnly="False" isolation="Full">
        &lt;File name="Settings.txt" hide="False" readOnly="False" source=".\Files\X_Drive\AppData\Settings.txt" />
    &lt;/Directory>
&lt;/Directory>
</pre>
