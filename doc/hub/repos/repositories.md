## Repositories

A repository contains the image and version histories of a project, and it may be private or public.

If a repository is public, it will appear in search results, and any Spoonium user can pull or run it. Only the repository owner (or members of the owning organization) can push to the repository. 

Private repositories are not searchable, and they can only be accessed, pulled, or changed by their named owner(s).

The homepage for a repository is located at **http://spoonium.net/hub/[repo owner]/[repo name]**. The homepage contains 3 sections: 

1. **About** - Provides an overview of the repository. 
2. **Releases** - Lists all tagged versions of the image.
3. **History** - Lists the full version history of the image.

### Interacting with Repositories

Repositories can be forked to your Spoonium account by clicking the **Fork** button on a repository's homepage. This will create a copy of the repository under your user account. 

Repositories can be run straight from the web by clicking the **Run** button on the repository's homepage. This will stream the project from your browser, and it is equivalent to executing `spoon run <project name>` from the command prompt. 

You can also favorite a repository by clicking the **Star** button on the repository's homepage.

To investigate the contents of a repository, click the **Open Console** button. This is the equivalent to executing `spoon run --startup=cmd.exe <project name>` from the command prompt.