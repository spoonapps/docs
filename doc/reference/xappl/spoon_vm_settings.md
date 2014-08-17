# Spoon VM Settings

## Overview

The behavior of containers and images can be modified by enabling or disabling different settings of the **Spoon VM**. 

VM settings can be enabled or disabled for a using the `--enable=VALUE` or `--disable=VALUE` flags of the `spoon run` command. 

These settings can also be applied to images using the `--enable=VALUE` and `--disable=VALUE` flags of the `spoon build` command. 

By default, all Spoon VM settings are *disabled*. 

**Note**: The VM settings of a container will override those of the base image(s). 

## Available Settings

#### SpawnVM

**Default Value**: Enabled

**Persisted to Images**: Yes

All child processes of containerized processes are, by default, launched inside the container. To disable this so that child processes launch on the native system, specify `--disable=SpawnVm` at `run` or `build` time. 

#### ReadOnly

**Default Value**: Disabled

**Persisted to Images**: Yes

#### SuppressLogging

**Default Value**: Disabled

**Persisted to Images**: Yes

#### AccurateFolders

**Default Value**: Disabled

**Persisted to Images**: Yes

#### SpawnComServers

**Default Value**: Disabled

**Persisted to Images**: Yes

COM servers are, by default, created outside the virtual environment. This allows COM communication between containerized processes and native applications. 

When this setting is enabled, COM servers will be spawned within the container. 

#### IsolateWindowsClasses

**Default Value**: Disabled

**Persisted to Images**: Yes

Enabling this setting prevents a containerized process from viewing window classes that are registered by external processes. You can use this to prevent interaction between containerized and non-containerized versions of the same program when the application checks for existing class registrations. 

#### IndicateVirtualization

**Default Value**: Disabled

**Persisted to Images**: No

#### ReadShare

**Default Value**: Disabled

**Persisted to Images**: Yes

This setting forces any files opened within the container to open with the `READ_SHARE` flag. Enabling this setting may help resolve compatibility issues caused by sharing violations. 

#### DRMCompat

**Default Value**: Disabled

**Persisted to Images**: Yes

The `DRMCompat` setting enables additional compatibility with common DRM systems, such as Armadillo. 

#### ShutdownProcTree

**Default Value**: Disabled

**Persisted to Images**: Yes

Enabling this setting will shutdown all child processes in the container when the root process exits. 

#### DEPCompat

**Default Value**: Disabled

**Persisted to Images**: Yes

This setting enables compatibility for systems with Data Execution Protection (DEP) enabled. Enable this setting for containerized applications running on Windows 2003. 

#### IndicateElevated

**Default Value**: Disabled

**Persisted to Images**: Yes

Enabling the `IndicateElevated` setting will force an application to run as if it has elevated security privileges, even if the application does not. Enabling this setting will also eliminate UAC security prompts for elevation and subsequent application crashes. 

#### SuppressInjection

**Default Value**: Disabled

**Persisted to Images**: Yes

The `SuppressInjection` flag disables DLL injection from occurring within the container. 

#### FaultExecutables

**Default Value**: Disabled

**Persisted to Images**: Yes

#### HonorWow6464Access

**Default Value**: Disabled

**Persisted to Images**: Yes

#### SuppressPopups

**Default Value**: Disabled

Enabling this setting will suppress any error popups that the Windows operating system generates during application runtime. 

#### HideShellWindow

**Default Value**: Disabled

**Persisted to Images**: Yes



#### PeriodicRegFlush

**Default Value**: Disabled

**Persisted to Images**: No

When enabled, the registry in the container will be periodically "flushed." 

#### EnableDiagnostics

**Default Value**: Disabled

**Persisted to Images**: Yes

When enabled, the `EnableDiagnostics` flag will persist diagnostic logging to an image. 

#### ForceWriteCopyIsolation

**Default Value**: Enabled

**Persisted to Images**: No

  

#### EnableCrashLogging

**Default Value**: Disabled
**Persisted to Images**: No

Enabling this setting turns on crash logging within the Spoon VM. 

#### AttachConsole

**Default Value**: Disabled

**Persisted to Images**: No

Enabling this process will attach the console to the root process of the container. 

#### MergePathEnvVars

**Default Value**: Disabled

**Persisted to Images**: No

When enabled, this flag will cause all of the `PATH` variables for a set of merged Spoon images to be merged together (instead of overriding one another). 

#### MergeVmSettings

**Default Value**: Disabled

**Persisted to Images**: No