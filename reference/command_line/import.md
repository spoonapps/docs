### import

The `import` command is used to add Spoon images or non-Spoon file types from your local machine to your local registry.

```
Usage: spoon import <options> <type> <path>

<options> available:
  -n, --name=VALUE           Name of the image
      --overwrite            Overwrite existing image
      --wait-after-error     Leave program open after error
```

The filetype must be specified when importing external files into the Spoon registry. 

```
svm           Spoon image
msi           Microsoft Software Installer
thinapp       Thinapp Configuration
```

You can optionally specify a name for the newly-imported image. Use the `--overwrite` flag to overwrite an existing image.

```
# Import a thinapp config
spoon import -n=old-thinapp-image thinapp C:\s\package.ini

# Import a spoon image
spoon import svm C:\s\old-image.svm
```

**Spoon Studio** users can use this command to import their existing components. 