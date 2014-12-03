### states

The states command lists all container states on the hub.  

```
Usage: spoon containers [<container-prefix>] <options>

<options> available:
      --csv                  Print output with tab-separated columns
  -l, --latest               List the most recently created container
  -n=VALUE                   List the 'n' most recently created containers
      --no-trunc             Don't truncate output
```

Command line flags for the `states` flag serve to modify or filter the command's results. A `<container-prefix>` can be added to only display states of containers that starts with `<container-prefix>`.

```
# Only show most recently created state
> spoon states -l

Container  Created              State     Visibility
---------  -------              -----     ----------
e4b1ba0f   2014-12-01 18:48:47  2e981e1e  Public

# Show last 'n' created containers
> spoon states -n=3
Container  Created              State     Visibility
---------  -------              -----     ----------
e4b1ba0f   2014-12-01 18:48:47  2e981e1e  Public
cf6ba018   2014-12-01 18:34:55  5f2b7843  Public
dfc32e73   2014-12-01 18:33:35  eafa3740  Public
```

If the value specified for `-n` is greater than the number of states present on the hub, all of the states are listed (same result as running `spoon states`). 

#### Formatting Results

The table that is returned by the states command is space-formatted. If you wish to return the table with tabs between each column then use the `--csv` flag. 

```
> spoon states --csv
```

Data in the table returned by the states command is truncated so that it prints nicely and is easily readable in a command prompt. If you wish to view the untruncated data in each column, use the `--no-trunc` flag. 

```
> spoon states --no-trunc
```
