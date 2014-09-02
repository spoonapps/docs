### enable

The **enable** instruction enables the specified VM setting inside the container. 

```
enable <vm setting>
```

Only one setting can be enabled per instruction. To enable multiple VM settings, use multiple **enable** instructions. 

#### VM Settings

**SpawnVm** - Any child process which is launched inside the container will have access to the container's virtual environment. This is enabled by default.
**ReadOnly** - Any attempts to write to a file or registry value will result in an access denied error code.
**SpawnComServers** - Starts COM servers in the virtual environment, isolated from the host device.
**IsolateWindowsClasses** - Isolates windows classes which have been registered via the ::RegisterClass or ::RegisterClassEx Windows APIs. For example, this allows a virtualized Firefox instance to run while a non-virtualized instance is running.
**ReadShare** - Forces all file create or open operations to implicitly include the read share permission.
**DRMCompat** - Enables runtime compatibilty for some DRM solutions which may fail without.
**ShutdownProcTree** - Causes all child process to be killed automatically if the initial process is exited.
**DEPCompat** - Provides additional compatibility for legacy applications on DEP-enabled platforms.
**IndicateElevated** - Causes the applications in the container to believe they are running in an elevated security context.
**HonorWow6464Access** - Allows 32bit applications to gain access to the 64bit-specific registry and filesystem.
**SuppressPopups** - Prevents any error messages from being display in popup dialogs. This is enabled by default.
**HideShellWindow** - Prevents applications in the container from retrieving a handle to the desktop's shell window.
**ForceWriteCopyIsolation** - Forces all directories and keys with **merge** isolation to be **write copy** isolation. This is enabled by default.