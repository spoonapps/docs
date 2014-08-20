## Getting Started: C# 

#### What You'll Need

- An IDE or text editor, such as Visual Studio or MonoDevelop.
- An existing Selenium script or project. If you do not have an existing script, you can use the example script provided in the **SharpDevelop** IDE on the [Selenium IDEs](http://spoonium.net/ides). 
- A web browser open to [http://spoonium.net/selenium](http://spoonium.net/selenium).
- The Spoon browser plugin. 

#### Starting the Spoonium Hub

In your web browser, click the **Start Grid** button in the top-left corner of the page. A buffering dialog will appear on your desktop. When the buffering dialog completes, check the **Hub** window on the page. When the Spoonium hub is ready, this output will appear in the window: 

	Jun 26, 2014 3:21:23 PM org.openqa.grid.selenium.GridLauncher main
	INFO: Launching a selenium grid server
	2014-06-26 15:21:24.064:INFO:osjs.Server:jetty-7.x.y-SNAPSHOT
	2014-06-26 15:21:24.088:INFO:osjsh.ContextHandler:started o.s.j.s.ServletContextHandler{/,null}
	2014-06-26 15:21:24.094:INFO:osjs.AbstractConnector:Started SocketConnector@0.0.0.0:4444

#### Adapting Your Test

Open your test in your favorite IDE or text editor. 

At the top of your test, you'll need to add a `using` directive for the `OpenQA.Selenium.Remote` namespace, if it's not already referenced. 

	using OpenQA.Selenium.Remote;

Now, find the line in your test where the `RemoteWebDriver` is started. It probably looks like this: 

	IWebdriver driver = new FirefoxDriver();

First, we'll add a line above this to create `DesiredCapabilities` for the test. These are used by the hub to determine which browser to run the test against. We'll then configure the test to run against Firefox. For more information on configuring your tests to run against different browsers, see the `Configuring Capabilities` section, below. 

	ICapabilities capabilities = new DesiredCapabilities();
	capabilities.SetCapability(CapabilityType.BrowserName, "firefox");

Instead of using a browser-specific driver, you'll need to use the `RemoteWebDriver`. Change the line where you start the driver to: 

	IWebDriver driver = new RemoteWebDriver(new Uri("http://localhost:4444/wd/hub"), capabilities);

That's it! Your test is now ready to run on Spoonium!

#### Configuring Capabilities

When using Selenium Grid, all of your tests are sent to a central **hub**, which then distributes them to the proper **node** (browser) for that test. 

To determine which node to send the test to (which browser to test on), the hub uses the test's `DesiredCapabilities`. When using Spoonium, you'll need to specify these for each test. 

The `DesiredCapabilities` class is part of the `OpenQA.Selenium.Remote` namespace, so make sure you've added a `using` directive for this namespace before beginning. 

Then, create the `DesiredCapabilities` instance and use the `SetCapability` method to declare which browser and version you wish to test against. 

	ICapabilities capabilities = new DesiredCapabilities();
	capabilities.SetCapability(CapabilityType.BrowserName, "firefox");
	capabilities.SetCapability(CapabilityType.Version, "30");

For command capabilities, such as the browser and version to test against, Selenium provides a `CapabilityType` class.  For less-common, or browser-specific, capabilities, capabilities can be specified as strings. For example, we can specify a capability `name` with value `test name` by using: 

	capabilities.SetCapability("name", "test name");

Spoonium supports some capabilities outside of the standard Selenium capabilities. 

Tests can be named using the `name` capability. To give your test a name, add the following line to your test between the creation of the test's `DesiredCapabilities` and the start of the `RemoteWebDriver`. 

	capabilities.SetCapability("name", "Your test's name here");