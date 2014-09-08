## Transitioning from Docker

Aside from Spoonium supporting Windows applications and services, there are some other fundamental differences between the technologies. This section highlights the major differences.

### Default Isolation

When a container is created, it is given a read-only view into the host device's file system and registry and any changes are written to the container's sandbox. This allows virtual applications to interact with the host device yet prevent any changes which could alter the system configuration. 

Network settings and port assignments are undisturbed from the application's configuration outside the container. To change the configuration or block ports, the `--route-add`, `--route-block`, and `--hosts` flags for the `run` command can be used.

Isolation from the host device only applies to processes which are created from within the container. Existing applications or system services will not be isolated nor are their interactions with processes inside the container. For example, executing an MSI installer package will result in an application being installed to the host device as the MSI file is processed by a Windows system service. In this case, using Spoon IDE to **snapshot** the installation process is recommended.
