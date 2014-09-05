### search

The `search` command is used to search the remote registry for images.

```
Usage: spoon search <query> [<query>...]
```

Only public repositories are listed in search results. 

Multiple queries can be added to make searches more specific. The `search` command will return the set intersection of multiple queries (**AND** not **OR**). For example, the command below will only return images with Java and Maven. 

```
> spoon search java maven
```