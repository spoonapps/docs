# Walkthroughs #

## Manually Configure a Simple Virtual Application ##
In this section you will learn how to manually configure a simple virtual application in Spoon Virtual Application Studio based on the Microsoft Windows Notepad application. Manual configuration is typically used by experienced software developers to package internally developed applications.
Complete the following steps to add Microsoft Windows Notepad to the virtual application configuration:
Select Filesystem.
Open the Filesystem > System Drive > System32 tree node.
Select Add Files.
Navigate to the System32 folder under your Microsoft Windows installation directory, usually located at C:\Windows\System32, and double-click on notepad.exe.
Right-click on notepad.exe from the display on the right and select Set as Startup File.
For Microsoft Windows Vista and 7:
While the System32 node is still selected, choose New Folder and set the name to en-us.
Set the isolation for the en-us folder to Merge.
Open the en-us folder node and select Add Files to add the notepad.exe.mui file, which is required by the Notepad application. The file is located in the System32\en-us folder inside your Windows installation.
Complete the following steps to add a text file to the virtual application configuration:
Using Notepad, create a file called hello.txt containing the text "Hello world" and save it to your desktop folder.
In Spoon Virtual Application Studio, open the Filesystem > Current User Directory > Desktop node and select Add Files to add the hello.txt file.
Complete the following steps to build a virtual application from your configuration:
Select the Virtual Application tab to display the virtual application settings.
Verify that the Startup File points to notepad.exe. The startup file indicates which file to execute when a virtual application is started by the user.
Select Browse for the Output File setting, then navigate to your desktop folder and Save. The output file indicates where to save the virtual application executable.
Choose Build. Spoon Virtual Application Studio will display a status dialog while it builds your virtual application. When it finishes, select OK.
To launch the newly built virtual Notepad, navigate to your desktop using Microsoft Windows Explorer and double-click on notepad.exe.
Complete the following steps to verify that you are inside the virtual application:
Using Windows Explorer, delete the hello.txt file from your desktop folder. 
Launch the virtual Notepad application and navigate to File > Open.
Navigate to the Desktop folder and verify that the hello.txt file is still present. This occurs because the virtual Notepad application is using the virtual system, which includes the hello.txt file that was added in the build process. You can open and view hello.txt exactly as if it were a real file in the physical filesystem.

## The Snapshot Process ##
Snapshot
The snapshot process consists of two phases: the before snapshot and the after snapshot. The before snapshot takes an inventory of all files and settings that are currently on the computer. The after snapshot is taken after the target application is installed. The contents of the after snapshot are compared to the before snapshot to determine all changes made to the host system during installation. The after snapshot also copies the new or modified files to a snapshot directory specified by the user.
Snapshots must be performed on clean Microsoft Windows machine. This ensures that all dependencies are included in the installation and are captured by the snapshot process.
Complete the following steps to snapshot the OpenOffice installation:
Capture the before snapshot by selecting Capture Before on the Spoon Virtual Application Studio ribbon bar. The snapshot process can take a few minutes.
Install OpenOffice and all of its necessary dependencies.
Tip: Launch the application and change the default settings in Preferences or Options to apply them in the virtual build of the application.
Capture the after snapshot by selecting Capture and Diff. Spoon Virtual Application Studio will prompt for the directory where the snapshot files are to be stored.
Note: If your application requires you to restart the system before it can finish, save the before snapshot. Choose the arrow below Capture Before and select Save Snapshot. Before you capture the after snapshot, load it by choosing the arrow below Capture Before again and selecting Load Snapshot.
Saving the Virtual Application Configuration
Save a copy of the original virtual application snapshot in case errors are introduced during virtual application customization and optimization. Saving a copy also enables you to test and modify the application without re-snapshotting. Because the original snapshot is automatically saved during Capture and Diff, you can save a copy of the configuration for modification as a new file.
Complete the following steps to save the virtual application configuration:
Select Start Menu and choose Save Configuration As.
The Spoon Virtual Application Studio configuration file is stored as a Spoon XAPPL file. The XAPPL format does not contain the filesystem content, which is saved separately in the Files directory during the after snapshot.
Note: The XAPPL file uses relative paths to identify snapshot files. The Files directory and the XAPPL files must be located in the same directory.
Configuring the Virtual Application
After you create the application snapshot, you can modify or optimize the configuration. For example, OpenOffice is a suite of applications; program entry points must be setup so each application can run individually.
Complete the following steps to get OpenOffice to function as a virtual application:
Set the Output File.
Configure the Startup Files (Jukeboxing).
Configure the Setup options.
Remove unused installation files (optional).
Setting the Output File Name
The Output File is the name of the virtual executable file or SVM that is created by Spoon Virtual Application Studio.
Complete the following steps to set the Output File:
Select Virtual Application.
Locate the Output group and select Browse.
Choose a location for the output and assign it a file name.
Startup Files (Jukeboxing)
The Startup File settings identify specific files that can be executed by the virtual application. These files can be started by launching the virtual application, launching it with command line parameters (see Specifying multiple startup files (Jukeboxing)), or launching it via registered shortcuts (see Configure Shortcuts).
Complete the following steps to configure Startup Files:
Select Virtual Application.
Locate the Output group and select the Multiple to open the Startup Files window.
The Start Files window displays all entry points for the application. If an entry point is missing for your application, you can add one by:
Using Start Files, enter the File location on the first line and select Enter.
Using Filesystem, locate the target file. Right-click on the file and select Add to Startup Files.
Command Line enables you to add parameters for each Startup File.
Trigger sets the command-line parameter that specifies which Startup File to launch.
Note: each Startup File must have a unique value for its Trigger field.
Select Auto Start for the Startup File that should run by default if no Trigger is passed to the virtual application.
Setup Options
When virtualizing suites such as OpenOffice you can create a setup file. Setup files generated by Spoon Virtual Application Studio are created using MSI setup file format. Spoon Virtual Application Studio setup files only install the virtual application and create file associations and shortcuts. No other installation functions are performed.
Note: Setup options also apply if the application is registered to the Microsoft Windows shell using the Spoon plugin (refer to Using the Spoon Console) or SpoonReg tool (refer Register Virtual Applications in the Windows Shell).
To create a setup file for the virtual application, the Output Location, Product Info, Installation Parameters, Shortcuts, and File Associations must be configured in Setup.
Output Location defines where the setup file is created.
Product Info is the metadata associated with the setup file. Product Info is displayed in the Add/ Remove Programs window. This information must be accurate.
Installation Parameters control how the virtual application is installed on the host system.
Shortcuts enable the end user to launch the application directly from the Microsoft Windows Start Menu, Desktop, and Sent To menus.
Output Location
Complete the following steps o define Output Location for the virtual application setup file:
From Setup select the MSI tree node. 
Select Browse and assign it a file name.
Select Automatically Generate MSI After Successful Build to automatically create the setup file after the build process.
Product Info
The following fields specify metadata associated with setup files and is visible in the Add/Remove Programs window. These fields are accessed from the MSI tree node under Setup.
Product Name: The name of the application.
Product Version: The version of the application.
Company Name: The name of the company that made the application.
Installation Parameters
Installation Parameters are accessed from the MSI tree node under Setup.
To install the virtual application for All Users, select the Install Application for All Users check box. When checked administrative privileges are required on the target system.
For Application Folder, the Company Name\Product Name must be entered. If neither is entered, the virtual application is installed under folders named "Company Name\Product Name".
To automatically update existing versions, select Automatically Upgrade Earlier Application Versions. This updates previous versions of the virtual executable. To use side-by-side installation, select Allow Side-by-Side Versions of the Same Application.
Creating Shortcuts
Although Studio automatically detects application shortcuts in the snapshot process, you can manually configure them as well.
Complete the following steps to manage shortcuts for the virtual application:
From Setup expand Shortcuts and select one of the shortcut destinations: Desktop, Programs Menu, or SendTo.
Select Add Shortcut and assign it a Name, a Target, an Icon, and enter any Arguments that must pass to the specific application. Existing Shortcuts can be changed or deleted by using Edit Shortcut or Remove.
Select Add Folder to create a shortcut folder for shortcut organization.
For more information refer to Configure Shortcuts.
File Associations
Although Studio automatically detects file associations in the snapshot process, you can manually configure them as well.
Complete the following steps to manage file associations:
From Setup expand ProgIds.
Select Add ProgId and enter ProgId and Description. Change or remove existing * ProgIds* by selecting Edit ProgId or Remove. When a verb is necessary for the ProgId, choose its node and select Add Verb. Enter the necessary information in the Create Verb window.
Expand Extensions.
Select Add Extension and enter the file Extension and associated ProgId. Enter the MIME Type for the association.
Removing Unnecessary Files From the Snapshot
Temporary installation files are created during application installation processes. These files are necessary for installation but not required for the virtual application to run.
In OpenOffice, installation files are created in the same directory from which the install executable was executed.
Complete the following steps to remove these files from the snapshot:
Open Filesystem.
Navigate to the location of the installation files, right-click the folder, and select Delete.
Note: For OpenOffice, removing the installation files from the snapshot can reduce output virtual application binary size by up to 151 MB.
Build and Test
You can build and test a virtual application after it is configured, customized, and optimized.  
Complete the following steps to build the virtual application:
Select Build or Build and Run. This creates the virtual application binary file where Output File is defined. The build process can take a few minutes.
The MSI setup file is created at a separate location defined by Output Location (when the steps to automatically create one were followed).
Complete the following steps to test the virtual application:
Execute the virtual application binary file. The OpenOffice splash screen displays and the OpenOffice Quickstarter opens.
Execute the virtual application binary file from a command prompt with the "swriter" Trigger. For example, run "openoffice.exe swriter" from a command prompt and the OpenOffice Writer application opens instead of the Quickstarter.
Complete the following steps to test the Setup options:
Execute the setup file on a system without OpenOffice installed. The virtual application, shortcuts and file associations are installed on the host system.
Open the OpenOffice Writer Program from the Start Menu shortcut.
Open a file associated with the OpenOffice Writer program. 

## Building Microsoft Office with the Template Wizard or Desktop Scan ##

Building Microsoft Office with the Template Wizard
The template wizard is a fast and easy way to build Microsoft Office. Use the following steps to build your version of Microsoft Office for upload to Spoon Server, or for your desktop.
To use the Template Wizard, the version of Office that you wish to package must be installed on the machine being used.
Start Spoon Virtual Application Studio. If the configuration wizard does not open on startup, click the Configuration Wizard button in the Virtual Application menu bar.
Click the Build a virtual application from a template button. This will launch the template wizard.
Spoon Virtual Application Studio will then attempt to connect to the Spoon servers to download the latest list of available templates to build from.
Select the version of Office that you have installed from the drop down list. Be sure you select the correct version and language for your installation, click Next.
Spoon Virtual Application Studio will then ask to download the current configuration for Microsoft Office. Click Next to download the configuration, or recipe.
Next, Spoon Virtual Application Studio will import the information from your local installation to be built. Click Next to start the import.
With Office template builds, the next screen asks which version of the mail client (Outlook) should be the default. Selecting the virtualized client will use the packaged Outlook as the default mail handler. Alternately, the local version of Outlook, or any other installed mail client can remain the default by selecting "Use the default mail client settings from the host machine". Click Next.
Select the output file for the build. Click Next to open the file browser window. Name the file (default is MSOffice.exe) and place it in the desired location. Click Save to proceed.
Finally, there are checkboxes for saving the configuration about to be built, building and running the application. Click Finish.
If selected, the build process will begin, the exe will be created. Click OK when completed to be returned to the main window, with the configuration already loaded.
Packaging Microsoft Office 2010 for use in Spoon Server
Spoon recommends using the Desktop Scan wizard when packaging Microsoft Office for use in Spoon Server. The following is a step by step walkthrough for packaging Microsoft Office 2010 by using the Desktop Scan wizard.
Ensure that Microsoft Office is installed on the platform that it is intended to be used on. For example, if the virtualized version of Office will be run on Windows 7 32-bit, have Office installed on a Windows 7 32bit machine. If you are using 32 bit Microsoft Office on a 64 bit version of Windows, it is recommended to use a 32 bit virtual machine for this process.
Start Spoon Virtual Application Studio. If the configuration wizard does not open on startup, click the Configuration Wizard button in the Virtual Application menu bar.
Click the Scan desktop for installed applications button. This will launch the desktop scan process.
After the scan completes, press Next to match the results against the Spoon database of known applications. It is possible to review the information that is being sent to the Spoon servers at this point.
A list of matching applications will display. Select the version of Microsoft Office that matches the version and language of the local installation. If no version of Office is listed, verify the installation of Office. Selecting multiple applications will not effect the Office package process. Press the Next button
Select the location for the finished package. For Windows Vista and Windows 7, the default location is C:\Users\USERNAME\My Documents\Spoon.
Click Next to start the package process. Spoon Virtual Application Studio will download the needed information and use the files and registry items on the local machine to build a Microsoft Office package.
When the process completes, a success or failure message will display. With a successful build, a .spoon file is created for easy uploading to Spoon Server.
