### config

The `config` command displays and allows modification of the current configuration settings.

```
Usage: spoon config <options>

<options> available:
      --hub=VALUE            The hub server to log into
      --reset                Reset configuration to default values
```

If `spoon config` is executed without command line parameters then the current settings are returned. 

To modify any settings, specify them as command line flags and assign a value to the flag. This value will then be applied to that setting. 

#### Change the Hub Server

The hub server that Spoon will connect to, and thus push to and pull from, can be configured with the `--hub` flag. 

By default, Spoon is configured to connect to **https://spoon.net/hub**.

#### Resetting Config Settings

The configuration settings for Spoon can be reset to their default values by issuing the config command with the `--reset` flag.
