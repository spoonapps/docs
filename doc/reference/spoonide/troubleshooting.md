# Troubleshooting #
This section describes the most common configuration errors that occur when using Spoon IDE.

If you encounter a problem with a virtual application, please carefully read this section or query the online knowledge base before using other support options. It is very likely that the issue you have encountered is addressed in one of these places.


## Access Internet-based Resources ##
Several Spoon IDE features require access to Internet-based resources. These features may be unavailable if Spoon IDE is unable to connect to the Internet.
In many corporate environments, access to the Internet is filtered through a firewall or proxy server. In these cases, Spoon IDE attempts to automatically configure for Internet access. It may be necessary to manually configure the proxy server settings.
Complete the following steps to configure proxy server settings:
Select Proxy Settings from the Options menu. This displays the Proxy Settings dialog. 
Enter appropriate proxy server settings in the dialog. Consult your system administrator to obtain your proxy server settings.
For users not on a corporate network, it may be necessary to ensure that Windows Firewall is configured to allow an exception for Spoon IDE so the program can access our servers.
To add an exception to Windows Firewall (Windows Vista and Windows 7):
Open the Control Panel.
Select Windows Firewall.
Click the Allow a program or feature through Windows Firewall link.
In the popup window, find Spoon IDE and ensure the proper boxes are checked.
Click OK and close the window.
Note: If users are running a third-party antivirus or security software, and exception may need to be added to those programs as well. The exception process varries for each program.

## Generate Diagnostic Mode Virtual Applications ##
Sometimes errors from virtual application configuration result in an executable which fails to run properly. Errors are typically a result of a mistake in the virtualization configuration, such as a missing file or registry entry.
To assist in diagnosis of these problems, Spoon Studio offers the option of enabling diagnostic-mode. Diagnostic-mode executables generate logging data during execution that can assist in diagnosis of problems related to virtualization.
All executables can be run in diagnostic-mode by passing in a command-line argument, /XEnable=Diagnostics, or by using an environment variable, __VMDIAGNOSTICS=t. Alternatively, to generate an executable that will run in diagnostic-mode by default, select Generate Diagnostic Mode Executable in the Output section of Virtual Application. Select Build to generate the executable. This generates an xclog_<id>.txt file in the application startup directory that contains detailed diagnostic data gathered during execution. Inspection of this file, particularly of entries labeled WARNING or ERROR, often enables diagnosis of virtualization errors. If you require assistance from Spoon technical support to resolve your problem, submit this information along with your support request to facilitate a faster resolution.
Note: Because diagnostic-mode executables run significantly slower than standard executables, and generate very large log files, diagnostic-mode executables should not be distributed to your end-users except for diagnosing an issue.

## Spoon IDE FAQ ##

FAQ
Question/Issue
Solution
Why do I get a "File not found" error when I try and load my configuration?
This error shows when Spoon IDE cannot find one of the files referenced in your configuration. If your configuration file (XAPPL) has moved, ensure the Files folder is in the same relative location to the configuration as it was when it was created.




Why will my application not start after building?
There are several possible reasons why an application may fail to start. There are a few things you can check to get the application to run.
Verify you have the correct startup file selected.
If your application will not open on one Operating System, verify that it is the same on all available Operating Systems.
Create a diagnostic version of the application and look in the created logs for specific error messages. This can often provide a quick fix by letting you know exactly where the issue is.
If the virtual application will not run, but the native version does run, try building from the Capture and Diff snapshot without any changes. Does the application still start? If not, it is possible the application is not compatible and cannot be virtualized. If the application does launch, start removing the registry and filesystem items again and see if it still executes. Perhaps something needed was unintentionally removed.
I receive an error "Unable to contact server" when I try and build my application.
If you are including a runtime in your build, ensure you can access internet resources and Spoon IDE will download the needed runtime information in order to complete the build. For more information, see Access Internet-based Resources.
Why do I receive a connection error when I start my application?
There is a known issue with SQL 2005 where if the hard drive is compressed and the SQL 2005 Express Runtime is included in the virtual application, a connection error will display at startup. The only current workaround is to decompress the hard drive. More information can be found on MSDN here.




Why is my application unable to find a child process?
If your application cannot find child processes, check to see if Enable startup executable optimization is enabled. This can be found on the Settings menu under Process Configuration. Enable startup executable optimization is disabled by default. This means that there is a bootstrap process between your application and the host services. In this case, you may have a code statement that looks like this: 

ProcessserviceProcess = _GetProcessByNameAndParent ("sqlservr", Process.GetCurrentProcess ()); 

This statement will not return any results because of the bootstrap process. 
Editing the statement to the line below will allow you to look first to the parent process, the bootstrap application, and then find the child process you are wanting to modify. 

ProcessserviceProcess = _GetProcessByNameAndParent ("sqlservr", GetParentProcessOfCurrentProcess ());
I have Excel 2007 and Excel 2010. I tried adding both my Microsoft Office 2007 and Microsoft Office 2010 applications to my desktop in the same directory and they will not work. Why is that?
Microsoft Office 2007 and 2010 have some shared registry keys. Because of this, the applications are not able to be run in the same sandbox. This is the same as if you had both versions installed locally. In order to have both versions, you would need to different applications and ensure the sandbox path for each is unique. This applies to all Microsoft Office applications.
Why are the icons missing when I browse to open a file in the virtual application?
Some applications will place the icon references, or .ico files, in the c:\windows\installer folder. The snapshot process does not capture this folder as it contains many large files that are not required for the virtual application to run. If, when running your application, you attempt to open a file and you do not see the correct file type icon, you can manually add the needed reference files to the build in Spoon IDE. Go to Filesystem, select the Windows folder in the System Drive tree and click the New Folder button, name the folder Installer. Next, select the Installer folder and click Add Files. In the window that pops up, navigate to the icon (*.ico) files in the c:\windows\installer folder and click Open. This will add the needed icon resource files without adding additional large files to the application configuration.
I virtualized and added Outlook 2010 64 bit to my Desktop for use with GroupWise, and now Outlook 2010 will not start.
There is a known issue in GroupWise where it will not work with 64 bit versions of Outlook 2010. The error also occurs when both applications are installed locally.
Can I have a virtual mapped drive for my virtual application?
Yes, a virtual mapped drive can be added to your XAPPL file in the FileSystem section. This is not available in the Studio UI, but can be added manually in a text editor. Below is an example XML snippet for adding the virtual file X:\AppData\Settings.txt to the configuration. This would be inserted before the closing tag of the FileSystem section:
<Directory rootType="VirtualDrive" name="@DRIVE_X@" isolation="Merge">
    <Directory name="AppData" hide="False" readOnly="False" isolation="Full">
        <File name="Settings.txt" hide="False" readOnly="False" source=".\Files\X_Drive\AppData\Settings.txt" />
    </Directory>
</Directory>

In this example the drive is X:, but any drive letter can be specified in the @DRIVE_X@ variable where the letter after the underscore is the drive letter. It is important to remember that if the application is going to read from the drive, the entire path must be created and the file needs to be listed. The virtual mapped drive will not be visible in Windows Explorer or through File browse dialogs, but it will be visible via a command window or if the application does a file lookup using standard Windows APIs.