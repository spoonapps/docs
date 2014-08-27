### config

The config command displays and allows modification of the current configuration settings.

If `spoon config` is executed without command line parameters, the current settings are returned. 

To modify any settings, specify them as command line flags and assign a value to the flag. This value will then be applied to that setting. 

#### Change the Remote Registry

The remote registry that Spoon will log in to, and thus push to and pull from, can be configured with the **--hub** flag. 

By default, the Spoon IDE will log in to **https://spoonium.net/hub**. 