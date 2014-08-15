# Best Practices #
This section describes various best practices for making use of Spoon IDE. All methods outlined in this section are optional.

## Best Practices for Configuring Applications using the Snapshot Process ##

### Machine Configuration ###

#### Perform Snapshot on a Clean Machine ####
Performing the snapshot on a clean machine ensures that all dependencies are installed by the application setup. Installing on a machine with existing components can inadvertently include dependencies in the before snapshot and exclude them from the final output.

#### Use Snapshot with Whole-Machine Virtualization ####

If you configure a clean machine using whole-machine virtualization tools such as Microsoft Virtual PC and save a before snapshot based on this image you can snapshot many distinct virtual applications in rapid succession by reverting the whole-machine virtual state and using the same before snapshot.

#### Snapshot on the Earliest Operating System Variant you Target ####

Most applications can be configured by performing the snapshot on the earliest (least common denominator) target operating system. A small number of applications may require multi-platform merge for successful deployment across all operating system variants.

### Snapshot Process ###

#### Proper Build ﻿Procedure ####
Capture the before snapshot on a clean machine. Install the application and any necessary dependencies/components. If necessary, perform a custom installation to include/exclude items from the build. Once the installation is complete, perform the Capture and Diff snapshot. Save a backup copy of the configuration file (snapshot.xappl) adjacent to the Files folder created during the Capture and Diff. Edit the configuration, removing unnecessary registry keys, files and folders. Set the desired isolation settings. Finally, build and test the application.

#### Saving the Capture and Diff Snapshot ####

When selecting a folder to save the **Capture and Diff** snapshot, select **Make New Folder** in Spoon IDE. This folder will not be included in the snapshot. If the folder is included in the **Capture and Diff** snapshot, remove it using the **Filesystem** tab.

#### Save Before Editing ####

Before editing the configuration, save a backup of the **Capture and Diff** snapshot (snapshot.xappl). Revert to the original **Capture and Diff** snapshot in the event of an error.

#### Run Native Application to Determine Isolation Characteristics ####

Run and use the native application to understand what registry keys and folders it updates at runtime. This will help determine the proper isolcations settings for folders and registry keys.

#### Fully Isolated or Merged ####

To determine if a folder should be set to full isolation or merge isolation, decide if the user would want access to files created within that folder outside the virtual application environment. If yes, the folder should be set to merge, if no, full.

#### Removing Uninstall Shortcuts ####

Remove uninstall shortcuts during the pruning process. There are two steps to removing uninstall shortcuts:

1. Navigate to **Setup** and remove the file from the list of shortcuts.
2. Remove the shortcut from the list of start-up files, if it exists: select **Multiple** and then delete any uninstall files.

#### Removing Logs ####

When the application is ready for the final build, make sure to uncheck the Generate diagnostic-mode executable box. Otherwise logs are created every time the virtual application runs.

#### Testing Isolation ####

Complete the following steps to verify that a virtual application will not create unnecessary files outside of the sandbox:

1. Take a before snapshot on a clean machine and run the virtual application. 
2. Use the virtual application as if you were an actual user.
3. Close the virtual application and take the capture and diff snapshot. Verify that there are no unintentional files or folders created outside the sandbox inside the **Filesystem** and **Registry** tab. If such files/folders exist, edit the **xappl** to set the folders/files to Full Isolation and then retest for isolation issues.


## Best Practices for the Desktop Scan Wizard ##
When running the Desktop Scan wizard, there are a few best practices users can follow for optimal results:

- It is recommended that users run the desktop scan on the oldest operating system version available. For example, if users use both Windows XP and Windows 7, it is advised to run the desktop scan on the Windows XP machine.
- The exception is with Microsoft Office. For the Microsoft Office Suite, it is recommended to run the scan from the operating system where it is intended to be used.
- When scanning OpenOffice, it is recommended to scan the version available with Java. This will allow the packaged application to function on machines that do not have Java installed as well as machines that do. It is also possible that the desktop scan will not find an installation of OpenOffice that does not include Java.
- Applications packaged with the desktop scan may retain settings from the local machine used during the packaging process.
- Adobe Creative Suite (all versions) will not complete correctly when scanned from Windows Vista. When using the desktop scan to package Adobe Creative Suite, Windows XP or Windows 7 is recommended.
- When using the desktop scan with browsers, ensure that any plugins that are installed outside the browser, such as Windows Media Player, are already installed when the scan is run. This is important because some plugins are installed using the msiexec.exe process and won't be recognized within the virtualized browser. Plugins that are installed from within the browser, such as Adobe Flash, do not have this problem.

## Virtualizing Microsoft Internet Explorer ##
Due to the complexity of packaging Internet Explorer, Spoon provides several version as part of the **Template Wizard**. If using the **Template Wizard** is not an option, there are recommendations below on how to best package Internet Explorer.

Use **Microsoft Internet Explorer snapshot compatibility mode** under the **Options** menu when snapshotting. This ensures a complete capture of the Microsoft Internet Explorer portions of the registry and filesystem.

Internet Explorer 9 should be virtualized from Windows Vista 32-bit to support the largest number of Windows platforms. Internet Explorer 9 does not support Windows XP.

