# Best Practices #

## Best Practices for Snapshots ##
The following practices are recommended for optimal Snapshot feature use.
Machine Configuration
Perform Snapshot on a Clean Machine
Performing the snapshot on a clean machine ensures that all dependencies are installed by the application setup. Installing on a machine with existing components can inadvertently include dependencies in the before snapshot and exclude them from the final output.
Use Snapshot with Whole-Machine Virtualization
If you configure a clean machine using whole-machine virtualization tools such as Microsoft Virtual PC and save a before snapshot based on this image you can snapshot many distinct virtual applications in rapid succession by reverting the whole-machine virtual state and using the same before snapshot.
Snapshot on the Earliest Operating System Variant you Target
Most applications can be configured by performing the snapshot on the earliest (least common denominator) target operating system. A small number of applications may require multi-platform merge for successful deployment across all operating system variants.
Snapshot Process
Proper Build ﻿Procedure
Capture the before snapshot on a clean machine. Install the application and any necessary dependencies/components. If necessary, perform a custom installation to include/exclude items from the build. Once the installation is complete, perform the Capture and Diff snapshot. Save a backup copy of the configuration file (snapshot.xappl) adjacent to the Files folder created during the Capture and Diff. Edit the configuration, removing unnecessary registry keys, files and folders. Set the desired isolation settings. Finally, build and test the application.
Saving the Capture and Diff Snapshot
When selecting a folder to save the Capture and Diff snapshot, select Make New Folder in Spoon Virtual Application Studio. This folder will not be included in the snapshot. If the folder is included in the Capture and Diff snapshot, remove it using the Filesystem tab.
Save Before Pruning
Before beginning the pruning process, save a backup of the Capture and Diff snapshot (snapshot.xappl). Revert to the original Capture and Diff snapshot in the event of an error.
Run Native Application to Determine Isolation Characteristics
Run and use the native application to understand what registry keys and folders it updates at runtime. This will help determine the proper isolcations settings for folders and registry keys.
Fully Isolated or Merged
To determine if a folder should be set to full isolation or merge isolation, decide if the user would want access to files created within that folder outside the virtual application environment. If yes, the folder should be set to merge, if no, full.
Removing Uninstall Shortcuts
Remove uninstall shortcuts during the pruning process. There are two steps to removing uninstall shortcuts:
Navigate to Setup and remove the file from the list of shortcuts.
Remove the shortcut from the list of start-up files, if it exists: select Multiple and then delete any uninstall files.
Removing Logs
When the application is ready for the final build, make sure to uncheck the Generate diagnostic-mode executable box. Otherwise logs are created every time the virtual application runs.
Testing Isolation
Complete the following steps to verify that a virtual application will not create unnecessary files outside of the sandbox:
Take a before snapshot on a clean machine and run the virtual application.
Use the virtual application as if you were an actual user.
Close the virtual application and take the capture and diff snapshot. Verify that there are no unintentional files or folders created outside the sandbox inside the Filesystem and Registry tab. If such files/folders exist, edit the xappl to set the folders/files to Full Isolation and then retest for isolation issues.


## Best Practices for the Desktop Scan Wizard ##
When running the Desktop Scan wizard, there are a few best practices users can follow for optimal results:
It is recommended that users run the desktop scan on the oldest operating system version available. For example, if users use both Windows XP and Windows 7, it is advised to run the desktop scan on the Windows XP machine.
The exception is with Microsoft Office. For the Microsoft Office Suite, it is recommended to run the scan from the operating system where it is intended to be used.
When scanning OpenOffice, it is recommended to scan the version available with Java. This will allow the packaged application to function on machines that do not have Java installed as well as machines that do. It is also possible that the desktop scan will not find an installation of OpenOffice that does not include Java.
Applications packaged with the desktop scan may retain settings from the local machine used during the packaging process.
Adobe Creative Suite (all versions) will not complete correctly when scanned from Windows Vista. When using the desktop scan to package Adobe Creative Suite, Windows XP or Windows 7 is recommended.
When using the dsektop scan with browsers, ensure that any plugins that are installed outside the browser, such as Windows Media Player, are already installed when the scan is run. This is important because some plugins are installed using the msiexec.exe process and won't be recognized within the virtualized browser. Plugins that are installed from within the browser, such as Adobe Flash, do not have this problem.

## Virtualizing Microsoft Internet Explorer ##
Due to the complexity of packaging Internet Explorer, Spoon provides several version as part of the Template Wizard. If using the Template Wizard is not an option, there are recommendations below on how to best package Internet Explorer.
Use Microsoft Internet Explorer snapshot compatibility mode under the Options menu when snapshotting. This ensures a complete capture of the Microsoft Internet Explorer portions of the registry and filesystem.
Internet Explorer 9 should be virtualized from Windows Vista x32 to support the largest number of Windows platforms. Internet Explorer 9 is not supported on Windows XP.

## Setting Up and Managing a Build Lab ##

If you intend to build virtualized applications on a regular basis, set up a build lab to ensure quality application builds and decrease build time. Perform certain steps on multiple operating systems to ensure maximum compatibility and performance. Because many steps are time-consuming the process can move more efficiently if steps are performed on multiple machines. This process is referred to as pipeline building, and is useful when virtualizing a high volume of applications.
Setting Up a Build Lab
Set up a build lab with the following six machine configurations:
Windows XP, Service Pack 3, x86 architecture
Windows XP, Service Pack 2, x64 architecture
Windows Vista, Service Pack 2, x86 architecture
Windows Vista, Service Pack 2, x64 architecture
Windows 7, Service Pack 1, x86 architecture
Windows 7, Service Pack 1, x64 architecture
Regularly re-imaged each machine to an initial configuration, or clean state. Clean machines are required to complete build and testing processes. Save an image of the initial configuration on a local partition, then use third-party software to create an external drive to boot the machine from that image.
Complete the following steps to setup the initial configuration for each machine:
Set up two partitions: one for the operating system and the other for the clean image.
Install the operating system.
Install all current patches for the OS, except for Microsoft Internet Explorer upgrades.
Create accounts for an administrator and a standard user.
Disable automatic updates.
The following steps are optional, but recommended:
Run Microsoft Internet Explorer 8 once to prevent repeating the first-run wizard each time you re-image the machine to a clean state.
Enable remote desktop protocol access.
Configure the power options so the machine never enters the sleep state.
Disable the Microsoft Windows Firewall.
Right-click My Computer, select Properties, select Advanced, edit the Performance Settings to Adjust for Best Performance.
After the operating system is set up, create a system image (using software such as Paragon Partition Manager) on a USB drive. Use this image to restore the machine to a clean state.
Note: It is not necessary to set up a build lab using physical machines; a build lab can be set up using a collection of virtual machine images. For this approach, Spoon recommends creating virtual machine images for each of the six machine configurations. The virtual machines should be configured following the steps set forth in this section, excluding the creation of a new partition. It is not necessary to create a partition to save the clean image because you can save the current state of a virtual machine.
Build process
The "build process" is the process of converting a Windows desktop application into a standalone executable (EXE) or Spoon Virtual Machine (SVM).
Use the snapshot technique to capture the application on a "clean" Windows XP 32-bit machine. The snapshot process is covered in detail in the Snapshots topic of the Getting Started section.
Use Spoon Virtual Application Studio to generate a standalone executable.
Test this executable per the recommendations in the "Build testing process" section.
If the virtual application fails to run on Windows Vista or Windows 7, it may be necessary to perform the snapshot on multiple platforms, and then perform a platform merge. Refer to the Platform Merge topic in the Advanced Topics section for details on how to perform a platform merge.
After the application has been verified to work on all six platforms, use Spoon Virtual Application Studio to generate a component (SVM file) if needed.
If the virtual application fails to build or function correctly, please refer to the Troubleshooting section in this document or contact Spoon support.
Build testing process
The build test process exists to ensure that the build process successfully captured all aspects of the target application necessary for the virtual application to run correctly.
Spoon recommends adhering to the following strategies while testing virtual applications:
Conduct testing on each of the six machine platforms identified in the "Setting up the build lab" section above.
Under ideal circumstances, each machine in your build lab should be "cleaned" prior to testing the virtual application.
At a minimum, the virtual application should not be tested on a machine where the application is also natively installed.
Profiling the application
If the virtual application is intended to be delivered via the Web as a streaming application, you may choose to profile the virtual application in order to dramatically reduce the buffering time needed to launch the application. Spoon recommends profiling any application greater than 10 MB in size.
During the profiling process, you will use the application as a typical user would, while Studio observes this behavior and stores it in a transcript. These transcripts are then subsequently used to construct a streaming model of the application. There is no limit to the number of transcripts that can be used to construct a streaming model, Spoon recommends gathering at least one transcript from each of the six machine platforms identified in the "Setting up the build lab" section above. The profiling process is covered in detail in the Create Application Streaming Models topic in the Advanced Topics section.
Managing builds
Spoon recommends allocating a folder on a shared network drive to store and organize the SVMs, EXEs,* *and models generated as a result of the virtualization process.
During the build process, Spoon recommends storing the snapshot files, the EXE and SVM in the following folder structure:
Snapshot - \\<Share>\Builds\<Application>\<Version>.
During the profiling process, Spoon recommends storing the transcripts and model files in the following folder structure:
Transcripts - *\\<Share>\Builds\<Application>\<Version>\Transcripts*
Models - \\<Share>\Builds\<Application>\<Version>\XStream\<Model Number>
If it is necessary to deliver virtual applications and models to Spoon, please contact Spoon support (support@spoon.net) for additional details.