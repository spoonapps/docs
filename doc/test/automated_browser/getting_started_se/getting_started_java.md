# Getting Started: Java

## What You'll Need

- An IDE or text editor, such as IntelliJ or Eclipse. 
- An existing Selenium script or project. If you do not have an existing script, you can use the example script provided in the **Eclipse** IDE on the [Selenium IDEs](http://spoonium.net/ides). 
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

Open your test in your favorite IDE or text editor.

At the top of your test, you'll need to import a couple of classes from the `org.openqa.selenium.remote` package.

	import org.openqa.selenium.remote.DesiredCapabilities;
	import org.openqa.selenium.remote.RemoteWebDriver;

Now, find the line in your test where you start the `RemoteWebDriver`. It probably looks like this:

	WebDriver driver = new FirefoxDriver();

First, we'll add a line above that to create a new `DesiredCapabilities` object. This is what hub uses to determine which browser to test against. We'll then configure it to run against Firefox. For more information on configuring your tests to run against different browsers, see the Configuring Capabilities section, below.

	DesiredCapabilities capabilities = new DesiredCapabilities();
	capabilities.setCapability(CapabilityType.BROWSER_NAME, "firefox");

Instead of using a browser-specific driver, you'll need to use the `RemoteWebDriver`. So change the line where you start the driver to:

	WebDriver driver = new RemoteWebDriver(new URL("http://localhost:4444/wd/hub"), capabilities);

That's it! Your test is ready to run on Spoonium.

## Configuring Capabilities

When using Selenium Grid, all of your tests are sent to a central **hub** before they are distributed to the proper **node** (browser) for that test.

To determine which node to send the test to, the hub uses the test's `DesiredCapabilities`. When using Spoonium, you'll need to specify these for each test.

The `DesiredCapabilities` class is part of the `org.openqa.selenium.remote package`, so make sure you've added an import statement for this class before starting.

Then, create the `DesiredCapabilities` object and use the `setCapability` method to declare which browser and version you wish to test against.

	DesiredCapabilities capabilities = new DesiredCapabilities(); //create the DesiredCapabilities object
	capabilities.setCapability(CapabilityType.BROWSER_NAME, "firefox"); //test against firefox
	capabilities.setCapability(CapabilityType.VERSION, "30"); //want to test against version 30 of firefox

If you want to test against Chrome or Internet Explorer, change the second line to:

	capabilities.setCapability(CapabilityType.BrowserName, "chrome"); //chrome

or

	capabilities.setCapability(CapabilityType.BrowserName, "internet explorer"); //internet explorer

To better memorialize your test, you can also use `DesiredCapabilities` to give your test a unique, descriptive name.

To name your test, add this line of code between the creation of your test's `DesiredCapabilities` and the start of the `RemoteWebDriver`:

	capabilities.setCapability("name", "Your test's name here");
