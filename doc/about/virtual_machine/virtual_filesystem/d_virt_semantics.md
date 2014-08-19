# Virtualization Semantics

In the event of a conflict between a file in the virtual filesystem and a file present on the host device, the file in the virtual filesystem takes precedence.

Folders may be virtualized in **Full**, **Merge**, **Write Copy**, or **Hide** mode.

- **Full**: Full mode is used when a complete level of virtual application isolation is your desired outcome. Only files in the virtual filesystem are visible to the application, even if a corresponding directory exists on the host device, and writes are redirected to the sandbox data area.
- **Merge**: Merge mode is generally used when some level of interaction with the host device is your desired outcome. For example, **Merge** mode can be used to enable the virtualized application to write to the host device's **My Documents** folder. Files present in a virtual folder are merged with files in the corresponding directory on the host machine, if such a directory exists. Writes to host files are passed through to the host device and writes to virtual files are redirected into the sandbox data area. 
- **Write Copy**: Write Copy mode is used when a virtual application must be read from files already present on the host device, but isolation of the host device is still desired. Files present on the host device are visible to the virtual environment, but any modifications to folder contents are redirected to the sandbox data area. 

**Note**: *Write Copy* isolation is the default isolation mode for all files and folders in Spoon containers. 

- **Hide**: Hide mode is used when a file on the host machine could interfere with the application's ability to run properly. By adding a file or folder with Hide enabled, the application receives a File Not Found message, even if the file or folder exists on the host machine. Files and folders with Hide enabled will return a File Not Found message to the application at runtime. This applies to both the virtual filesystem and the host file system. 

**Spoon IDE Tip**: To apply selected isolation modes to all subfolders, right-click on the folder, choose Isolation, select the checkbox for Apply to Subfolders, then select OK.