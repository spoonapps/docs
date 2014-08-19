# Integrating Spoonium with an Existing Grid

If you or your development team already have an in-house Selenium Grid, you can use Spoonium to "fill in the gaps" in your Grid to support browsers that you may not have the capacity or hardware to host internally.

For example, if your in-house Grid is only large enough to host and support the latest versions of each browser, you can use Spoonium to add legacy browsers to your Grid. 

After initial configuration and setup, the Spoonium hub will automatically provision and run tests on any browser that is not in your internal Grid.

## Setup Guide

The Spoonium hub has the same external API as the standard Selenium hub. You can connect external nodes to the Spoonium hub just like you would a normal Selenium hub.

1. Start the Spoonium hub
	1. *If using Spoonium as part of your CI process*: 
		1. Log on, or RDP in, to your build/test server (must be a Windows machine). 
		2. Open a web browser and navigate to [http://spoonium.net/selenium](http://spoonium.net/selenium). Log in with your Spoon.net username and password.
		3. Click **Start Grid** to start the Spoonium hub. If the Spoon.net plugin is not already installed, you will have to install it before Spoonium will start. 
	2. *If using Spoonium from a development machine*: Log in to [http://spoonium.net/selenium](http://spoonium.net/selenium) with your Spoon.net username and password. Click **Start Grid** and the Spoonium hub will start.
2. Connect your internal nodes to the Spoonium hub. 
	1. The hub will launch on port 4444 of the machine Spoonium was accessed from. You can connect to the hub from a remote node by executing the following command (from the remote node): `java -jar selenium-server-standalone-2.xx.y.jar -role node -hub http://hub-machine:4444/grid/register`. For more information on configuring nodes with additional command line parameters, see [the official Selenium Grid Documentation](https://code.google.com/p/selenium/wiki/Grid2). 

Once your Grid is configured, you can send your tests to it just as you normally would. If the hub cannot find a matching browser on your internal nodes, it will automatically provision a fresh browser from Spoonium.net and run the test on it.