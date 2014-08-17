# Spoonium Documentation

This is the official Git repository for Spoonium's public documentation. 

Live version of the docs can be found at http://spoonium.net/docs

## Building the Docs

### What You'll Need

- Python 2.7
- Pip

Python dependencies are listed in the py-reqs.txt file in the root directory of this repo. 

To install these dependencies, run: 
	`pip install -r py-reqs.txt` 

### Building

Execute: `python build.py` from the root directory of the repo. 

This will generate a "build" folder with the same structure as the "docs" folder, but with each .md file converted to and saved as an HTML file. 

The build folder will also contain a new "docs.html" file in the root of the /build directory.

## Writing the Docs

### Style Guide

When contributing to the docs on Spoonium, please take the following style guidelines into consideration. 

1. Only 1 `h1` should be specified in each `.md` file. This `h1` is used to populate the sidenav bar.
2. When mocking the command prompt, start the "input" line with a >. See example, below

Input: `>spoon build -n="my image" /path/to/spoon.me`

Output: `building "my image" from /path/to/spoon.me`

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

### Meta.yaml

The overall structure of the page is dicated by the **meta.yaml** file, located at /doc/meta.yaml.
Each document in the yaml file specifies a topic that will appear in the top navbar of the docs page. A topic **must** have the following four properties: 

1. A `display_name`. This is the actual wording that will appear in the top nav bar
2. An `ordering`. This is the order, left-to-right, that the topic will appear in the nav bar, relative to all other topics. 
3. A `link`. This is the initial section that will be shown when a user clicks on a topic, without selecting a section from the dropdown. 
4. A list of `sections`. This list is used to populate the topic's dropdown. 

Each topic has an attribute for a list of containing `sections`. Each section must have the following attributes: 

1. A `display_name`. This will be the text that appears for that section in the containing topic's dropdown. The `display_name` is also used as the basis for forming that section's `id` on **docs.html**. The `id` for a section is the `display_name` with whitespace removed appended to the text "cmdTabContent".
2. An `ordering`. This is the ordering, relative to the other sections in the containing topic, that this section will appear, top-to-bottom, in the topic dropdown. 
3. A list of `pages`. Should always be an empty list in the **meta.yaml** file. 

### Meta.md

Each subdirectory of the /doc folder must be populated with a `meta.md` file. This file tells the build script which section to add any pages in that folder to (appended to the `pages` list attribute of a `section`). The `meta.md` does **not** apply to subdirectories. A **meta.md** file must have the following structure: 

	---
	section: <display_name of section>
	---

Take, for example, the **/doc/basics/about/meta.md** file. This file tells the build script to place any files in this directory in the *Basics > About Spoonium* section of the docs.  

If a **meta.md** file specifies a `section` that is not listed in the **meta.yaml** file, the script will raise a `NoSuchSectionError`. 

If the folder has doc in it and there is no **meta.md** file, a `NoMetaFileError` will be raised. 

## The docs.html Page

This page is built from a `Jinja2` template - **docs_temp.html** located in the /templates folder. 

This template only controls the creation of the navbar and populates the page's list of all the docs pages. To modify the header or footer of the page, edit **/templates/head.html** or **/templates/footer.html**, respectively. 

You may notice that there's some `EJS` templating sprinkled into the page. 

The Spoonium website runs on `NodeJS` and uses `EJS` templating to abstract out some resources. These resources are not held in this repository. 

## The Migration Tool

If you want to change the display_name of a topic or section, use the migration tool -- migrate.py. This will take care of all the internal dependencies for you. 

The script takes 3 parameters:

1. The type of migration (two valid values: "topic" or "section")
2. The current display_name of the topic/section
3. The name to change the topic/section to

USAGE: `python migrate.py --type topic --current <current name> --to <new name>`

