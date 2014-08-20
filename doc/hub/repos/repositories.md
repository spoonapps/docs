## Repositories

A repository contains the image and version history of a project. 

Repositories may be public or private. If a repository is public, it will appear in search results and be pulled or run by any Spoonium user. Only the repository owner (or members of the "owner" organization) can push to the repository. 

Private repositories can only be viewed by, pulled from, or pushed to, by their owner (or members of the "owner" organization).

The homepage for a repository is located at **http://spoonium.net/hub/[repo owner]/[repo name]**. The homepage contains 3 sections: 

1. About - provides an overview of the repository. 
2. Releases - lists all tagged versions of the image.
3. History - lists the full version history of the image.

#### Interacting with Repositories

Repositories can be "forked" to your Spoonium account by clicking the **Fork** button on a repository's homepage. This will create a copy of the repository under your user account. 

Repositories can be run from the web by clicking the **Run** button on the repository's homepage. This is equivalent to executing `spoon run <project name>` from the command prompt. 

You can also favorite a repository by clicking the **Star** button on the repository's homepage.

To investigate the contents of a repository, click the **Open Console** button. This is the equivalent to executing `spoon run --startup=cmd.exe <project name>` from the command prompt. 

