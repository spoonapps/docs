### register

The `register` command creates desktop shortcuts and file associations for an image on your local device.

```
Usage: spoon register <options> <image>

<options> available:
      --wait-after-error     Leave program open after error
```

Desktop registration integrates the image into the Windows shell creating desktop and Start Menu shortcuts and file associations for the specified image. These changes can be removed by unregistering the image with the `spoon unregister` command, from the uninstall shortcut which is created in the Start Menu, or from the **Program and Features** menu in the Windows Control Panel.

List of registered images can be checked using `spoon images --no-trunc` command.