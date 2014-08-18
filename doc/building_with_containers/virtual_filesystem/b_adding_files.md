# Adding Files

Files can be added to a container's virtual filesystem through any of the built-in Windows command line file copying or moving utilities. When a file is copied or moved into the virtual filesystem, it is no longer visible to the host system. Any changes made to the file are written within the context of the application container and are not applied to the file on the host machine.

To illustrate this concept, we've included a brief walkthrough of this behavior, below.

## Command Line

Files can be added to a container from the Spoon CLI through any standard Windows file-copy utility (such as copy or xcopy).

Git repositories can also be cloned into a container using git. If git is installed on your native system, you can use git commands within the container. If you do not have git installed natively, you will need to add the **spoonbrew/git** image (or any other image containing Git) to your container.

#### Tutorial: Copying a file into the virtual environment

In this tutorial, we will copy a text file from your local machine into an application container's virtual filesystem and modify the contents of the newly-embedded text file, demonstrating the semantics of filesystem virtualization. 

1. Begin by creating a new text file on your desktop. 

	>echo Hello World! > hello.txt

2. Now, use the `spoon run` command to create a new, empty container. 

	>spoon run -a spoonbrew/scratch

3. Once inside the container, use the Windows file-copy utility `copy` to copy **hello.txt** from your native desktop to the root directory of the virtual filesystem. 

	(2a34d5c) >copy \path\to\hello.txt C:\
			1 files copied.

4. To confirm that the file was not added to your local `C:\` root, open File Explorer and navigate to `C:\`. To confirm the file was added to the container, enter the command `cd C:\` in the containerized command prompt. Then, use the `dir` command to list all the files and subdirectories in this directory. You should see `hello.txt` appear in the list. 

**Note**: The Spoon virtual filesystem does *not* support copying files from their location on the native filesystem to the same location on the virtual filesystem. 

For example, the following command will *not* copy a file into the container. 

	(2a34d5c) >copy \path\to\hello.txt \path\to

## Spoon IDE

Complete the following steps to add virtual files:

1. Select the **Filesystem** button located on the left side of the Spoon IDE window.
 
2. Add the files and folders you wish to embed in the container. The **Application Directory** represents the folder containing the virtual application binary on the executing device; the other root folders represent the corresponding folders on the host device.

**Note**: When running a virtual application on Windows 7, the **All Users Directory\Application Data**and **All Users Directory** root folders will map to the same folder at runtime. To prevent one setting from overriding another, verify that the isolation settings for these folders are the same.
