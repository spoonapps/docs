Spoonium leverages containerization to offer solutions for testing browsers, applications, and servers.

Spoonium is a solution for both manual and automated browser testing. With our manual testing, you can run any version of any browser in a container or build a custom browser container with components like Java and Flash. Our automated testing solution allows you to run tests with [Selenium](http://seleniumhq.org) on our web-based Selenium Grid that utilizes our browser containers on your local machine to minimize your testing environment setup.

For other applications and servers, our containers can make testing your project's latest builds easier by making them more portable and more efficient. As we learned in the [Build](/docs/build) section, images created with the command-line interface or IDE capture the state of a container at a specific time. This allows you to create and push specific builds or versions of your project that your testers can pull and test without any setup. This makes Spoonium a useful tool for continuous integration and nightly beta build testing.

## Manual Browser Testing

Spoonium offers 2 tools for manual browser testing.

<!--TODO: revise all this when the new templating goes into place for these tools -->

#### Browser Sandbox

[http://spoonium.net/manual](http://spoonium.net/manual)

The Spoonium.net Browser Sandbox makes cross-browser and backwards compatibility testing easy. Just click Run for any browser to launch it instantly.

Browsers run within an isolated virtual environment, eliminating the need for installs and allowing legacy browsers such as Internet Explorer 6 to run on Windows 7 and 8.

Virtualized browsers behave exactly like installed browsers. And because they run locally, you can test web applications hosted on your own development machine or on internal servers. Simply launch the browser from Spoon.net or the Spoon Console and enter your test URL in the navigation bar.

Spoon.net supports standard browser components like Java applets and ActiveX controls as well as popular browser plugins like Firebug, IE Developer Toolbar, and CSS and JavaScript debugging consoles. 

#### Browser Studio

[http://browserstudio.com](http://browserstudio.com)

Need to test a web application with a Java dependency? Want to see if Flash breaks your website? Browser Studio is Spoonium's three-step tool for creating custom browser environments. Pick your browser and version, pick the runtimes and plugins you need, and click **BUILD**. We'll create your custom test environment in minutes, and you can save your new browser for future use.