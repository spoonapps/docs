### images

The `images` command lists all of the images present in the local registry. 

```
Usage: spoon images <options>

<options> available:
      --csv                  Print output with tab-separated columns
      --no-trunc             Don't truncate output
```

The results are truncated so that they are most readable in the command prompt. To prevent Spoon from truncating data, specify the `--no-trunc` flag. 

The `--csv` flag can be specified to return the output as a tab-separated table. 

#### Examples:

```
# List all images in local registry
> spoon images

ID 			  Name  				Tag	 Created 				Size
-- 			  ----  				---  -------    			----
7a85fe8f7ad1  spoonbrew/chocolatey       8/22/2014 11:34:19 AM  3.6 MB
```