## VM Settings

The behaviour of containers and images can be modified by changing **Spoon VM** settings.

Effect the settings flags below using the `--enable=VALUE` or `--disable=VALUE` flags with the `spoon run` or `spoon build` command.

    # Example
    spoon run --enable=IsolateWindowsClasses node cmd

Altering VM settings for a container will override the settings of the base image(s).

|| **Flag** || **Default** || **Persisted to Images** || **Behavior** ||
|| **AttachConsole** || Disabled || No || Enabling this process will attach the console to the root process of the container. ||
|| **DEPCompat** || Disabled || Yes || This setting enables compatibility for systems with Data Execution Protection (DEP) enabled. Enable this setting for containerized applications running on Windows 2003. ||
|| **DRMCompat** || Disabled || Yes || The `DRMCompat` setting enables additional compatibility with common DRM systems, such as Armadillo. ||
|| **EnableCrashLogging** || Disabled || No || Enabling this setting turns on crash logging within the Spoon VM. ||
|| **EnableDiagnostics** || Disabled || Yes || When enabled, the `EnableDiagnostics` flag will persist diagnostic logging to an image. ||
|| **FaultExecutables** || Disabled || Yes || This option will force all executable files to be faulted into the application container. ||
|| **HonorWow6464Access** || Disabled || Yes || Grants registry access to 32-bit applications snapshotted and running on 64-bit operating systems. ||
|| **IndicateElevated** || Disabled || Yes || Enabling the `IndicateElevated` setting will force an application to run as if it has elevated security privileges, even if the application does not. Enabling this setting will also eliminate UAC security prompts for elevation and subsequent application crashes. ||
|| **IsolateWindowsClasses** || Disabled || Yes || Enabling this setting prevents a containerized process from viewing window classes that are registered by external processes. You can use this to prevent interaction between containerized and non-containerized versions of the same program when the application checks for existing class registrations. ||
|| **MergePathEnvVars** || Disabled || No || When enabled, this flag will cause all of the `PATH` variables for a set of merged Spoon images to be merged together (instead of overriding one another). ||
|| **MergeVmSettings** || Disabled || No ||  ||
|| **PeriodicRegFlush** || Disabled || No || When enabled, the registry in the container will be periodically purged. ||
|| **ReadOnly** || Disabled || Yes ||  ||
|| **ReadShare** || Disabled || Yes || This setting forces any files opened within the container to open with the `READ_SHARE` flag. Enabling this setting may help resolve compatibility issues caused by sharing violations. ||
|| **ShutdownProcTree** || Disabled || Yes || Enabling this setting will shutdown all child processes in the container when the root process exits. ||
|| **SpawnComServers** || Disabled || Yes || COM servers are, by default, created outside the virtual environment. This allows COM communication between containerized processes and native applications. When this setting is enabled, COM servers will be spawned within the container. ||
|| **SpawnVM** || Enabled || Yes || All child processes of containerized processes are, by default, launched inside the container. To disable this so that child processes launch on the native system, specify `--disable=SpawnVm` at `run` or `build` time. ||
|| **SuppressInjection** || Disabled || Yes || The `SuppressInjection` flag disables DLL injection from occurring within the container. ||
|| **SuppressLogging** || Disabled || Yes ||  ||
|| **SuppressPopups** || Disabled ||  || Enabling this setting will suppress any error popups that the Windows operating system generates during application runtime. ||