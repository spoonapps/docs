### history

The `history` command lists all images used in the past. 

```
Usage: spoon history <options> <image>

<options> available:
      --csv                  Print output with tab-separated columns
  -n=VALUE                   List the 'n' most recently used images
      --no-trunc             Don't truncate output
```

The most used recent images are listed first.

```
# List the recently used images
> spoon history

ID            Last used             Name            Tag
--            ---------             ----            ---
73dfe6973074  8/29/2014 4:51:08 PM  spoonbrew/node  head
07b66f57ed8d  8/29/2014 4:50:33 PM  spoonbrew/git   head
```
    
To show the history of a certain image, use `spoon history image-name`. 

By default 50 entries are shown. Specify `-n` flag to show more entries. 

The results of `spoon history` are truncated so that they are most readable in the command prompt. To prevent Spoon from truncating data, specify the `--no-trunc` flag. 

The `--csv` flag can be specified to return the output as a tab-separated table. 