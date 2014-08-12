# Beginner Tutorial

Welcome to the wonderful world of Selenium testing!

In this guide, we'll walk you through how to run your first-ever Selenium test on Spoonium.
Starting a New Hub

## Starting a Hub
Let's start by firing up a new Hub. In Selenium, the hub receives test requests and commands, and distributes them to the appropriate browser.

To start the Spoonium hub, click the **START GRID** button on the [Selenium](http://spoonium.net/selenium) page. This will begin the streaming and provisioning process for the Spoonium hub.
When the hub is ready to begin receiving tests, you will see a few lines of output appear in the Selenium Hub window.

Once you see this, you're ready to test!

## Running a Test

Now that your hub is ready, you will need a test to run. We've provided ready-to-run sample tests in some example IDEs, available at [http://spoonium.net/ides](http://spoonium.net/ides).

For this tutorial, let's use the Python IDE, IDLE. Click **Python** on the IDEs page to run IDLE. When the IDE appears on your local machine, the example test will be ready to run. To run the test, click **Run** and then **Run Module**, or press **F5**. 

The hub will now add the browser(s) specified in your test to your Grid. When this occurs, you will see a buffering dialog on your screen with the name of the browser being added. Once added, the Spoonium hub will forward your test to this new browser and begin executing commands.

In a few seconds, a new browser window will appear on your screen. Don't touch it! That's the new virtual browser that will run through the example Selenium test. The browser will run through each command in the example test - examining page elements, clicking buttons, and submitting the form on the page. When the test is over, the browser will close automatically.

If you happen to touch the browser or select an element on the page, you may interfere with the running test - potentially causing the test to fail. If you would like to interact with the browser in the middle of the test, we suggest you put a breakpoint in your test script to do some interactive debugging.

## Next Steps

Now that you've seen the basic workflow for Spoonium,  as well as for general Selenium testing, we recommend you jump right into the code.

We've tried to leave some useful comments in each of the code samples in our Selenium IDEs. Feel free to play around by modifying the code to click, clear, or select any of the elements on our example page - [http://spoonium.net/example](http://spoonium.net/example).