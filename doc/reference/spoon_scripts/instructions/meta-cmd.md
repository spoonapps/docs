### meta

The **meta** instruction sets the metadata value for the output image. 

```
meta <name>=<value>
```

Standard metadata properties are listed below:

* Title
* Description
* Published
* Website
* Version

Custom metadata can be specified using other name-value pairs. 

```
# Add a title
meta title="application name"

# Add custom metadata
meta internal-name=new-name
```