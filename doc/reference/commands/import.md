### import

The import command is used to add Spoon images or non-Spoon file types from your local machine to your local registry.

When importing external files into the Spoon registry, the filetype must be specified as an input to the command. 

	svm						Spoon image
	msi						Microsoft Software Installer
	thinapp					Thinapp Configuration

You can optionally specify a name to give the newly-imported image. 

	# import a thinapp config
	spoon import -n=old-thinapp-image thinapp C:\s\package.ini

	# import a spoon image
	spoon import svm C:\s\old-image.svm

**Spoon Virtual Application Studio** users, can use this command to import their existing components. 