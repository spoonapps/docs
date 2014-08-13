# Getting Started: Python

## What You'll Need

- An IDE or text editor, such as PyCharm or IDLE. 
- An existing Selenium script or project. If you do not have an existing script, you can use the example script provided in the **IDLE** IDE on the [Selenium IDEs](http://spoonium.net/ides). 
- A web browser open to [http://spoonium.net/selenium](http://spoonium.net/selenium).
- The Spoon browser plugin. 

## Starting the Spoonium Hub

In your web browser, click the **Start Grid** button in the top-left corner of the page. A buffering dialog will appear on your desktop. When the buffering dialog completes, check the **Hub** window on the page. When the Spoonium hub is ready, this output will appear in the window: 

	Jun 26, 2014 3:21:23 PM org.openqa.grid.selenium.GridLauncher main
	INFO: Launching a selenium grid server
	2014-06-26 15:21:24.064:INFO:osjs.Server:jetty-7.x.y-SNAPSHOT
	2014-06-26 15:21:24.088:INFO:osjsh.ContextHandler:started o.s.j.s.ServletContextHandler{/,null}
	2014-06-26 15:21:24.094:INFO:osjs.AbstractConnector:Started SocketConnector@0.0.0.0:4444

## Adapting Your Test

At this point, you should have a test open in an IDE or text editor. 

If it's not already imported into your script, make sure you've imported the `webdriver` module from the `selenium` package. 

	from selenium import webdriver

To access the `desired_capabilities` class, you'll also need to import `webdriver.common`: 

	from selenium import webdriver.common

First, we'll add a line above that to create a new `desired_capabilities` object. This is what hub uses to determine which browser to test against. We'll then configure it to run against Firefox. For more information on configuring your tests to run against different browsers, see the **Configuring Capabilities** section, below.

	capabilities = desired_capabilities.FIREFOX

Instead of using a browser-specific driver, you'll need to use `webdriver.Remote`. Change the line where you start the driver to: 

	self.driver = new webdriver.Remote(command_executor="http://localhost:4444/wd/hub", desired_capabilities=capabilities)

That's it! Your test is ready to run on Spoonium. 

## Configuring Capabilities

When using Selenium Grid, all of your tests are sent to a central **hub** before they are distributed to the proper **node** (browser) for that test. 

To determine which node to send the test to, the hub uses the test's `desired_capabilities`. When using Spoonium, you'll need to specify these for each test. 

To specify the browser you want to test against, use the `desired_capabilities` object, which has fields for each browser. 

For Firefox, use: 

	caps = desired_capabilities.FIREFOX

Likewise, for Chrome or Internet Explorer, use: 

	caps = desired_capabilities.CHROME

or 

	caps = desired_capabilities.INTERNETEXPLORER


Desired Capabilities in Python are really just Python dictionaries. You can specify further capabilities, such as version, through the standard Python dictionary syntax. 

	caps['version'] = '31'

Spoonium also supports naming your tests. You can name a test using the `desired_capabilities` object with a `name` key and specifying a string value.  

	caps['name'] = 'the name of your test'