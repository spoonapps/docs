# Spoonium Documentation

This is the official Git repository for Spoonium's public documentation. 

Live version of the docs can be found at http://spoonium.net/docs

## Writing the Docs

### Style Guide

When contributing to the docs on Spoonium, please take the following style guidelines into consideration. 

**Code and Command-line Styling**

- Command-line comment: All comments should have a # followed by a space and the first word should be capitalized.

```
# this is formatted properly :)

#this is not :( 
```

- Command-line input

```
> spoon build -n="my image" /path/to/spoon.me
```

- Command-line output


- Command-line spacing



```
building "my image" from /path/to/spoon.me
```

- Always use `spoon` not `spn` in the command line documentation.
- All code blocks should be 'fenced' with 3 backticks (a la [GFM](http://github.com/github-flavored-markdown)). Inline code styles (i.e. this is a sample command: `spoon run`) only use 1 backtick. The syntax highlighting to use can be specified after the top 3 backticks (not available for inline code). 
- Use inline code styles sparingly. 

**Other Styling**

- Inline paths should be **bolded**. --> Example: navigate to **C:\Users** 
- Internal links to other sections of the doc should be relative paths
	* Other doc links: /docs/[topic]#[section]
	* To the hub: /hub
	* To contact page: /contact

### Adding images

- Put the image in the same folder as the md file
- Modify the path in the link based on the example below
- If you need to specify image dimensions, use HTML

```
# GitHub location
https://github.com/spoonium/docs/tree/master/doc/getting_started/tour_ii/image.png

# Markdown would be
![](/components/docs/getting_started/tour_ii/image.png)
```

### Contributing 

#### How to Contribute

If you are not a member of the **spoonium** org (AKA you don't work at Spoon), fork this repo, make changes, commit, and submit a pull request. 

#### Editing an Existing Page

Edit the existing markdown file, save it, and rebuild to make sure you didn't accidentally break anything. Do *not* edit any of the **meta** files. 

#### Adding a Page

If adding a page to an *existing section*, find the (a) corresponding folder in the /doc folder and add your new **.md** file to it. Check the **meta.md** file in that directory and make sure it matches the section you want to add the page to. 

If adding a page and creating a new section, create a new folder under the appropriate topic. Add your new **.md** file and create a new **meta.md** file that will specify the name of the section to add. Then, add the new section you are creating to the **meta.yaml** file, rearranging the ordering of the other sections as you see fit. 

#### Creating a New Topic

To add a new topic to the top navbar, first create a new folder in the /doc directory corresponding to your topic. Then, edit the **meta.yaml** file, adding your new topic and rearranging the topic `ordering` as you see fit. Follow existing patterns when editing this file. 

Populate your new directory in the /doc folder with subdirectories and new markdown files. Make sure that any subdirectory containing documentation has a **meta.md** file. 

## Structure

This section outlines the structure of the Spoonium doc repo and how it is assembled.

### docs.yaml

The overall structure of the page is dicated by the **docs.yaml** file, located at /docs/docs.yaml.
Each document in the yaml file specifies a topic that will appear in the top navbar of the docs page. A topic has the following properties:

1. A `topic`. This is the actual wording that will appear in the top nav bar
2. A list of `documents`. This list is used to populate the topic's documents.