# The Spoon VM

The heart of Spoonium is the **Spoon Virtual Machine**, a lightweight implementation of core operating system APIs, including the filesystem, registry, process, and threading subsystems, completely implemented within the Windows user-mode space. Applications executing within the Spoon virtual environment interact with a virtualized filesystem, registry, and process environment, rather than directly with the host device operating system. 

The virtualization engine handles requests within the virtualized environment internally or, when appropriate, routes requests to the host device filesystem and registry, possibly redirecting or overriding requests as determined by the virtual application configuration. 

The Spoon engine supports merge, override, write-copy, and hide isolation semantics, down to individual file and folder granularity. This allows virtual machine contents to be entirely isolated from, merged with, or hide corresponding locations on the host device. 

The Spoon virtualization engine dynamically remaps shell folder locations such as My Documents so that proper application behavior is preserved across client operating system versions. Similarly, registry key values containing explicit path names or prefixes are dynamically remapped to the appropriate values for the executing host device.

Spoon also supports virtualization of system services such as web servers and local database engines, component object model (COM) servers, and network services such as DNS. The Spoon virtual machine also virtualizes advanced operating system features including kernel object namespace isolation and side-by-side (SxS) manifests.

The Spoon virtual microkernel has been carefully optimized to add only negligible storage and runtime performance overhead. Spoon's local caching behavior can be adjusted from zero to full local caching, even allowing large numbers of applications to be used from storage-constrained thin client devices.

A cross-platform emulation layer allows many legacy applications and browsers to run properly on new operating systems such as Windows 7 and 8. A generalized multi-platform virtualization layer dynamically adapts virtual machine behavior based on the endpoint platform, allowing a **single universal binary to be deployed across all devices**.