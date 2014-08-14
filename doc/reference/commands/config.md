# config

The `config` command serves 2 purposes: 

1. Viewing the current configuration settings
2. Modifying the configuration settings

If `spoon config` is executed without command line parameters, it will return the current Spoon IDE settings for viewing. 

To modify any settings, specify them as command line flags and assign a value to the flag. This value will then be applied to that setting. 

## Command Line Flags

###### Remote Registry

The remote registry that Spoon will log in to, and thus push to and pull from, can be configured with the `--hub` flag. 

By default, the Spoon IDE will log in to `http://spoonium.net/hub`. 