## Continuous Integration

Create automated, clean, and consistent test environments with Spoon while keeping the Continuous Integration (CI) 
server free from conflict causing dependencies.

Existing CI servers may have many varying libraries, runtimes, custom settings, and applications, possibly in different languages and versions, that are required for the various automated builds.  Sometimes these dependencies collide to create inconsistent test environments and headaches when configuring automated builds. 

With Spoon no installed dependencies are required on the CI server. All dependencies are built into containers providing consistent environments and a dependency-free CI server.  This eliminates the possibility of dependency collision and makes automated build configuration very simple.

The basic steps for integrating Spoon into a CI server are to create a SpoonScript, integrate it into an automated build on a CI server, and finally run and test the container.

### Create SpoonScript

The SpoonScript contains all the steps necessary to build the container.

```
# Creates a new container from the specified images
FROM spoonbrew/node spoonbrew/git

# Clone a project in the container
CMD mkdir c:\root
CMD git clone https://github.com/project/repo c:\root

# Install Node.js depencies 
CMD cd c:\root\server & npm install
```

Save your script as a `.me` file. See the [SpoonScript reference](/docs/reference/SpoonScript) for more information on SpoonScript script instructions.

### Integrate into the CI server

The next step is to configure an automated build on the CI server that will execute the SpoonScript and create an image.  You'll need to configure the necessary triggers, schedules, notifications, etc., which will vary between CI servers.

Now add the follow commands to your automated CI build script:

```
# Log in if images from a hub repository are specified
spoon login <username> <password>

# Execute the SpoonScript and build a new image
spoon build -n=<name> C:\path\to\spoon.me

# Export the image to a location on the host system
spoon export <name> c:\root\image.svm
```

Rather than exporting the image to the host system, you can also `spoon push` the image to the hub where other users could pull it down and test.

See the [Command Line Interface](/docs/reference/command-line) page for more information on `spoon` commands.

### Run the container

```
# First import the image to your local registry
> spoon import -n=<name> C:\root\image.svm

# Run the image
> spoon run <name> <command>
```

If you alternately pushed to the hub then use these commands to pull and run:

```
> spoon pull <account name>/<name>
> spoon run <account name>/<name> <command>
```