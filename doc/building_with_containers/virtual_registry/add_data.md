# Add Registry Data

## Spoon IDE

Complete the following steps to add virtual registry data:

- Select the Registry button located on the left side of the Spoon IDE window.
- Add or remove the registry keys and values you want to embed in the application executable. When adding blob data, enter the values in hexadecimal format.

The **Classes** root, **Current User** root, **Local Machine**, and **Users** root folders correspond to the **HKEY_CLASSES_ROOT**, **HKEY_CURRENT_USER**, **HKEY_LOCAL_MACHINE**, and **HKEY_USERS** keys on the host machine.

Registry string values can include well-known variables such as **@WINDIR@** and **@PROGRAMFILES@**.