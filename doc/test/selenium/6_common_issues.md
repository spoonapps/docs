## Common Issues and Troubleshooting

#### Cannot connect to the Spoonium Hub

Before proceeding, make sure the Spoonium hub is running on your local computer. You can check this by opening **Windows Task Manager** and checking the **Processes** tab for *SpooniumComponent.exe*. 

**Solution 1: Check your Firewall**: This issue may occur if your computer has a restrictive firewall that blocks incoming and outgoing connections to/from your computer. 

If possible, check your firewall and make sure port 4444 is not blocked. This is the port the Spoonium hub listens for commands on. If this port is blocked, it must be unblocked before using Spoonium.  

#### Cannot Launch the Spoonium Hub

Ensure that the Spoon Plugin is installed and running. The Spoon Plugin can be downloaded from [http://start.spoon.net/install](http://start.spoon.net/install). 

To run or restart the Spoon Plugin once installed, go to the **Start Menu** > **All Programs** > **Startup** and select **Spoon.net Sandbox Manager 3.33**. 

#### After clicking **Start Grid**, "Pending" appears but the Grid never launches

This issue occurs when the Spoon Plugin is not activate or installed. If you have not installed the Spoon Plugin, it can be downloaded from [http://start.spoon.net/install](http://start.spoon.net/install). 

If the Spoon Plugin is installed and you continue to see this issue, verify that your browser is not blocking the Spoon Plugin from running on Spoonium. 

**Mozilla Firefox**

1. Navigate to [http://spoonium.net/selenium](http://spoonium.net/selenium).
2. To the left of the browser's address bar, a "building block" icon should appear (it looks like a small LEGO). 
3. Click this icon and a small box will appear beneath it with the dialog "Allow *spoonium.net* to run Spoon?" 
4. Select **Allow and Remember** 
5. Refresh the page and click **Start Grid**. 

**Google Chrome**

1. In the address bar, type **chrome://plugins**. 
2. Locate **Spoon Plugin** and check the **Always allowed** box. 
3. Restart Google Chrome to apply this new setting. 

#### Selenium Errors

**Internet Explorer does not launch with Error "IELaunchURL() returned HRESULT 80070012"**

This error occurs due to a bug in Selenium's IEDriverServer. For more information, see this issue report: [https://code.google.com/p/selenium/issues/detail?id=7045](https://code.google.com/p/selenium/issues/detail?id=7045). 

To avoid this error, enable **ForceCreateProcessApi** in your test capabilities. For language-specific instructions, see **Testing Internet Explorer**.