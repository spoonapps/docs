## Working with IDE

Spoon IDE is a desktop application that allows users to convert any Windows application to a containerized virtual application or an image compatible with [CLI](/docs/reference/command+line) and [Hub](/docs/hub).

Unlike the command line interface, IDE has a graphical user interface. Similar to CLI, IDE is a tool for managing images and containerized virtual applications.

The GUI allows users to more easily edit complex configurations for images and virtual applications that may require complicated settings. IDE saves these configurations in XAPPL files. Read more about XAPPL files and their format [here](/docs/reference/xappl).

Once created with IDE, CLI builds these XAPPL files into images that you can push to the Spoonium Hub. Click [here](/docs/build#working+with+images) for a specific example.

IDE also provides two unique methods for creating images and virtual applications:

1. **Desktop scan for installed applications**: This option will scan your desktop for installed applications and build an image or virtual application using content and settings from the desktop.

2. **Snapshot an application or component**: In this method, snapshots capture the system state before and after an application is installed. Based on the observed system changes, the virtual application settings are automatically configured. This method is ideal for virtualizing off-the-shelf applications or ones that use complex MSI installer packages that would be incompatible with CLI.

IDE offers a user interface to manage custom images and virtual applications as well as additional creation methods not available in CLI.

#### System requirements and download

IDE runs on any Windows operating system. Download a free 30-day trial [here](http://spoon.net/studio).