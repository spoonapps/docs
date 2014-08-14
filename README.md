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

## Writing the Docs

### Style Guide

When contributing to the docs on Spoonium, please take into consideration the following style guidelines. 

1. Only 1 `h1` should be specified in each `.md` file. This `h1` is used to populate the sidenav bar on the Spoonium doc page. 

### Contributing 

