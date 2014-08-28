## Working with Images

### Creating Images

There are four ways to create an image:

1. Commit a container
2. Automatically create with a build script
3. Build images from XAPPL configuration files created with IDE
4. Import and convert various file types to images

#### Commit a Container

```
# Before committing a container check that it is stopped
> spoon containers

# Then create a new image from the container
> spoon commit <container-id> <image-name>
```

See a more detailed example [here](http://spoonium.net/docs/build#working-with-containers).

#### Automatic Builds

You can automatically build images using a Spoon Script, which is a set of instructions that recreate the steps of configuring a container. See more information on [Spoon Script](/docs/reference#spoon-scripts) verbage and syntax.

```
# Example script to automatically build a 7-Zip image

# Pull dependency images
FROM spoonbrew/wget

# Prepare environmnet
CMD mkdir c:\7zip

# Download installation media
WORKDIR C:\7zip
CMD %spn_wget% http://downloads.sourceforge.net/sevenzip/7z920.exe

# Install 7-Zip
CMD 7z920.exe /S /D=C:\7zip
```

Save the script as a .me file and then use `spoon build` command:

```
# Build the script and specify a name for the new image
> spoon build -n=7-zip:9.20 C:\path\to\build.me

# New image is now saved in the local registry
> spoon images

NAME   TAG   ID            CREATED               SIZE
7-zip  9.20  95sdf1245239  8/18/2014 2:21:32 PM  25.4MB
```

#### Building from a XAPPL File

XAPPL files are static configuration files originally created using IDE that specify the files, registry keys, and virtual machine settings for an image. The CLI can also build images based on XAPPL configuration files using `spoon build` command.

```
# Build an image and specify a name
> spoon build -n=firefox:30 C:\path\to\firefox30.xappl
```

#### Import

If you have an existing image (file type `.svm`) on your local machine or a network drive (perhaps built with IDE or a legacy version of Spoon Studio), you can import it to your local registry.

```
# Specify the new name, file type, and path to the image
> spoon import -n=newimage svm C:\path\to\image.svm
```

If the image is not explicitly named, its ID will be used as a default.

The `import` command also supports building from 2 external file types:

1. Microsoft Software Installer (`.msi`)
2. ThinApp Configuration (`package.ini`)

Use the appropriate file type parameter:

```
# MSI
> spoon import msi <path to .msi>

# ThinApp configuration
> spoon import thinapp <path to package.ini> 
```

### Forking, Renaming, and Tagging

Images can be forked using the `spoon fork` command. This creates a link to the specified image with a new name and tag. It does not affect the original image.

```
# Pull an image
> spoon pull account/image:head

# Check the image
> spoon images

Name            Tag  ID            Created               Size
account/image   head 14wed2165141  8/18/2014 1:55:23 PM  1.9MB

# Fork to a new image name and tag
> spoon fork account/image:head tester/test1:1.0

# New image is added
> spoon images

Name            Tag  ID            Created               Size
account/image   head 14wed2165141  8/18/2014 1:55:23 PM  1.9MB
tester/test1    1.0  14wed2165141  8/18/2014 1:55:23 PM  1.9MB
```

The `spoon tag` command can also retag images.

```
# Specify the image you want to tag and the new tag
> spoon tag tester/test1:1.0 2.0

# Check the tag
> spoon images

Name            Tag  ID            Created               Size
account/image   head 14wed2165141  8/18/2014 1:55:23 PM  1.9MB
tester/test1    2.0  14wed2165141  8/18/2014 1:55:23 PM  1.9MB
```

### Push to a Remote Repository

Images in a local registry can be copied to a remote repository on the [hub](http://spoonium.net/hub) with the `spoon push` command to make your images available to your team members, end-users, or the public.

```
# Specify the image you want to push
> spoon push sample

# Or push to a specific namespace and tag
> spoon push spoontest/sample:latest
```

If unspecified, the image will be pushed to the logged-in user's namespace with the tag head.

For basic users, pushed images will be public by default. For paid users, pushed images will be private by default until the private repository limit is reached. Visit [the hub](http://spoonium.net/hub) to change these defaults.

See more information on [using the hub](http://spoonium.net/docs#hub).