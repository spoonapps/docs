### config

The `config` command displays and allows modification of the current configuration settings.

```
Usage: spoon config <options>

<options> available:
      --hub=VALUE            The hub server to log into
```

If `spoon config` is executed without command line parameters then the current settings are returned. 

To modify any settings, specify them as command line flags and assign a value to the flag. This value will then be applied to that setting. 

#### Change the Remote Registry

The remote registry that Spoon will connect to, and thus push to and pull from, can be configured with the `--hub` flag. 

By default, Spoon is configured to connect to **https://spoon.net/hub**. 