# Introduction

In this tutorial, we'll walk you through how to create and containerize a basic web application. We'll also show you how to automate the creation of new images of your web application using **Spoon.me** scripts and walk you through some of the basics of the Spoonium containerization network stack. 

#### Topics Covered

- The basic container/image creation path
- Copying local files into a container
- Automating image creation with Spoon.me scripts
- The Spoonium network stack

## Create the App

For this tutorial, we'll be using Python 2.7 and the [Flask](http://flask.pocoo.org/) microframework. 

To begin, create a new directory on your local machine, we'll call it `C:\node`. 

Create a new file in this directory named `hello.py`. Add the following script to this file: 

	from flask import Flask
	app = Flask(__name__)

	@app.route("/")
	def hello():
		return "Hello World!"

	if __name__ == "__main__":
		app.run()

Believe it or not, that's it! If you have Python installed locally, you can test out your app by running: `python hello.py`. (Note: you must install `Flask` first -- `pip install Flask`).

## Create a Container

Next, we'll containerize our application. Containers run on top of base images, which provide any underlying dependencies for our application. 

Since our example application uses Python, we'll need a Python image. Luckily, the **spoonbrew** account provides a basic Python image we can use. Grab the image from the Spoonium hub by logging in to the Spoon IDE in the command prompt and running `spoon pull spoonbrew/python`. 

The `spoonbrew/python` image is the "vanilla" Python install on Windows - so it doesn't have `pip` or `distribute` installed. 