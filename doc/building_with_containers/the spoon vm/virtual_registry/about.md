# The Virtual Registry

**Spoon IDE** enables you to embed a *virtual registry* into your executable. Embedded registry keys are accessible by your Spoon-processed application as if they were present in the actual registry. 

Unlike data present on the host device, virtual registry keys and values are not visible from and do not require changes to the host device. The use of a virtual registry does not require security privileges on the host device, even if the virtual registry entries are in a privileged section of the registry. 

Because virtual registry entries are embedded in the application executable, other applications are unable to disrupt application execution by inadvertent modification of registry entries.