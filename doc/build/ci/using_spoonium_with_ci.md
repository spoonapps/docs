## Why ##

Create automated, clean, and consistent test environments with Spoonium while keeping the Continuous Integration (CI) server free from conflict causing dependencies.

Existing CI servers may have many varying libraries, runtimes, custom settings, and applications, possibly in different languages and versions, that are required for the various automated builds.  Sometimes these dependencies collide to create inconsistent test environments and headaches when configuring automated builds. 

With Spoonium no installed dependencies are required on the CI server.  Instead all dependencies are built into containers providing consistent environments and a dependency free CI server.  This eliminates the possibility of dependency collision and makes automated build configuration very simple. 

## How ##

The basic steps for integrating Spoonium into a CI server are to create a Spoon.me script, integrate it into an automated build on a CI server, and finally run/test the container.

### Create Spoon.me script ###

The Spoon.me script contains all the steps necessary to build the container.  Here is an example:

    from spoonbrew/node spoonbrew/git
    cmd mkdir c:\root
    cmd git clone https://github.com/project/repo c:\root
    cmd cd c:\root\server & npm install

The `FROM` instruction creates a new container from the specified images.  In this example a container is being created using the `node` and `git` images from the Spoonbrew repository on [https://spoonium.net/](https://spoonium.net/).

The `CMD` instructions execute the specified commands inside the container.  In this example the directory `c:\root` is being created, a Github repository is being cloned to `c:\root`, and `npm install` is being run to install the node app.

See the [Syntax](#Syntax_for_.me_Scripts) page for more information on Spoon.me script instructions.

### Integrate into the CI server ###

Once the Spoon.me script is created the next step is to configure an automated build on the CI server that will execute the Spoon.me script and create the container.  This step includes configuring the necessary triggers, schedules, notifications, etc. and will vary between CI servers.

Next a build step needs to be created in the automated build that will execute the following commands:

    spn login <spoonium account> <spoonium password>
    spn build -n <container name> Spoon.me
    spn export <container name> c:\root\image.svm
    spn rmi <container name>

The `login` command is necessary if images from a Spoonium repository are specified.  If only local images are specified then this step can be skipped.

The `build` command executes the Spoon.me script and builds a new container.

The `export` command exports the container as an image and copies it to a file location.

The `rmi` command removes the local image created by the build script.  Images can be quite large and can us a large amount of disk space if left on the local system.

**Note:**  Spoonium images can also be pushed to a Spoonium Hub repository on [https://spoonium.net/](https://spoonium.net/) with the `push` command.  Here is an example that would replace the export command in the previous example:

    spn push <container name>:master

See the [Command Line Interface](#command_line_interface) page for more information on `spn` commands.

### Run the container ###

The final step is to `pull`/`import` the image and run it.  

If the image was exported to an SVM use these commands to import and run:

    spn import -n <container name> image.svm
    spn run local/<container name> cmd.exe

If the image was pushed to the Spoonium Hub use these commands to pull and run:

    spn pull <account name>/<container name>
    spn run <account name>/<container name> cmd.exe
