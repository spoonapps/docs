# Containerizing Java

In this tutorial, we'll cover how to containerize a Java project and how to effectively use and configure Java within a Spoon container. 

#### Topics Covered

- The basic image creation workflow
- Configuring environment variables within a container
- Using git within a container

## Pull Required Dependencies

Before beginning, we'll get all of the dependencies we'll need to run and containerize the Java project. In this case, that means we'll need both `Java` and `Git` inside our container. Luckily, both of these images can be found in the `spoonbrew` account on the Spoonium hub. 

We'll start by issuing a `spoon pull` command for each of these dependencies. This will create local copies of these images for later use. 

	>spoon pull spoonbrew/jdk7
	>spoon pull spoonbrew/git

When both of these commands have completed, you can verify that they are indeed on your local system by running `spoon images`. 

	>spoon images

	NAME			SIZE		CREATED
	spoonbrew/git	32.1MB 		8/08/2014 5:09:11 PM
	spoonbrew/jdk7	43.2MB 		8/10/2014 10:00:32 AM


