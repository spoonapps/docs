### register

The `register` command creates desktop shortcuts and file associations for an image on your local device.

```
Usage: spoon register <options> <image>

<options> available:
      --wait-after-error     Leave program open after error
```

Desktop registration integrates the image into the Windows shell creating desktop and **Start Menu** shortcuts and file associations for the specified image. 

Use the `spoon images --no-trunc` command to see the list of registered images.

There are three options for removing the image from the system:

1. Use the `unregister` spoon command.
1. Use the uninstall shortcut on the **Start Menu**.
1. Uninstall from the **Program and Features** menu in the **Windows Control Panel**.
