# import

The `import` command is used to add Spoon images or non-Spoon file types from an arbitrary location on your local machine (or network) to your local registry.

The `import` command currently supports the conversion of the following file types: 

1. Microsoft Software Installer (`MSI`)
2. Thinapp Configuration (`package.ini`)

When importing external files into the Spoon registry, the filetype must be specified as a flag to the `import` command. 

	-svm						Spoon image
	-msi						Microsoft Software Installer
	-thinapp					Thinapp Configuration

**Spoon Virtual Application Studio** users, can use this command to `import` existing `.svm` files into their local registry. 


