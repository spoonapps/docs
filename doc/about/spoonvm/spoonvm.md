## Virtual Machine

The backbone of Spoonium is the **Spoon Virtual Machine**. It's a lightweight implementation of core operating system APIs, including the filesystem, registry, process, and threading subsystems, within the Windows user-mode space. Applications executing within the Spoon VM interact with a virtualized filesystem, registry, and process environment, rather than the host machine.

The virtualization engine handles requests within the VM internally or routes requests to the host device filesystem and registry if appropriate. It performs these actions according to the virtual application configuration.

The Spoon VM supports merge, override, write-copy, and hide isolation modes between the virtual and host filesystem and registry. These settings are available for directories as well as individual files.

The virtualization engine dynamically remaps shell folder paths so that proper application behaviour is preserved across various client operating systems. Similarly, registry key values containing explicit path names or prefixes are dynamically remapped to the appropriate values for each host device. A generalized multi-platform virtualization layer dynamically adapts virtual machine behavior based on the endpoint platform.

In addition to desktop applications, the VM supports virtualization of system services such as web servers and local database engines, component object model (COM) servers, and network services such as DNS. The VM also supports advanced operating system features including kernel object namespace isolation and side-by-side (SxS) manifests.

The Spoon virtual microkernel has been optimized to produce negligible storage and runtime performance overhead. Spoon's local caching feature can be adjusted from zero to full local caching, even allowing large numbers of applications to be used from storage-constrained thin client devices.