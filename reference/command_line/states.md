### states

The `states` command lists all of the container states on the Spoon.net Hub.  

```
Usage: spoon states [<container-prefix>] <options>

<options> available:
      --csv                  Print output with tab-separated columns
  -l, --latest               List the most recently created container state
  -n=VALUE                   List the 'n' most recently created container states
      --no-trunc             Don't truncate output
```

Command line flags can be used to filter or limit the results. 

```
# Use a container prefix to show states for containers that match
> spoon states cf6ba

Container  Created              State     Visibility
---------  -------              -----     ----------
cf6ba018   2014-12-01 18:34:55  5f2b7843  Public

# Show the last state created
> spoon states -l

Container  Created              State     Visibility
---------  -------              -----     ----------
e4b1ba0f   2014-12-01 18:48:47  2e981e1e  Public

# Show last 'n' container states that were created
> spoon states -n=3
Container  Created              State     Visibility
---------  -------              -----     ----------
e4b1ba0f   2014-12-01 18:48:47  2e981e1e  Public
cf6ba018   2014-12-01 18:34:55  5f2b7843  Public
dfc32e73   2014-12-01 18:33:35  eafa3740  Public
```

If the value specified for `-n` is greater than the number of container states present on the hub, all of the states will be listed. 

#### Formatting Results

The table returned by the `states` command is space-formatted by default. Use the `--csv` flag to return a tab delimited table. 

```
> spoon states --csv
```

Data in the table returned by the `states` command is truncated so that it prints nicely and is easily readable in a command prompt. Use the `--no-trunc` flag to view all of the data. 

```
> spoon states --no-trunc
```
