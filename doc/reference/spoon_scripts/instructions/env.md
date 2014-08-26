### env

```
env <name> <value>
```

The `env` instruction creates a new environment variable inside the working container. This environment variable will be persisted to the output image from the `build` command. 

Only one environment variable can be added per `env` instruction. To add multiple environment variables to the working container, use multiple `env` instructions. 

```
env foo bar
env var 5
```