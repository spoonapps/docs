## To Hub

The Hub is an online repository for Spoon images and provides a central location to archive and distribute applications. Once an application is packaged into a Spoon image using the IDE or the command line tool, the image can be pushed to the Hub and made available publicly or privately to a specified set of users.  

Images are pushed to the Hub using the command line tool. The most common scenario is to create a container via the command line, commit the container to your local registry and then push the image to the Hub. However, it's also possible to start with an SVM output from the IDE and push that to the Hub. Read below for details on each scenario.

#### SVMs

Here is an example of how you would deploy an SVM to the Hub.

```
#Import the SVM into your local registry with the name "myimage"
> spoon import -n=myimage svm \\path\to\app.svm

#Verify that the image is now in your local registry
> spoon images

#Push the image to the Hub
> spoon push myimage
```
Once the push is complete you can verify that the image is available on the Hub by going to the [Hub](/hub) in your browser.

#### Containers

Here is an example of how you would push a container to the Hub.

```
#Create a container with Java, Node and Git support
> spoon run spoonbrew/jdk;spoonbrew/node;spoonbrew/git

#Shutdown the container by typing exit into the new command window
> exit

#Get the container id for the last container
> spoon containers -l

#Commit the container to your local registry
> spoon commit 922e myimage

#Verify that the image is now in your local registry
> spoon images

#Push the image to the Hub
> spoon push myimage
```
Once the push is complete you can verify that the image is available on the Hub by going to the [Hub](/hub) in your browser.