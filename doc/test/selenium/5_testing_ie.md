## Testing Internet Explorer

When testing parallel instances of Internet Explorer on Spoonium, we recommend setting the following options in your test. 

1. Force Internet Explorer to use the `Create Process` API.
2. Launch Internet Explorer with the `-private` (for **Internet Explorer 8+** only)

Using these settings helps prevent cookies and other session-specific items from being shared between different instances of Internet Explorer. 

If you are not testing multiple instances of Internet Explorer in parallel, we recommend setting the `Ensure Clean Session` capability to `True`. 

#### Configuring Internet Explorer Options

See below for language-specific instructions for how to properly configure your Internet Explorer tests for Spoonium. 

**Java**

Before beginning, import the `org.openqa.selenium.ie` package, if you have not already. 

	import org.openqa.selenium.ie;

When setting `DesiredCapabilities` for your test, use the static `FORCE_CREATE_PROCESS` and `IE_SWITCHES` fields of the `InternetExplorerDriver` to create capabilities that will force IE to use Windows' Create Process API and to set the browser to **private** mode.

	DesiredCapabilities capabilities = DesiredCapabilities.ie();
	capabilities.setCapability(InternetExplorerDriver.FORCE_CREATE_PROCESS, true);
	capabilities.setCapability(InternetExplorerdriver.IE_SWITCHES, "-private");

**Note**: If testing serial instances of Internet Explorer (only 1 IE window open at a time), also add the `IE_ENSURE_CLEAN_SESSION` parameter to your capabilities. 

	capabilities.setCapability(InternetExplorerDriver.IE_ENSURE_CLEAN_SESSION, true);

**C#**

Before beginning, add a `using` directive for the `OpenQA.Selenium.IE`, if it is not already in your test. 

	using OpenQA.Selenium.IE;

The C# bindings contain an `InternetExplorerOptions` class that can be used to set and manipulate Internet Explorer-specific settings. 

In lieu of `DesiredCapabilities`, create a new instance of the `InternetExplorerOptions` class. 

	InternetExplorerOptions ieOptions = new InternetExplorerOptions();

This object has properties for all of the relevant settings we want to switch. 

	ieOptions.ForceCreateProcessApi = true
	ieOptions.BrowserCommandLineArguments = "-private";

If you want to specify a version of Internet Explorer to test against, use the `AddAdditionalCapability` method. 

	ieOptions.AddAdditionalCapability("version", "10");

When instantiating your test's `RemoteWebDriver`, pass the `InternetExplorerOptions` as the tests capabilities using the `InternetExplorerOptions.ToCapabilities()` method. 

	IWebDriver driver = new RemoteWebDriver(new Uri("http://localhost:4444/wd/hub"), ieOptions.ToCapabilities());

**Python**

Internet Explorer-specific capabilities can be specified as key-value pairs through the capabilities object. 

Start by creating a capabilities object for Internet Explorer. 

	capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER

Next, add two capabilities to force Internet Explorer to use Windows' Create Process API and to set the browser mode to **private**. 

	capabilities['ie.forceCreateProcessApi'] = True
	capabilities['ie.browserCommandLineArguments'] = '-private'

Finally, pass these capabilities as the `desired_capabilities` for the remote WebDriver. 

	driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", desired_capabilities=capabilities)

#### Internet Explorer Container Configuration

Spoonium's Internet Explorer containers are packaged and pre-configured to work with Selenium's Remote WebDriver without any end-user configuration. Each container is pre-configured with the following settings:

- Packaged with the latest IEDriverServer installed in the virtual environment's PATH.
- Protected Mode Enabled in all zones.

For Internet Explorer 10 and 11, Enhanced Protected Mode is Disabled.

For Internet Explorer 11, the following registry key has been added to the container:

- HKLM\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE with DWORD iexplore.exe and value 0.

For more information on these changes, as they relate to the InternetExplorerDriver, see [the Selenium documentation](https://code.google.com/p/selenium/wiki/InternetExplorerDriver).

#### Internet Explorer "Gotchas"

The InternetExplorerDriver in Selenium has some unique features that may cause unexpected test results. Below, we've compiled a list of some of the most commonly encountered "gotchas" we've seen testing Internet Explorer. 

- When testing Internet Explorer, the browser zoom level should always be left at 100%. The IEDriverServer relies on this zoom level for native mouse events - configuring the zoom to be greater or less than 100% may cause inadvertent failures in your tests.
- If you are using a hover command in your tests, do not place your mouse over the Internet Explorer window. Doing so causes the hover to fail.