# File Attributes

## Hidden

Files and folders can be hidden from shell browser  dialogs and other applications. This is used to prevent internal components and data files from being displayed to the user. To hide a file or folder, select the checkbox in the Hidden column adjacent to the desired file or folder.

**Note**: The **Hidden** flag is NOT the **Hide** isolation mode. Enabling the **Hidden** flag prevents a file or folder from displaying in shell browser dialogs or from directory enumeration APIs; it does not prevent the application (and potentially the end-user) from accessing the folder or file contents by direct binding. To prevent the file or folder from being found by the application, enable **Hide** isolation mode.

**Note**: Files and folders can only be marked as `hidden` in the Spoon IDE. 

## Read Only

Flagging files and folders as **read-only** prevents the application from modifying the file or folder contents. To make a file or folder read-only, select the checkbox in the **Read Only** column next to the desired file or folder.

#### Marking a Container as Read Only

To mark a container's filesystem as read-only, enable the `ReadOnly` VM setting at runtime. 

	>spoon run --enable=ReadOnly <image>