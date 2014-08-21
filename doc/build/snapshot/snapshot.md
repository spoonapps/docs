In this walkthrough you will learn how to create a virtual OpenOffice application using the snapshot, jukebox, and setup features of Spoon Virtual Application Studio. Although this example is specific for OpenOffice, the processes described can be used to virtualize and configure almost any application.

## Snapshot

The snapshot process consists of two phases: the before snapshot and the after snapshot. The before snapshot takes an inventory of all files and settings that are currently on the computer. The after snapshot is taken after the target application is installed. The contents of the after snapshot are compared to the before snapshot to determine all changes made to the host system during installation. The after snapshot also copies the new or modified files to a snapshot directory specified by the user.

Snapshots must be performed on clean Microsoft Windows machine. This ensures that all dependencies are included in the installation and are captured by the snapshot process.

Complete the following steps to snapshot the OpenOffice installation:

1. Capture the before snapshot by selecting Capture Before on the Spoon Virtual Application Studio ribbon bar. The snapshot process can take a few minutes.

2. Install OpenOffice and all of its necessary dependencies.
**Tip**: Launch the application and change the default settings in Preferences or Options to apply them in the virtual build of the application.

3. Capture the after snapshot by selecting Capture and Diff. Spoon Virtual Application Studio will prompt for the directory where the snapshot files are to be stored.

**Note**: If your application requires you to restart the system before it can finish, save the before snapshot. Choose the arrow below Capture Before and select Save Snapshot. Before you capture the after snapshot, load it by choosing the arrow below Capture Before again and selecting Load Snapshot.

## Saving the Virtual Application Configuration

Save a copy of the original virtual application snapshot in case errors are introduced during virtual application customization and optimization. Saving a copy also enables you to test and modify the application without re-snapshotting. Because the original snapshot is automatically saved during Capture and Diff, you can save a copy of the configuration for modification as a new file.

Complete the following steps to save the virtual application configuration:

1. Select **Start Menu** and choose **Save Configuration As**.

2. The Spoon Virtual Application Studio configuration file is stored as a Spoon XAPPL file. The XAPPL format does not contain the filesystem content, which is saved separately in the Files directory during the after snapshot.

**Note**: The XAPPL file uses relative paths to identify snapshot files. The Files directory and the XAPPL files must be located in the same directory.

## Configuring the Virtual Application

After you create the application snapshot, you can modify or optimize the configuration. For example, OpenOffice is a suite of applications; program entry points must be setup so each application can run individually.

Complete the following steps to get OpenOffice to function as a virtual application:

1. Set the Output File.

2. Configure the Startup Files (Jukeboxing).

3. Configure the Setup options.

4. Remove unused installation files (optional).

## Setting the Output File Name

The **Output File** is the name of the virtual executable file or **SVM** that is created by Spoon Virtual Application Studio.

Complete the following steps to set the Output File:

1. Select Virtual Application.

2. Locate the Output group and select Browse.

3. Choose a location for the output and assign it a file name.

## Startup Files (Jukeboxing)

The Startup File settings identify specific files that can be executed by the virtual application. These files can be started by launching the virtual application, launching it with command line parameters (see Specifying multiple startup files (Jukeboxing)), or launching it via registered shortcuts (see Configure Shortcuts).

Complete the following steps to configure Startup Files:

1. Select Virtual Application.

2. Locate the Output group and select the Multiple to open the Startup Files window.

3. The Start Files window displays all entry points for the application. If an entry point is missing for your application, you can add one by:

a. Using Start Files, enter the File location on the first line and select Enter.

b. Using Filesystem, locate the target file. Right-click on the file and select Add to Startup Files.

4. Command Line enables you to add parameters for each Startup File.

5. Trigger sets the command-line parameter that specifies which Startup File to launch.

6. **Note**: each Startup File must have a unique value for its Trigger field.

7. Select Auto Start for the Startup File that should run by default if no Trigger is passed to the virtual application.

## Setup Options

When virtualizing suites such as OpenOffice you can create a setup file. Setup files generated by Spoon Virtual Application Studio are created using MSI setup file format. Spoon Virtual Application Studio setup files only install the virtual application and create file associations and shortcuts. No other installation functions are performed.

**Note**: Setup options also apply if the application is registered to the Microsoft Windows shell using the Spoon plugin (refer to Using the Spoon Console) or SpoonReg tool (refer Register Virtual Applications in the Windows Shell).

To create a setup file for the virtual application, the Output Location, Product Info, Installation Parameters, Shortcuts, and File Associations must be configured in Setup.

- Output Location defines where the setup file is created.

- Product Info is the metadata associated with the setup file. Product Info is displayed in the Add/ Remove Programs window. This information must be accurate.

- Installation Parameters control how the virtual application is installed on the host system.

- Shortcuts enable the end user to launch the application directly from the Microsoft Windows Start Menu, Desktop, and Sent To menus.

#### Output Location

Complete the following steps o define Output Location for the virtual application setup file:

1. From Setup select the MSI tree node. 

2. Select Browse and assign it a file name.

3. Select Automatically Generate MSI After Successful Build to automatically create the setup file after the build process.

#### Product Info

The following fields specify metadata associated with setup files and is visible in the Add/Remove Programs window. These fields are accessed from the MSI tree node under Setup.

- Product Name: The name of the application.

- Product Version: The version of the application.

- Company Name: The name of the company that made the application.

#### Installation Parameters

Installation Parameters are accessed from the MSI tree node under Setup.

To install the virtual application for All Users, select the Install Application for All Users check box. When checked administrative privileges are required on the target system.

For Application Folder, the Company Name\Product Name must be entered. If neither is entered, the virtual application is installed under folders named "Company Name\Product Name".

To automatically update existing versions, select Automatically Upgrade Earlier Application Versions. This updates previous versions of the virtual executable. To use side-by-side installation, select Allow Side-by-Side Versions of the Same Application.

#### Creating Shortcuts

Although Studio automatically detects application shortcuts in the snapshot process, you can manually configure them as well.

Complete the following steps to manage shortcuts for the virtual application:

From Setup expand Shortcuts and select one of the shortcut destinations: Desktop, Programs Menu, or SendTo.

- Select Add Shortcut and assign it a Name, a Target, an Icon, and enter any Arguments that must pass to the specific application. Existing Shortcuts can be changed or deleted by using Edit Shortcut or Remove.

- Select Add Folder to create a shortcut folder for shortcut organization.

For more information refer to Configure Shortcuts.

#### File Associations

Although Studio automatically detects file associations in the snapshot process, you can manually configure them as well.

Complete the following steps to manage file associations:

1. From Setup expand ProgIds.

2. Select Add ProgId and enter ProgId and Description. Change or remove existing * ProgIds* by selecting Edit ProgId or Remove. When a verb is necessary for the ProgId, choose its node and select Add Verb. Enter the necessary information in the Create Verb window.

3. Expand Extensions.

4. Select Add Extension and enter the file Extension and associated ProgId. Enter the MIME Type for the association.

## Pruning

Temporary installation files are created during application installation processes. These files are necessary for installation but not required for the virtual application to run.

In OpenOffice, installation files are created in the same directory from which the install executable was executed.

Complete the following steps to remove these files from the snapshot:

1. Open Filesystem.

2. Navigate to the location of the installation files, right-click the folder, and select Delete.

**Note**: For OpenOffice, removing the installation files from the snapshot can reduce output virtual application binary size by up to 151 MB.

## Build and Test

You can build and test a virtual application after it is configured, customized, and optimized.  

Complete the following steps to build the virtual application:

1. Select Build or Build and Run. This creates the virtual application binary file where Output File is defined. The build process can take a few minutes.

2. The MSI setup file is created at a separate location defined by Output Location (when the steps to automatically create one were followed).

Complete the following steps to test the virtual application:

1. Execute the virtual application binary file. The OpenOffice splash screen displays and the OpenOffice Quickstarter opens.

2. Execute the virtual application binary file from a command prompt with the "swriter" Trigger. For example, run "openoffice.exe swriter" from a command prompt and the OpenOffice Writer application opens instead of the Quickstarter.

Complete the following steps to test the Setup options:

1. Execute the setup file on a system without OpenOffice installed. The virtual application, shortcuts and file associations are installed on the host system.

2. Open the OpenOffice Writer Program from the Start Menu shortcut.

3. Open a file associated with the OpenOffice Writer program. 



Commercial applications require combinations of filesystem and registry entries. To facilitate containerization of these applications, Spoon IDE can snapshot application installations and automatically configure them based on modifications made to the host system during setup.

## Snapshots

Snapshots use before and after images of the host machine to determine configuration:

- Before: This snapshot is taken prior to installing the application and captures the state of the host device without the target application installed.

- After: This snapshot is taken after installing the application and captures all changes to the host device during application installation. Studio then computes the changes between the before and after snapshots, and inserts these changes into the configuration.

Complete the following steps to use the Snapshot feature:

1. Prepare the host device: remove the target application and all dependencies or copy Studio onto a clean machine.

2. Capture the before image: select the Virtual Application tab on the ribbon bar and then Capture Before. This may take several minutes to complete.

3. Save the before snapshot (optional): saving the before snapshot enables you to skip this step in subsequent applications from the same clean machine. Select the down arrow underneath Capture Before and choose Save Snapshot. Studio automatically saves the most recently captured before snapshot; this snapshot is reset once the Capture and Diff is complete.

4. Install your application: also install any other files, settings, runtimes, and components you want to include in the image. Refer to Add Runtimes and Components for more information. If the application setup requests a reboot, save the before snapshot, then proceed with the reboot.

5. Capture the after image: on the Virtual Application tab on the ribbon bar, select Capture and Diff.  This captures the after snapshot, computes the deltas between the two snapshots, and populates the image with the delta entries.

6. Review the filesystem and registry entries: also remove any files or settings which are not required for proper execution of your virtual application. Removing unused entries will reduce image size. Avoid accidental removal of required resources, as it will cause your image to no longer function properly.

## Saving snapshots

Sometimes the before snapshot remains fixed while several after snapshots are taken. It is recommended that you save the before snapshot image so that the before snapshot does not need to be re-captured each time. Because snapshots can take up to several minutes, this can significantly reduce the time required to build virtual applications.

To save the before snapshot, select the down arrow underneath the Capture Before button on the Virtual Application ribbon bar and choose Save Snapshot from the drop-down menu. Select a filename and location and choose Save. To load a saved snapshot, select Load Snapshot and navigate to the saved snapshot file. To clear the current before snapshot image, select Clear Snapshot.

## Quick Snapshot Mode

Spoon Virtual Application Studio uses a "quick" snapshot algorithm which attempts to minimize the amount of time spent scanning the host system device. Sometimes, but rarely, use of this mode can result in an improperly configured virtual application. Use of quick snapshot mode can also increase the size of the virtual application configuration contents. Perform snapshots using the quick snapshot mode. Disabling quick snapshot mode significantly increases the amount of time required to complete the virtual application configuration process.

To disable quick snapshot mode, uncheck Quick snapshot mode in the Options menu.

Note: before and after snapshots must be taken using the same snapshot algorithm. Loading a saved snapshot image causes Spoon Virtual Application Studio to automatically configure the snapshot mode to be consistent with the algorithm used during the saved snapshot capture.

## Capture Application Updates via Snapshot

Virtual application updates can be captured within Spoon IDE via snapshots.

Complete the following steps to capture an update via snapshots:

1. Install the native version of the application on a clean machine.

2. Select Capture Before.

3. Install necessary updates to the native application.

4. Select Capture and Diff to create the after snapshot. This captures the deltas between the original and updated versions.

5. Set the Project Type to Component, then select Build to create the SVM.

This process only captures changes between the original executable and installed updates. You can then apply the resulting SVM to the original virtual package.

For more information on updating virtual applications using SVMs, refer to Create and Use Shared Virtual Components and Specify Additional SVMs for a Virtual Application.

## Best Practices

### Machine Configuration

#### Perform Snapshot on a Clean Machine

Performing the snapshot on a clean machine ensures that all dependencies are installed by the application setup. Installing on a machine with existing components can inadvertently include dependencies in the before snapshot and exclude them from the final output.

#### Use Snapshot with Whole-Machine Virtualization

If you configure a clean machine using whole-machine virtualization tools such as Microsoft Virtual PC and save a before snapshot based on this image you can snapshot many distinct virtual applications in rapid succession by reverting the whole-machine virtual state and using the same before snapshot.

#### Snapshot on the Earliest Operating System Variant you Target

Most applications can be configured by performing the snapshot on the earliest (least common denominator) target operating system. A small number of applications may require multi-platform merge for successful deployment across all operating system variants.

### Snapshot Process

#### Proper Build Procedure

Capture the before snapshot on a clean machine. Install the application and any necessary dependencies/components. If necessary, perform a custom installation to include/exclude items from the build. Once the installation is complete, perform the Capture and Diff snapshot. Save a backup copy of the configuration file (snapshot.xappl) adjacent to the Files folder created during the Capture and Diff. Edit the configuration, removing unnecessary registry keys, files and folders. Set the desired isolation settings. Finally, build and test the application.

#### Saving the Capture and Diff Snapshot

When selecting a folder to save the Capture and Diff snapshot, select Make New Folder in Spoon Virtual Application Studio. This folder will not be included in the snapshot. If the folder is included in the Capture and Diff snapshot, remove it using the Filesystem tab.

#### Save Before Pruning

Before beginning the pruning process, save a backup of the Capture and Diff snapshot (snapshot.xappl). Revert to the original Capture and Diff snapshot in the event of an error.

#### Run Native Application to Determine Isolation Characteristics

Run and use the native application to understand what registry keys and folders it updates at runtime. This will help determine the proper isolation settings for folders and registry keys.

#### Fully Isolated or Merged

To determine if a folder should be set to full isolation or merge isolation, decide if the user would want access to files created within that folder outside the virtual application environment. If yes, the folder should be set to merge, if no, full.

#### Removing Uninstall Shortcuts

Remove uninstall shortcuts during the pruning process. There are two steps to removing uninstall shortcuts:

1. Navigate to Setup and remove the file from the list of shortcuts.

2. Remove the shortcut from the list of start-up files, if it exists: select Multiple and then delete any uninstall files.

#### Removing Logs

When the application is ready for the final build, make sure to uncheck the Generate diagnostic-mode executable box. Otherwise logs are created every time the virtual application runs.

#### Testing Isolation

Complete the following steps to verify that a virtual application will not create unnecessary files outside of the sandbox:

1. Take a before snapshot on a clean machine and run the virtual application.

2. Use the virtual application as if you were an actual user.

3. Close the virtual application and take the capture and diff snapshot. Verify that there are no unintentional files or folders created outside the sandbox inside the Filesystem and Registry tab. If such files/folders exist, edit the xappl to set the folders/files to Full Isolation and then retest for isolation issues.