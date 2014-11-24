## Walkthrough - ASP.NET

Spoon also supports running ASP.NET applications within a container. In this example, we will clone an ASP.NET application, MiniBlog, from GitHub, deploy it in a container and test it with Firefox.

### Topics Covered

1. Creating a container using multiple base images
2. Deploying an ASP.NET website
3. Running IIS Express within a container
4. Test with Firefox in the container

```

# Create a new container with git and ASP.NET and a DNS mapping
C:\> spoon run microsoft/aspnet,mozilla/firefox,git/git

Downloading git from https://spoon.net/users/git
Downloading aspnet from https://spoon.net/users/microsoft
Downloading firefox from https://spoon.net/users/mozilla
Running container b1275642 with visibility public (use '--private' for a private container)

# This will start a container that has git, Firefox and ASP.NET support.
# Note that the startup file is selected based on the git image since that is last in the list.

```

In your container, configure up the ASP.NET application.

```

(c99f354f) C:\> cd c:\
(c99f354f) C:\>git clone https://github.com/madskristensen/MiniBlog.git

# Like the Hello World sample, this directory exists inside your container - not on your local system.

# Start the ASP.NET application console
(c99f354f) C:\> start "MiniBlog" "C:\Program Files (x86)\IIS Express\iisexpress.exe" /path:C:\MiniBlog\Website /port:80

```

![](/components/docs/getting_started/walkthrough_-_asp.net/iis.png)

```

# Begin testing with Firefox
(c99f354f) C:\> "C:\Program Files (x86)\Mozilla\firefox.exe"

```

Go to http://localhost and test the blog application.

![](/components/docs/getting_started/walkthrough_-_asp.net/miniblog.png)

### Next Steps 

Learn more about:

- [Building containers and advanced Spoon commands](/docs/building).
- [Practical examples and use cases](/docs/reference/samples), such as containerizing Java, Node, Python, and .NET projects.


Enjoy!