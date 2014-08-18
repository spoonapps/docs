# About

Through the Spoon IDE, you can embed a *virtual filesystem* into an application container. Embedded files are accessible by your Spoon-processed application as if they were present in the actual filesystem. 

Virtual files, unlike files on the host device, are not visible from and do not require changes to the host device. 

Virtual files do not require security privileges on the host device, regardless of whether the virtual files reside in a privileged directory. Because virtual files are embedded in the application executable, shared DLLs do not interfere with or are overwritten by other applications on the host device.