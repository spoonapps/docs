# Packaging Basics #
In this section you will learn about the basics of creating and editing virtual application configurations.
## What are Snapshots? ##
Commercial applications require combinations of filesystem and registry entries. To facilitate virtualization of these applications, Studio can snapshot application installations and automatically configure them based on modifications made to the host system during setup.

Snapshots use before and after images of the host machine to determine configuration:

- **Before:** This snapshot is taken prior to installing the application and captures the state of the host device without the target application installed.
- **After:** This snapshot is taken after installing the application and captures all changes to the host device during application installation. Studio then computes the changes between the before and after snapshots, and inserts these changes into the configuration.

### Using the Snapshot feature ###

Complete the following steps to use the Snapshot feature:

1. Prepare the host device: remove the target application and all dependencies or copy Studio onto a clean machine.
2. Capture the **before** image: select the **Virtual Application** tab on the ribbon bar and then **Capture Before**. This may take several minutes to complete.
3. Save the **before** snapshot (optional): saving the before snapshot enables you to skip this step in subsequent applications from the same clean machine. Select the down arrow underneath **Capture Before** and choose **Save Snapshot**. Studio automatically saves the most recently captured before snapshot; this snapshot is reset once the **Capture and Diff** is complete.
4. Install your application: also install any other files, settings, runtimes, and components you want to include in the virtual application. Refer to [Add Runtimes and Components](#add-runtimes-and-components) for more information. If the application setup requests a reboot, save the before snapshot, then proceed with the reboot.
5. Capture the **after** image: on the **Virtual Application** tab on the ribbon bar, select **Capture and Diff**.  This captures the after snapshot, computes the deltas between the two snapshots, and populates the virtual application with the delta entries.
6. Review the filesystem and registry entries: also remove any files or settings which are not required for proper execution of your virtual application. Removing unused entries will reduce virtual application size. Avoid accidental removal of required resources, as it will cause your virtual application to no longer function properly.

### Saving snapshots ###
Sometimes the **before** snapshot remains fixed while several **after** snapshots are taken. It is recommended that you save the **before** snapshot image so that the before snapshot does not need to be re-captured each time. Because snapshots can take up to several minutes, this can significantly reduce the time required to build virtual applications.

To save the before snapshot, select the down arrow underneath the **Capture Before** button on the **Virtual Application** ribbon bar and choose **Save Snapshot** from the drop-down menu. Select a filename and location and choose **Save**. To load a saved snapshot, select **Load Snapshot** and navigate to the saved snapshot file. To clear the current before snapshot image, select **Clear Snapshot**. 

## Load and Save Configurations ##

After you configure your virtual application and take your after snapshot, save the configuration for future use or modification. It is important to save the virtual application snapshot in its original state, in order to avoid saving any errors introduced during virtual application customization and optimization. This also enables the application to be tested and modified without the need to re-snapshot after each iteration.

To save a configuration:

- Select the **File Menu** menu and choose **Save Configuration As**.
- Select a filename and location and choose Save. This saves the virtual application configuration file. By default, configuration files use the extension **.xappl**.

**Note:** Configuration files do not store the *contents* of virtual filesystem files. The configuration file specifies only the *source path* for each virtual filesystem entry.  The source file must exist at build time or the virtual application will not build successfully.

Spoon IDE automatically stores source file locations as paths relative to the location of the saved **XAPPL** file, in the same directory as the **XAPPL** file (the folder marked Files).

**Note:** Spoon IDE users can create their own default settings for application building by saving an **XAPPL** file with a few customization settings (Example: changing the default sandbox location) and no associated application, then loading this **XAPPL** file (and saving as a new file) before beginning the snapshot process in a new project.

## Specify a Startup File ##

Although the virtual filesystem can contain several executable files (such as .exe, .cmd, and .java) and viewable file formats (such as .html and .swf), your virtual application is consolidated into a single executable. It is necessary for the virtual application designer to indicate a startup file -- the executable or viewable file that opens when the user starts the virtual application.

A startup file should be specified after the application has been installed and configured with runtimes and the after snapshot has been taken.

Complete the following steps to select the startup file:
1. Select **Virtual Application** from the ribbon bar. 
2. Select **Startup File**. This opens a drop-down menu listing all files in the virtual filesystem. 
3. Select the startup file or navigate to the desired startup file in the virtual filesystem display. Right-click the file, and select **Set as Startup File**.

Files located on the host device (outside of the virtual filesystem) can be used as startup files. To select a file on the host device as the startup file, enter that file's full path in the **Startup File** text box. Use well-known root folder variables, such as **@WINDIR@** and **@PROGRAMFILES@**, as the root of the full path to ensure that the startup file can be located on all base operating systems.

**Note**:While any file can be selected as the startup file, you should only select a file which is executable or viewable. Selecting a file that cannot be opened will cause an error when the virtual application is started.

### Specify Multiple Startup Files (Jukeboxing) ###
In some situations a virtual application can expose multiple startup files. For example, when using a virtualized office productivity suite, you may want to launch the word processor or spreadsheet component of the suite while still deploying a single executable file.

Studio enables triggering multiple entry points into the virtual application based on a command-line argument to the executable. For example, in the office suite scenario described, you could use the command line argument **office word** (to trigger the word processor) and **office spreadsheet** (to trigger the spreadsheet) Refer to [The Snapshot Process](#the-snapshot-process) for an example of Jukeboxing during the OpenOffice build process.

Complete the following steps to specify multiple startup files:

1. Select the **Multiple** button adjacent to the **Startup File** textbox on the **Virtual Application** ribbon bar. This displays the **Startup Files** selection dialog. 
2. Select the **File** column on the first empty row in the startup file list and select the desired file from the drop-down list. Files located on the host device (outside of the virtual filesystem) can also be used as startup files. To select a file on the host device as the startup file, enter the full path to the desired startup file in the **Startup File** text box. 
3. Enter the desired command line arguments, if any, in the **Command Line** column.
4. Enter the desired command line trigger in the **Trigger** column. For example, in the command line office word, the trigger would be word.
5. Check the **Auto Start** checkbox if you want the startup file to automatically launch on startup.
6. After adding a new startup file, hit **Enter** to save.

**Note:** When specifying a startup file located outside of the virtual filesystem, use well-known root folder variables such as **@WINDIR@** and **@PROGRAMFILES@** as the root of the full path to ensure that the startup file can be properly located on all base operating systems.

**Note:** The **Auto Start** flag can be specified for multiple startup files. This will automatically launch multiple applications typically used together in a single session (also known as **shotgunning**).

**Note:** When deploying applications using Spoon Server, the command line arguments in this section are ignored. When deploying with Spoon Server, specify the command line arguments in the **Setup > Shortcuts** section of the configuration. The shortcuts correspond to **Entry Points** in Spoon Server. More information is available under the [Manage Applications](#manage-applications) section.

## Edit the Virtual Filesystem ##
Spoon IDE enables you to embed a *virtual filesystem* into your executable. Embedded files are accessible by your Spoon-processed application as if they were present in the actual filesystem. Virtual files, unlike files on the host device, are not visible from and do not require changes to the host device. Virtual files do not require security privileges on the host device, regardless of whether the virtual files reside in a privileged directory. Because virtual files are embedded in the application executable, shared DLLs do not interfere with or are overwritten by other applications on the host device.

Complete the following steps to add virtual files:

1. Select the **Filesystem** button located on the left side of the Spoon IDE window. 
2. Add the files and folders you wish to embed in the application executable. The **Application Directory** represents the folder containing the virtual application binary on the executing device; the other root folders represent the corresponding folders on the host device.

**Note:** When running a virtual application on Windows 7, the **All Users Directory\Application Data** and **All Users Directory** root folders will map to the same folder at runtime. To prevent one setting from overriding another, verify that the isolation settings for these folders are the same.

### Virtualization Semantics ###

In the event of a conflict between a file in the virtual filesystem and a file present on the host device, the file in the virtual filesystem takes precedence.

Folders may be virtualized in **Full**, **Merge**, **Write Copy**, or **Hide** mode.

- **Full**: Full mode is used when a complete level of virtual application isolation is your desired outcome. Only files in the virtual filesystem are visible to the application, even if a corresponding directory exists on the host device, and writes are redirected to the sandbox data area. 
- **Merge**: Merge mode is generally used when some level of interaction with the host device is your desired outcome. For example, **Merge** mode can be used to enable the virtualized application to write to the host device's **My Documents** folder. Files present in a virtual folder are merged with files in the corresponding directory on the host machine, if such a directory exists. Writes to host files are passed through to the host device and writes to virtual files are redirected into the sandbox data area. 
- **Write Copy**: Write Copy mode is used when a virtual application must be read from files already present on the host device, but isolation of the host device is still desired. Files present on the host device are visible to the virtual environment, but any modifications to folder contents are redirected to the sandbox data area. 
- **Hide**: Hide mode is used when a file on the host machine could interfere with the application's ability to run properly. By adding a file or folder with **Hide** enabled, the application receives a File Not Found message, even if the file or folder exists on the host machine. Files and folders with **Hide** enabled will return a **File Not Found** message to the application at runtime. This applies to both the virtual filesystem and the host file system. 

**Tip**: To apply selected isolation modes to all subfolders, right-click on the folder, choose Isolation, select the checkbox for **Apply to Subfolders**, then select **OK**.

### File Attributes ###

Files and folders can be hidden from shell browse dialogs and other applications. This is used to prevent internal components and data files from being displayed to the user. To hide a file or folder, select the checkbox in the **Hidden** column adjacent to the desired file or folder.

**Note**: The **Hidden Flag** is NOT the **Hide** isolation mode. Enabling the **Hidden Flag** prevents a file or folder from displaying in browse dialogs or from directory enumeration APIs; it does not prevent the application (and potentially the end-user) from accessing the folder or file contents by direct binding. To prevent the file or folder from being found by the application, enable **Hide** isolation mode.

Flagging files and folders as read-only prevents the application from modifying the file or folder contents. To make a file or folder read-only, select the checkbox in the **Read Only** column next to the desired file or folder.

### No Upgrade ###

By default, Spoon IDE enables files in the virtual filesystem to be upgraded with patches (refer Updating Registration Settings in the [Register Virtual Applications in the Windows Shell](register-virtual-applications-in-the-windows-shell) section for more information). If there are files in the virtual filesystem that should not be upgraded, such as user data files, select the **No Upgrade** flag to prevent these files from being upgraded.

### No Sync ###

This feature only applies to virtual applications that are delivered and managed by Spoon Virtual Desktop Server, or Spoon.net. By default, Spoon IDE enables files in the virtual filesystem to be synchronized to a user's Spoon account. This enables the application state to be maintained across different devices that are Spoon enabled. If there are folders in the virtual filesystem that should not be synchronized, but should remain only on the local device, enable the **No Sync** flag to prevent files within the folder from being synchronized. This setting is managed on a folder level and applies to all files within that folder.

### Filesystem Compression ###

To reduce executable size, Spoon IDE can compress virtual filesystem contents. This reduces virtual application size by approximately 50%, but also prevents profiling and streaming of the application. By default, the **Compress Payload** option in the **Process Configuration** area of the **Settings** panel is unchecked. Leave this box unchecked during the build process if the application will be optimized for streaming from Spoon Server.

**Note**: Disabling payload compression may significantly increase the size of the virtual application binary.


## Edit the Virtual Registry ##
Spoon IDE enables you to embed a virtual registry into your executable. Embedded registry keys are accessible by your Spoon-processed application as if they were present in the actual registry. Unlike data present on the host device, virtual registry keys and values are not visible from and do not require changes to the host device. The use of a virtual registry does not require security privileges on the host device, even if the virtual registry entries are in a privileged section of the registry. Because virtual registry entries are embedded in the application executable, other applications are unable to disrupt application execution by inadvertent modification of registry entries.

Complete the following steps to add virtual registry data:

1. Select the Registry button located on the left side of the Spoon IDE window.
2. Add or remove the registry keys and values you want to embed in the application executable. When adding blob data, enter the values in hexadecimal format.

The **Classes** root, **Current User** root, **Local Machine** root, and **Users** root folders correspond to the **HKEY_CLASSES_ROOT**, **HKEY_CURRENT_USER**, **HKEY_LOCAL_MACHINE**, and **HKEY_USERS** keys on the host machine. 

Registry string values can include well-known variables such as **@WINDIR@**, **@SYSWOW64@**, **@PROGRAMFILESX86@** and **@PROGRAMFILES@**.

### Virtualization Semantics ###

In the event of a conflict between a key or value in the virtual filesystem and data present on the host device registry, information in the virtual registry takes precedence. Keys may be virtualized in **Full**, **Merge**, **Write Copy**, or **Hide** mode.

- **Full**: In Full mode, values only in the virtual registry are visible to the application, even if a corresponding key exists on the host device, and writes are redirected to the user registry area.
- **Merge**: In Merge mode, values present in a virtual key are merged with values in the corresponding key on the host machine (if such a key exists). Writes to host keys are passed through to the host registry and writes to virtual keys are redirected to the user registry area.
- **Write Copy**: Write Copy mode is used when a virtual application must be read from registry keys already present on the host device, but isolation of the host device is still desired. Keys and values present on the host device are visible to the virtual environment, but any modifications to keys or values are redirected to the sandbox data area. 
- **Hide**: Keys and values in the virtual registry or the corresponding host registry will not be found by the application at runtime.

**Tip**: To apply selected isolation modes to all subkeys, right-click on the key, choose **Isolation**, select the checkbox for **Apply to Subkeys**, then **OK**.

### No Sync ###

This feature only applies to virtual applications that are delivered and managed by Spoon Virtual Desktop Server, or Spoon.net. By default, Spoon IDE enables registry keys in the virtual registry to be synchronized to a user's Spoon account. This enables the application state to be maintained across different devices that are Spoon enabled. If there are keys in the virtual registry that should not be synchronized, but should remain only on the local device, enable the **No Sync** flag to prevent that key and any values within the key from being synchronized. This setting is managed on a registry key level and applies to all values within that key.

### Importing Registry Hive Files ###

Spoon IDE can import registry hive (.reg) files into the virtual registry. To import a .reg file, select the **Import** button in the **Registry** panel, then choose the registry hive file to import.

## Add Runtimes and Components ##
Many components and runtime systems consist of large, complex sets of filesystem entries and registry settings. Spoon IDE contains a collection of pre-configured component settings which can be added to your virtual application with a single click. For example, if your application is a .NET Framework 4.0 application, then selecting the .NET Framework 4.0 component will allow your executable to run on machines without the .NET Framework installed.

Additional runtimes and components are added to the virtual application during the snapshot process, before the **after** snapshot is taken.

To add a runtime or component:

1. Select the **Runtimes** tab on the ribbon bar. 
2. Select the appropriate runtime or component. Selected components are indicated with a highlighted button. To remove a component, click on the button again. The button will no longer be highlighted and the component will not be included.

**Note**: The displayed runtimes apply to the currently selected target architecture (see process settings). If the target architecture is changed, architecture specific runtimes, like .NET 2 or .NET 3.x will still be included but will not display as selected. To deselect them, the target architecture must be changed back, and the runtimes can be deselected.

**Note**: Depending on the size of the component, the executable size can significantly increase. Only select components that are required for proper execution of your application.

**Note**: You are responsible for compliance with licensing for any third-party redistributable components included in your virtualized application.

### Using .NET Runtimes ###

To limit conflicts with installed .NET runtimes, the .NET runtime packages are isolated from the native file system. If the application requires access to multiple .NET versions, it is necessary to include all of the required runtimes in the virtual package. For example, including only the .NET 4 runtime will hide visibility to the .NET 3.5 runtime on the native file system. This is fine if the application only requires the .NET 4 components, but would be problematic if it also requires earlier versions of .NET.

An alternative approach would be to use the snapshot feature of Spoon IDE to build a custom .NET component for the application. This approach provides visibility into the files and registry keys that are available and allows for custom isolation settings.

### Configuring the Java Runtime ###
Spoon IDE provides specialized support for the Java runtime. If your application is based on Java runtime, select the **Sun Java Runtime** button on the **Runtimes** ribbon bar. This displays the Java configuration menu.

Select the appropriate version of the Java runtime from the **Java runtime version** drop-down menu. If you deploy your application as a set of .class files, select **Class** from the **Startup Type** drop-down menu; if you deploy within a .jar file, select **Jar**. Enter the startup class name or Jar name in the appropriate textbox, along with any additional Java runtime options.

## Create and Use Shared Virtual Components ##

Sometimes multiple virtual applications can share common sets of configuration options. For example, system administrators may want to share a common set of configuration options (browser bookmarks, application settings, etc.) across a department or enterprise. With Spoon IDE you can easily create, share, and use virtual machine settings across multiple virtual applications.

Complete the following steps to create a shared virtual component:

1. Begin a new virtual application configuration.
2. Configure the filesystem, registry, and settings as you would for a standard virtual application. Refer to [Snapshots](#snapshots) and [Manually Configure a Simple Virtual Application](#manually-configure-a-virtual-application) for more information on this topic.
3. Select the **Virtual Application** tab.
4. Find the **Project Type** drop-down menu located in the **Output** ribbon group and set it to **Component**.
5. Select **Build** to create the component.

In **Component** mode, the build process ends with the creation of an **SVM** file instead of an executable file. An **SVM** contains the virtual application settings and data payload. **SVMs** are similar to virtual executable outputs; however, **SVMs** do *not* contain the Spoon virtual machine runtime engine. An **SVM** can only be used when combined as part of another virtual application or deployed with Spoon Server.

Complete the following steps to use an existing shared virtual component:

1. Click on the **Components** button to navigate to the project components pane.
2. If the component does not already appear in the components table, click **Import Components...**
3. Select the **SVM** file you wish to load into your project, and click **OK**. The **SVM** is then loaded into your project and the layer metadata is displayed in the **Components** list.
4. Select the checkbox next to the desired component.

To build without the component, uncheck the checkbox next to the component and rebuild.

Project virtualization settings take precedence over virtualization settings in any loaded shared components.

To remove a component completely so it will not be available for other applications, select the component and click the **Remove Component** button.

**Note**: Imported components are stored under the user's profile, %userprofile%\Spoon\Components. If the project is moved from one computer to another, the components will need to be removed and re-imported on the new machine.

## Embed a Database Engine ##
You can use Spoon IDE to embed SQL Server 2005 Express directly into the executable file. This enables executables to run an SQL Server user-instance for a virtual .mdf database file. 

Complete the following steps to embed SQL Server 2005 Express:

1. Select the **Runtimes** button on the ribbon bar.
2. Choose the **SQL Server 2005 Express** option.

### Configuring Applications to Use an Embedded Database ###

The code displayed in the database configuration dialog provides an example of how to create a connection string. This is for connecting to the user-instance database that loads an .mdf file from the virtual filesystem.

The virtualized SQL Server 2005 Express default instance name is stored in a  variable named `%SQLXENOCODE%`. A unique instance of this name is created at build time and is not user-configurable.

Complete the following steps to embed a database file:

1. Verify the desired .mdf database file is added to the virtual filesystem. 
2. Choose the .mdf database file to attach using the **AttachDBFilename** drop-down menu. This path is stored in the `%AttachDBFilename%` environment variable.

To manually modify this selection, select the **Environment Variables** button on the Process Configuration tab of the Settings pane. To add additional databases, create an additional **Environment Variable** for each database.

**Note**: The .NET 2.0 Framework is automatically included when the SQL Server Express 2005 engine is selected. SQL Server 2005 Express requires this component. If this component is removed, the application will only run on machines that have the .NET Framework 2.0 installed.

## Sandbox Merge ##
Sandbox merge enables sandbox content and settings generated during virtual application execution to be applied to a Spoon IDE configuration. Sandbox merge is an alternative to manual registry or filesystem configuration, and can be used applying additional customizations to virtual application configurations.

Complete the following steps to merge an existing sandbox into the active configuration:

1. Select Sandbox Merge from the Tools section of the Virtual Application toolbar.
2. Enter the path of the sandbox to be merged.
3. Select OK.

For example, complete the following steps to customize the home page of the Firefox virtual application template:

- Use the **Configuration Wizard** to create a Firefox virtual application (the wizard enables customization of the home page, but you can use the **Sandbox Merge** feature to override the setting specified in the wizard.
- Select **Build and Run** to launch the virtualized Firefox application.
- Using the Firefox interface, specify a new browser home page.
- Exit the Firefox virtual application.
- Select **Sandbox Merge** to display the sandbox merge dialog. The sandbox path will be pre-populated with the location of the Firefox virtual sandbox.
- Select **OK**. 

The virtual application settings update with the configuration changes made using Firefox, including the updated browser home page. 
