# Virtualization Semantics

In the event of a conflict between a key or value in the virtual filesystem and data present on the host device registry, information in the virtual registry takes precedence. Keys may be virtualized in Full, Merge, Write Copy, or Hide mode.

- **Full**: In Full mode, values only in the virtual registry are visible to the application, even if a corresponding key exists on the host device, and writes are redirected to the user registry area.
- **Merge**: In Merge mode, values present in a virtual key are merged with values in the corresponding key on the host machine (if such a key exists). Writes to host keys are passed through to the host registry and writes to virtual keys are redirected to the user registry area.
- **Write Copy**: Write Copy mode is used when a virtual application must be read from registry keys already present on the host device, but isolation of the host device is still desired. Keys and values present on the host device are visible to the virtual environment, but any modifications to keys or values are redirected to the sandbox data area. 
- **Hide**: Keys and values in the virtual registry or the corresponding host registry will not be found by the application at runtime.

**Spoon IDE Tip**: To apply selected isolation modes to all subkeys, right-click on the key, choose **Isolation**, and select the checkbox for **Apply to Subkeys**. Click OK. 