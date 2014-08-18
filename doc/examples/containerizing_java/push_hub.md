# Push to the Spoonium Hub

We'll finish this tutorial by explaining how the newly created `simple-java-webserver` can be uploaded to the [Spoonium Hub](http://spoonium.net/hub), where it can be made publicly available or shared with other collaborators. 

This can be especially useful when working in development teams that need to share work with each other. When you push an image to the Spoonium Hub, it creates a new repository for it (if one doesn't already exist) under your account. The repository page is then viewable from the URL: **http://spoonium.net/hub/{username}/{repo name**. This repository will be public, by default. 

 To push an image, execute the `spoon push` command from your local command prompt. The `push` command takes two parameters: the repository to push to and the name of the image to push. 

In this case, we'll push to a repository named **java-webserver**. 

	>spoon push java-webserver simple-java-webserver:master

**Note**: If you tagged your image in the previous section, use the command: `spoon push java-webserver simple-java-webserver:1.0`. 