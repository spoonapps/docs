## ENV

	ENV <name> <value>

The `ENV` instruction creates a new environment variable inside the working container. This environment variable will be persisted to the output image from the `build` command. 

Only one environment variable can be added per `ENV` instruction. To add multiple environment variables to the working container, use multiple `ENV` instructions. 

	ENV foo bar
	ENV var 5