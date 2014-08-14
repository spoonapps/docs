## Spoon IDE Overview ##

Spoon IDE enables you to convert your Windows, .NET, Java, AIR, Flash, Shockwave, or other Windows-compatible applications into self-contained virtual applications. These applications are streamed from the web and run instantly on end-user devices. Unlike traditional deployment methods, virtual applications do not require reboots, administrative privileges, or separate setup steps for external components and runtimes. Virtual applications are isolated from other system applications, preventing DLL conflicts and other deployment nightmares.

## What is a Virtual Application? ##
Virtual applications enable application publishers and IT administrators to significantly reduce the cost and complexity associated with development, setup, configuration, deployment, and maintenance of software applications. A virtual application is a virtual machine image pre-configured with files, registry data, settings, components, runtimes, and other dependencies required for a specific application to execute immediately. This virtual application improves both the user experience and reduces test and support complexity associated with deploying the application. For example, a publisher of an application based on the Microsoft .NET Framework or Java runtime engine can create a virtual application combining the application with the required runtime engine. An end-user can then run this application immediately, even if he has an incompatible (or has not installed the) runtime engine.
 
Because virtual applications run in isolated environments, applications that otherwise interfere with one another can run simultaneously. For example, applications which overwrite system DLLs or require different runtime engine versions can run concurrently on a single host device. Virtual applications can also provide access to internal copies of privileged system resources, enabling unprivileged users to directly execute applications without security exceptions or Windows Vista User Account Control prompts.

Spoon virtual application technology surpasses other virtualization systems in several ways:


- Spoon virtual applications run immediately on an end-user machine without changes to system infrastructure. No "player" software or separate installation is required.  
- Spoon low-overhead virtualization technology enables applications to run with the same performance characteristics as native executables. No significant processing or filesystem overhead is incurred.
- Spoon virtual applications provide all required virtualized operating system functionality within the internal virtual environment. No operating system must be installed onto the virtual application.

## Spoon IDE Features Overview ##

Spoon IDE enables you to:

- Create virtual applications which are streamed from the web, eliminating potentially long installation and download times. Virtual applications run from any desktop with broadband internet access.

- Create an application as a single executable. Application files, registry settings, runtimes, and components are packaged into a single executable that runs instantaneously.

- Run Java and .NET without separate runtime installations. Java and/or .NET-based applications run immediately, with no separate installation steps or runtime versioning conflicts. 

- Improve desktop security. You can run applications without granting administrative permissions to end-users. You can also stabilize desktop images by deploying applications in Spoon sandboxed virtual environments.

- Eliminate third-party setup dependencies. Spoon integrates third-party components, COM/VB controls, and content viewers such as Acrobat, Flash, and Shockwave, directly into your application.

- Eliminate Windows Vista and Windows 7 User Account Control prompts and compatibility errors. You can deploy 
Spoon virtual applications regardless of access to privileged system resources.

- Leverage Terminal Services and Citrix investments. By isolating applications from global resource areas, Spoon virtual application technology allows non-compliant applications to function properly in Terminal 
Server and Citrix environments.

- Improve mobile productivity. By placing Spoon virtual applications onto a USB flash-memory drive, you can run applications immediately on remote PCs, with no installation steps, administrative privileges or driver installations.

- Dramatically reduce test and support costs. Spoon virtual applications eliminate versioning conflicts, dependencies, and "DLL Hell." Spoon applications also reduce test complexity and eliminate support requests associated with dependency installation and inter-application resource conflicts. Spoon virtualization takes place entirely in user-mode, so no device drivers are installed or required.

## How Does Spoon Virtualization Differ from Hardware Virtualization? ##

Unlike hardware virtualization systems like Microsoft Virtual PC and VMware, Spoon virtualizes only the operating system features required for application execution. This enables virtualized applications to operate efficiently, with the same performance characteristics as native executables.

There are several advantages in choosing Spoon virtual applications over hardware virtualization systems:

- Optimal performance. Spoon virtual applications run at the same speed as applications running natively against the host hardware, with a minimal memory footprint. In contrast, applications running within hardware-virtualized environments experience significant slow-downs and impose a large memory footprint.

- Dramatically reduced application size. Spoon virtual applications require a footprint proportional to the size of the virtualized application, data, and included components. As a result, Spoon virtual applications are small enough to be quickly downloaded by end-users. Hardware virtualization requires an entire host operating system image, including many basic subsystems that are already present on the end-user device. Each virtual machine may occupy several gigabytes of storage.

- Multiple virtual applications capability. You can run multiple simultaneous Spoon virtual environments per processor. Due to the high overhead of hardware virtualization, only a small number of hardware-virtualized environments per processor can run simultaneously.

- Reduced licensing costs. Spoon does not require the purchase of separate operating system licenses to use a virtual application. Hardware virtualization systems require a host operating system in order to function, which can impose additional licensing costs and restrictions.

Hardware virtualization can be appropriate in certain specialized scenarios:

- Non-Windows operating systems. Spoon virtual applications currently run only using the Windows operating system. Hardware virtualization can execute any operating system compatible with the underlying virtualized hardware, such as Linux.

- Kernel mode virtualization. The Spoon Virtual Operating System only virtualizes user-mode operating system features, whereas hardware virtualization systems emulate the entire OS stack, including kernel mode components. Applications requiring device drivers or other non-user-mode software may require a hardware-virtualized environment to function properly.

Carefully evaluate the advantages and disadvantages of different virtualization approaches before deciding which technology best fits your needs.

## What Platforms are Supported? ##
Spoon IDE supports the following platforms for virtual application build, snapshotting, and execution:

- Microsoft Windows 8.1
- Microsoft Windows 8
- Microsoft Windows Server 2012
- Microsoft Windows 7
- Microsoft Windows Server 2008, all editions
- Microsoft Windows Server 2003, all editions
- Microsoft Windows Vista, all editions
- Microsoft Windows XP Professional
- Microsoft Windows Embedded XP
- Microsoft Windows 2000 Professional
- Microsoft Windows 2000 Server

Spoon IDE supports both 32- and 64-bit applications. Both 32-bit (under 32-bit mode) and 64-bit executables can be run on x64-based platforms.

Spoon IDE supports these operating systems running within VMware and Microsoft hardware virtualization and hypervisor environments. Spoon IDE has limited support for the Windows Preinstallation Environment (WinPE), though certain applications (depending on operating system features unavailable in WinPE) may not function properly.

**Note:** Spoon IDE does not support creation of 16-bit executables. To run 16-bit DOS applications, virtualize an appropriate emulator with the application and launch the application through the emulator.

## What Applications Can Be Virtualized Using Spoon IDE? ##

Spoon IDE and the Spoon virtualization engine support most major Windows desktop applications. However, certain applications are unsuitable for virtualization using Spoon's user-mode technology. These include application features which contain, or directly depend upon, interaction with specialized kernel-mode device drivers or other kernel-mode extensions, operating system components and extensions, anti-virus applications, and kernel event filtering, monitoring, and intrusion detection applications. Spoon applications are compatible with most major anti-virus, runtime, and security packages.