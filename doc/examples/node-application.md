## Containerizing a Node.js Application ##

The goal of this example is to show you how to create a Spoon container of a `Node.js` application that can be run on any Windows system with zero configuration.

In this example you will containerize `aIRChat`, an open source IRC client, create an image and and add your image to the Spoonium hub. 

From the hub, other users can run the image or pull it into their local repository to make changes. Let's get started!

### Login to your Spoonium account ###

If you haven't already done so, create an account on the [Spoonium website](http://spoonium.com) and install the Spoon Console. The Spoon Console includes the Spoon command-line tool.

Open a command prompt and log in to your Spoonium account using the login command:

    >spoon login <username> <password>

### Add application dependencies to your local repository ###

Before creating the container for `aIRChat`, we will add a couple of images to the local repository. These images are available in the standard library of containers on the Spoonium hub as part of the Spoon Brew images. For `aIRChat` we will need the `Node.js` image and the `Git` image. 

Use the `pull` command to add the images to the local repository.

    >spoon pull git 
    downloading http://start.spoon.net/Layers/git/1-9-4-0__0/git.xlayer...
    pull complete
    
    >spoon pull node 
    downloading http://start.spoon.net/Layers/nodejs/0-10-29-0__0/nodejs.xlayer...
    pull complete

After adding the images to the local repository, check the list of local images to make sure it looks correct using the `images` command.

    >spoon images

    NAME  				SIZE 		CREATED
    spoonbrew/git 		32.1MB   	7/16/2014 3:44:27 PM
    spoonbrew/node		10.2MB   	7/16/2014 3:45:10 PM
    
### Start the container ###
Now that the images are available, start a new container that includes the `Node.js` and `Git` images using the `run` command and specify the start-up file `cmd`.

    >spoon run git;node cmd
    downloading http://start.spoon.net/Layers/XVM/11-6-200-0__1/XVM.exe...

This will launch a command prompt that is running in the container. Now we will configure the `aIRChat` application in the container.

### Configure the project in the container ###

In the new command window running inside the container, we can now set up the project. Let's create a folder where we can clone the `aIRChat` project.

    >cd C:\
	>mkdir projects
	>cd projects

Clone the project by using the command `git clone`.

    >git clone https://github.com/redwire/airchat.git
    Cloning into 'airchat'...
    remote: Reusing existing pack: 2983, done.
    remote: Counting objects: 21, done.
    remote: Compressing objects: 100% (18/18), done.
    Receiving objects:  99% (remote: Total 3004 (delta 9), reused 0 (delta 0)
    Receiving objects: 100% (3004/3004), 8.84MiB | 948.00 KiB/s, done.
    Resolving deltas: 100% (1302/1302), done.
    Checking connectivity... done.

The `aIRChat` project is now in the container. To confirm, we can run `aIRChat` in the container.

    >cd .\airchat\Content
    >npm install
    ...lots of installs...
    >node app.js
    connect.multipart() will be removed in connect 3.0
    visit https://github.com/senchalabs/connect/wiki/Connect-3.0 for alternatives
    connect.limit() will be removed in connect 3.0
    Express server listening on port 3000

`aIRChat` is now running on port 3000.  Open a browser and go to [http://localhost:3000](http://localhost:3000) to confirm. 

After verifying that `aIRChat` is up and running, stop the `Node.js` server by hitting `Ctrl+C`.

### Saving the container to the local repository ###

Shutting down the container will automatically save the state of the container and assign it an ID in your local repository. To shutdown the container use the `exit` command in the command window of the container.

    >exit

The alpha-numeric ID will be output to the command window where the container was launched.

    1be755fcfafc4cf0b8e1c0667f6d13f0

To verify the container information, us the `ps` command.

    >spoon ps
 
    ID  								IMAGES 							COMMAND   						CREATED
    1be755fcfafc4cf0b8e1c0667f6d13f0	spoonbrew/git,spoonbrew/node   	C:\Windows\System32\cmd.exe   	7/16/2014 3:54:59 PM
    
If you need to access the container again to make changes you can start it in it's current state using the `spoon start` command followed by the ID.

    >spoon start 1be755fcfafc4cf0b8e1c0667f6d13f0

When the container is configured and ready to be pushed to the Spoonium hub, commit the changes to a named image using the `spoon commit` command. 

    >spoon commit 1be755fcfafc4cf0b8e1c0667f6d13f0 airchat
    decomposing spoonbrew/git...
    decomposing spoonbrew/node...
    merging base images...
    commit complete

Run the `spoon images` command to confirm that your container was saved as a new image. Note that the name of the image corresponds to the name provided in the `spoon commit` command.

    >spoon images

    NAME  				SIZE 			CREATED
    local/airchat 		120.8MB  		7/16/2014 4:05:12 PM
    spoonbrew/git 		32.1MB   		7/16/2014 3:44:27 PM
    spoonbrew/node		10.2MB   		7/16/2014 3:45:10 PM

### Pushing the container ###

To push your container up to the Spoonium Hub, run the `spoon push`.

    >spoon push airchat
    uploading https://io.spoon.net/users/spoonuser/hub/airchat...
    push complete

When the push is complete, re-run the `spoon images` command to verify that the image is no longer in the local repository, but now is available on the Spoonium hub.

Other Spoonium users will now be able to pull down your image and run the container with your saved changes. Any user can pull the container and run it without doing any configuration.

    >spoon images
     
    NAME  				SIZE 			CREATED
    spoonbrew/git 		32.1MB   		7/16/2014 3:44:27 PM
    spoonbrew/node		10.2MB   		7/16/2014 3:45:10 PM
    spoonuser/airchat 	120.8MB  		7/16/2014 4:05:12 PM

### Verify your new image on the Spoonium Hub ###    

Visit http://spoonium.net/hub to see the details of the image you just pushed.

### Create a Spoon.me file for aIRChat ###

Another way to configure containers is to use a `Spoon.me` file. This is a simple way to script the process from above and is more like writing a batch file instead of typing commands into a command window.

In a text editor, create a new file and copy and paste the text below.

    from spoonbrew/git spoonbrew/node
    cmd mkdir C:\projects\airchat
    cmd git clone https://github.com/redwire/airchat C:\projects\airchat
    cmd cd C:\projects\airchat\content & npm install

Name the file spoon.me and save it in directory of your choice. For example, `C:\spoon\aIRChat`.

### Build the Image ###

Open a new command prompt. Enter the command, below with the path to the directory where you saved the `spoon.me` file.

    >spoon build -t=aIRChat C:\spoon\aIRChat

### Run it! ###

Now that you've built the image, you can run it with the `spoon run` command. 

    >spoon run local/aIRChat node C:\projects\aIRChat\content\app.js
