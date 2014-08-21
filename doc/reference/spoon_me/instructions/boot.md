## BOOT FILE

	BOOT FILE <command> <params...>
	BOOT FILE [<exec>, <params...>]

The `BOOT FILE` instruction is used to specify the startup file or script to run when the created image is `run`. 

This instruction is only applied to the output image -- it does not affect the intermediate container. 

The `BOOT FILE` instruction will accept parameters as a space-delimited list or as a JSON-array of strings. 

If parameters are specified as a space-delimited list, the first parameter is the startup command and all subsequent parameters are parameters that will be passed to the startup command when the image is `run`. When specified in this manner, commands are interpreted by the Windows shell. 

	# hello world is passed to the 'echo' command
	BOOT FILE echo hello world

If parameters are specified as a JSON-array of strings, the first item in the array is the startup executable and all subsequent items are passed as parameters to the startup executable when the image is `run`.  When specified in this manner, parameters are passed directly to the startup executable. 

	#"clone" and "https://github.com/spoonium/docs" are passed to git.exe
	BOOT FILE ["git.exe", "clone", "https://github.com/spoonium/docs"]