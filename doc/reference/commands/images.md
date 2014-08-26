### images

The `images` command lists all of the images present in the current user's local registry. 

The results of this command returned in a tabular format with 3 columns: **NAME**, **ID**, and **CREATED**. 

The **NAME** column shows the name and tag of the image. If the image was pulled from a remote registry, it will also show the repository it was pulled from. 

The **ID** column shows the ID of the image. The **ID** is a SHA256 hash of the image contents and is used to uniquely identify the image. 

The **CREATED** column shows the date the image was first created. The date is displayed in the format *MM/DD/YYYY HH:MM:SS AM/PM*. 

#### Formatting Results

The `--csv` flag can be specified to return the output of the `spoon image` command as a tab-separated table. 

By default, the results of `spoon images` are truncated so that they are most readable in the command prompt. This is most noticeable in the **ID** column, where the 32-character ID is truncated to 12 characters. To prevent the Spoon IDE from truncating data, specify the `--no-trunc` flag. 

**Example Usage**: `spoon images --no-trunc`

