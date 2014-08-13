# Adapting Tests from Other Services

If you've used another cloud-based Selenium service in the past, switching over to Spoonium is as easy as switching a couple of lines of code. 

## BrowserStack

When switching from BrowserStack, you'll need to make 2 changes to your existing code: 

1. Delete the `browserstack.user` and `browserstack.key` capabilities from your test's capabilities, along with any other BrowserStack-specific commands or libraries. 
2. Change the `RemoteWebDriver` hub URL to `http://localhost:4444/wd/hub`. 

See below for language-specific instructions. 

#### Java

Find the section of your test where the test's `DesiredCapabilities` are created. It should look, roughly, like this: 

	DesiredCapabilities caps = new DesiredCapabilities.firefox();
	caps.setCapability("browserstack.user, "your-username");
	caps.setCapability("browserstack.key", "your-browserstack-key");
	
	RemoteWebDriver driver = new RemoteWebDriver(new URL("http://hub.browserstack.com/wd/hub/"), caps);

To adapt your script for Spoonium, delete the BrowserStack-specific capabilities and change the hub URL to `http://localhost:4444/wd/hub`. 

	DesiredCapabilities caps = new DesiredCapabilities.firefox();
	
	RemoteWebDriver driver = new RemoteWebDriver(new URL("http://localhost:4444/wd/hub"), caps);

If you were using a username-specific hub URL(i.e. `http://username:key@hub.browserstack.com/wd/hub`) instead of `DesiredCapabilities`, you only need to change the hub URL in your tests to `http://localhost:4444/wd/hub`. 

#### C# 

Find the section of your test where the tests `DesiredCapabilities` are created. It should look, roughly, like this: 

	DesiredCapabilities caps = new DesiredCapabilities.Firefox();
	caps.SetCapability("browserstack.user", "your-username");
	caps.SetCapability("browserstack.key", "your-browserstack-key");

	IWebDriver driver = new RemoteWebDriver(new Uri("http://hub.browserstack.com/wd/hub/"), caps);

To adapt your script for Spoonium, delete the BrowserStack-specific capabilities and change the hub URL to `http://localhost:4444/wd/hub`. 

	DesiredCapabilities caps = new DesiredCapabilities.Firefox();
	
	IWebDriver driver = new RemoteWebDriver(new Uri("http://localhost:4444/wd/hub"), caps);

If you were using a username-specific hub URL(i.e. `http://username:key@hub.browserstack.com/wd/hub`) instead of `DesiredCapabilities`, you only need to change the hub URL in your tests to `http://localhost:4444/wd/hub`. 

#### Python

Find the section of your test where the tests `desired_capabilities` are created. If probably looks something like this: 

	capabilities = desired_capabilities.FIREFOX
	
	self.driver = webdriver.Remote(desired_capabilities=capabilities, command_executor="http://USERNAME:ACCESSKEY@hub.browserstack.com/wd/hub")

To switch to Spoonium, change the `command_executor` to `http://localhost:4444/wd/hub`. 

	capabilities = desired_capabilities.FIREFOX

	self.driver = webdriver.Remote(desired_capabilities=capabilities, command_executor="http://localhost:4444/wd/hub")

## Sauce Labs

Sauce Labs provides 2 means of authentication when sending tests to their cloud server. If you are passing in your username and access key as `DesiredCapabilities`, you'll need to delete those capabilities and change the hub URL to `http://localhost:4444/wd/hub`. 

If you are using the user-specific hub URL (`http://USERNAME:ACCESSKEY@ondemand.saucelabs.com:80/wd/hub`), change this to `http://localhost:4444/wd/hub` and you're ready to go!

For language-specific instructions, see below: 

#### Java

Find the section of your test where the test's `DesiredCapabilities` are specified and the `RemoteWebDriver` is started. It probably looks something like this: 

	DesiredCapabilities caps = new DesiredCapabilities.firefox();
	caps.setCapability("username", "your-username");
	caps.setCapability("accessKey", "your-saucelabs-key");
	
	RemoteWebDriver driver = new RemoteWebDriver(new URL("http://ondemand.saucelabs.com:80/wd/hub"), caps);

or this: 

	DesiredCapabilities caps = new DesiredCapabilities.firefox();

	RemoteWebDriver driver = new RemoteWebDriver(new URL("http://your-username:your-saucelabs-key@ondemand.saucelabs.com:80/wd/hub), caps);

To adapt your script to Spoonium, change this section so that there aren't any Sauce Labs-specific capabilities, and change the hub URL to `http://localhost:4444/wd/hub`. 

	DesiredCapabilities caps = new DesiredCapabilities.firefox();

	RemoteWebDriver driver = new RemoteWebDriver(new URL("http://localhost:4444/wd/hub"), caps); 

#### C# 

Find the section of your test where the test's `DesiredCapabilities` are specified and the `RemoteWebDriver` is started. It probably looks something like this: 

	DesiredCapabilities caps = new DesiredCapabilities.Firefox();
	caps.SetCapability("username", "your-username");
	caps.SetCapability("accessKey", "your-saucelabs-key");
	
	IWebDriver driver = new RemoteWebDriver(new Uri("http://ondemand.saucelabs.com:80/wd/hub"), caps);

or this: 

	DesiredCapabilities caps = new DesiredCapabilities.Firefox();

	IWebDriver driver = new RemoteWebDriver(new Uri("http://your-username:your-saucelabs-key@ondemand.saucelabs.com:80/wd/hub), caps);

To adapt your script to Spoonium, change this section so that there aren't any Sauce Labs-specific capabilities, and change the hub URL to `http://localhost:4444/wd/hub`. 

	DesiredCapabilities caps = new DesiredCapabilities.Firefox();

	IWebDriver driver = new RemoteWebDriver(new Uri("http://localhost:4444/wd/hub"), caps); 

#### Python

Find the section of your test where the `desired_capabilities` are specified and the `webdriver.Remote` is started. It should look similar to this: 

	capabilities = desired_capabilities.FIREFOX

	self.driver = webdriver.Remote(desired_capabilities=capabilities, command_executor="http://USERNAME:ACCESSKEY@ondemand.saucelabs.com:80/wd/hub")

To switch to Spoonium, change the `command_executor` to `http://localhost:4444/wd/hub`. 

	capabilities = desired_capabilities.FIREFOX

	self.driver = webdriver.Remote(desired_capabilities=capabilities, command_executor="http://localhost:4444/wd/hub")

## Testing Bot

Similar to other cloud-based Selenium services, Testing Bot uses Selenium's `DesiredCapabilities` object as a means of authentication. When switching to Spoonium, you'll need to delete the `api_key` and `api_secret` capabilities from all of your tests - they are not necessary in Spoonium.

Testing Bot also offers their own, specialized version of the regular Selenium `RemoteWebDriver`, `TestingBotDriver` which offers extension methods for interacting with the Testing Bot API. While this driver will work with Spoonium, we recommend changing all references to `TestingBotDriver` to `RemoteWebDriver` - this also means you can remove any internal dependencies on Testing Bot code.

Note: if you were previously using any of the extension methods provided by the `TestingBotDriver`, those should also be removed from your code, as they may lead to unexpected results.

In addition to deleting Testing Bot-specific capabilities, you must also change the hub URL for your tests. Whereas the hub for Testing Bot is `http://hub.testingbot.com:4444/wd/hub`, for Spoonium the hub is `http://localhost:4444/wd/hub`.

For language-specific instructions on adapting your Testing Bot tests for Spoonium, see below.

#### Java

Find the section of your code where you create the `DesiredCapabilities` and start the `RemoteWebDriver`. It probably looks something like this: 

	DesiredCapabilities caps = new DesiredCapabilities.firefox();
	caps.setCapability("api_key", "your-api-key");
	caps.setCapability("api_secret", "your-api-secret");

	RemoteWebDriver driver = new RemoteWebDriver(new URL("http://hub.testingbot.com:4444/wd/hub"), caps);

To adapt your script to Spoonium, change this section so that there aren't any Testing Bot-specific capabilities, and change the hub URL to `http://localhost:4444/wd/hub`. 

You should also remove any methods that interact with the Testing Bot API. 

#### C# 

Find the section of your code where the test's `DesiredCapabilities` are created and the `RemoteWebDriver` is started. It probably looks something like this: 

	DesiredCapabilities caps = new DesiredCapabilities.Firefox();
	caps.SetCapability("api_key", "your-api-key");
	caps.SetCapability("api_secret", "your-api-secret");
	  
	driver = new RemoteWebDriver(new Uri("http://hub.testingbot.com:4444/wd/hub"), caps);

To adapt your script to Spoonium, change this section so that there aren't any Testing Bot-specific capabilities, and change the hub URL to `http://localhost:4444/wd/hub`. 

	DesiredCapabilities caps = new DesiredCapabilities.Firefox();
  
	driver = new RemoteWebDriver(new URL("http://localhost:4444/wd/hub"), caps);

You should also remove any methods that interact with the Testing Bot API. 
