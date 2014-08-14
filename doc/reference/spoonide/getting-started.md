# Getting Started with Spoon IDE #

## System Requirements ##

Spoon IDE runs on most Microsoft Windows operating systems as old as or newer than Windows 2000. For a full list of supported platforms, see What Platforms are Supported?

The Spoon IDE graphical interface assumes a screen resolution of at least 800×600, although a screen resolution of at least 1024×768 is recommended.

## User Interface Overview ##

Using the Spoon IDE user interface enables you to configure the filesystem and registry of a virtual application, embed external runtimes and components, take application snapshots, and create Spoon Virtual Machine (SVM) or executable files. The primary interface consists of a ribbon bar along the top and several panes accessed by buttons on the left.

### Items Located Above the Ribbon Bar ###

- The Start Menu button, or the circle at the top left of the window, enables virtual application configurations to be created, opened, saved, imported, applied, and closed.
- The Options bar provides Spoon IDE interface customization options, as well as the ability to set proxy settings and install certificates.
- The Help bar provides access to Spoon IDE documentation, including a searchable version of this document.

### Spoon IDE Ribbon Bar ###

- The Virtual Application tab provides access to the snapshot and build features, as well as output configuration options such as the startup file, output directory, and diagnostic-mode selection.
- The Runtimes tab provides a selection of auto-configurable runtime engines which can be embedded into your application with a single click. These include .NET Framework, Java, Flash, Shockwave, Acrobat Reader, and SQL Server 2005 Express runtimes.
- The Advanced tab provides advanced Spoon IDE functions such as Platform Merge and Streaming.

### Left-side button panes ###

- The Filesystem pane displays the application virtual filesystem, and enables you to add and remove virtual files and directories.
- The Registry pane displays the application virtual registry, and enables you to add and remove virtual registry keys and data values.
- The Settings pane enables you to configure virtual application metadata, startup image and shim, and process configuration options.
- The Components pane enables you to layer external virtual application components, such as toolbars and optional features.
- The Setup pane enables you to configure the MSI setup package, shortcuts, and other shell integration options.
- The Expiration pane enables you to configure application expiration options.

**Note:** Spoon IDE users are responsible for any third-party licensing compliance for redistributable components included using virtualization.

## Virtual Application Creation Methods ##

Spoon IDE offers four ways to create and configure virtualized applications:

- **Scan desktop for installed applications:** This is the recommended method for packaging standard applications like Microsoft Office. This option will scan your desktop for installed applications and build the virtual applications using content and settings from the desktop where Spoon IDE is running. See [Packaging Applications with the Desktop Scan](#package-with-desktop-scan).
- **Build a virtual application from a template:** Spoon IDE includes templates for many popular applications. This option automatically virtualizes and configures popular applications using a guided wizard and user-provided or downloaded media. This method is recommended for first-time users of Spoon IDE.
- **Snapshot a third-party application or component:** In this method, snapshots capture the system state before and after an application is installed. Based on the observed system changes, the virtual application settings are automatically configured. This method is ideal for virtualizing off-the-shelf applications. Refer to Snapshotting applications for more information.
- **Manually configure virtualization settings:**  This method is primarily used by developers who are virtualizing internally-developed applications. Manual configuration requires substantial technical knowledge, but allows maximum control over virtual application settings. Refer to Manually Configure a Simple Virtual Application for more information.

Every method provides additional configuration and customization after the initial virtual application configuration is constructed. For information on current available editions of Spoon IDE, visit [http://Spoon.net/Studio](http://Spoon.net/Studio).

<a name="package-with-desktop-scan"></a>
## Packaging Applications with the Desktop Scan ##
Spoon IDE can scan the machine where it is installed and build virtual application packages for use with 
Spoon Server using the content and settings from that machine.

### Running the Desktop Scan ###

1. Open the Configuration Wizard from the Virtual Application tab.
2. Click the button next to Scan desktop for installed applications.
3. A progress window displays while the filesystem and registry are scanned for application identifying information.
4. Once the scan is completed, the user has a chance to review the application that were found on the system. Clicking Next matched the information against the database of known applications.
5. A list of installed applications that match the available applications from Spoon is displayed. Check the box next to the applications to be packaged and click Next.
	- For some applications, there may be multiple options (such as language). Choose the option that matches the installed application on the desktop.
6. Choose the Location where the packaged applications will be placed.
7. Choose the Output format of the application packages then click Next.
8. A progress window displays while the selected applications are packaged. This process can take several minutes depending on the size and number of applications selected.
9. Once the process is finished, a window displays showing the results. If multiple applications are selected to be packaged, the status of each will be displayed. If one application fails to be packaged, it is possible for the other selected applications to build successfully.

The application is now ready to be imported into Spoon Server.

**Note: **Applications packaged with this method may retain the user settings that were in place at the time of the scan.

### Troubleshooting the Desktop Scan ###
To enable logging for the desktop scan add the following registry key.


    [HKEY_CURRENT_USER\Software\Code Systems\Spoon]
    "TraceLevel"="Debug"

After adding this registry key, logging information can be viewed through the DebugView console available from Microsoft's website.

## Packaging Applications using the Template Wizard ##
For applications that are not picked up in the Desktop scan, or if the application configuration needs to be modified, the template wizard can be used:

1. Open the Studio Configuration Wizard. The wizard starts automatically when Spoon IDE is launched. You can also open the wizard by selecting **Configuration Wizard** on the **Virtual Application** ribbon bar.
2. Select the box labeled **Build a virtual application from a template**.
3. Select an application from the Application drop-down menu.
4. The application information will be harvested from the local machine unless the application is flagged with a ' * '. If the application is not flagged, it must be installed on the local machine as part of the packaging process.
5. Follow the wizard steps to construct the virtual application.

After completing the wizard the application configuration remains loaded in the Spoon IDE interface while the settings are inspected and additional customization is performed. Refer to [Configure Virtual Applications](#configure-virtual-applications) and [Customize Virtual Applications](#customize-virtual-applications) for more information about configuration and customization.