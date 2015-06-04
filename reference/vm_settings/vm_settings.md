## VM Settings

The behaviour of containers and images can be modified by changing **Spoon VM** settings.

Effect the settings flags below using the `--enable=VALUE` or `--disable=VALUE` flags with the `spoon run` or `spoon build` command.

    # Example
    spoon run --enable=IsolateWindowsClasses node cmd

Altering VM settings for a container will override the settings of the base image(s).

|| **Flag** || **Default** || **Persisted to Images** || **Behavior** ||
|| **DEPCompat** || Disabled || Yes || Enables compatibility for systems with Data Execution Protection (DEP) enabled. Enable this setting for containerized applications running on Windows 2003. ||
|| **DRMCompat** || Disabled || Yes || Enables additional compatibility with common DRM systems such as Armadillo. ||
|| **FaultExecutables** || Disabled || Yes || Forces all executable files to be faulted into the application container. ||
|| **HonorWow6464Access** || Enabled || Yes || Grants registry access to 32-bit applications snapshotted and running on 64-bit operating systems. ||
|| **IndicateElevated** || Disabled || Yes || Forces an application to run as if it has elevated security privileges even if the application does not. Enabling this setting will also eliminate UAC security prompts for elevation and subsequent application crashes. ||
|| **IsolateWindowsClasses** || Enabled || Yes || Prevents a containerized process from viewing window classes that are registered by external processes. You can use this to prevent interaction between containerized and non-containerized versions of the same program when the application checks for existing class registrations. ||
|| **PeriodicRegFlush** || Disabled || No || Enables a container's registry to be periodically flushed to disk storage. ||
|| **ReadOnly** || Disabled || Yes || Any attempts to write to a file or registry value will result in an access denied error code. ||
|| **ReadShare** || Disabled || Yes || Forces any files opened within the container to open with the `READ_SHARE` flag. Enabling this setting may help resolve compatibility issues caused by sharing violations. ||
|| **ShutdownProcTree** || Disabled || Yes || Forces all child processes in the container to shutdown when the root process exits. ||
|| **SpawnComServers** || Enabled || Yes || Forces any COM servers to be isolated from the host device. By default, COM servers are created outside the virtual environment to allow COM communication between containerized processes and native applications. ||
|| **SpawnVM** || Enabled || Yes || Forces all child processes of a container to be launched inside the container with access to the virtual environment. ||
|| **SuppressPopups** || Enabled || Yes || Suppresses any error popup dialogs that the virtual environment generates during application runtime. ||
