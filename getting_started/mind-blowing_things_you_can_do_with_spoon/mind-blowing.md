## Mind-Blowing Things You Can Do with Spoon

Spoon containerization has some use cases that we think are pretty mind-blowing. Here's a few of them.

### Test multiple browsers and server configurations on a single box.

Run multiple browser versions side-by-side without conflicts on a single device. Dynamically add browser plugins and runtimes such as Java, .NET, and Flash.
 
<div style="width: 605px; height: 230px; margin: 0 8px; min-height: 190px; background-color: #292929; color: #949799; padding: 15px; border-top: 15px solid #696969; border-radius: 4px; margin-bottom: 28px;">
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Run a server application on Java 7 and 8</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run jre:7.51,server</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run jre:8.0,server</p>
   <br>
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Run multiple versions of Firefox simultaneously</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run firefox:33</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run firefox:32</p>
   <br>
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Launch another browser instance in a Java 6 environment</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run jre:6.45,firefox</p>
</div>

### Containerize and share existing desktop development environments.

Create pre-configured developer images including compilers, build tools, development frameworks, and other build dependencies. Share ready-to-use build environments with project collaborators.

<div style="width: 605px; height: 230px; margin: 0 8px; min-height: 190px; background-color: #292929; color: #949799; padding: 15px; border-top: 15px solid #696969; border-radius: 4px; margin-bottom: 28px;">
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Run your favorite build tools and development environments</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run golang/go,atom</p>
   <br>
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Use existing package managers like NuGet and Chocolatey</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run nuget</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">(9ac7bf21)&gt; nuget install MvcScaffolding</p>
   <br>
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Push ready-to-use development images out to collaborators</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon push dev-image</p>
</div>

### Connect multiple containers with virtual networking.

Develop and test client/server applications on a single developer box. Containerize multi-server applications and execute in virtualized production network environments. No more "localhost".

<div style="width: 605px; height: 230px; margin: 0 8px; min-height: 190px; background-color: #292929; color: #949799; padding: 15px; border-top: 15px solid #696969; border-radius: 4px; margin-bottom: 28px;">
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Launch a WordPress server, block external network connectivity</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run -d --name=web --route-block=tcp,udp wordpress</p>
   <br>
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Connect a Firefox browser instance to the WordPress server and</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># map the domain awesome.com to the server container's port 8080</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run --link=web:awesome.com firefox http://awesome.com:8080</p>
</div>

### Inherit multiple base images in a single container.

Easily synthesize complex container environments by combining pre-configured base images for popular build, source control, and test tools.

<div style="width: 605px; height: 230px; margin: 0 8px; min-height: 190px; background-color: #292929; color: #949799; padding: 15px; border-top: 15px solid #696969; border-radius: 4px; margin-bottom: 28px;">
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Create a container with git, SBT, and Java</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run git,sbt,jdk</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">(27661f14)&gt; git clone https://github.com/scala/async.git</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">(27661f14)&gt; cd async &amp;&amp; sbt clean test</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">(27661f14)&gt; exit</p>
   <br>
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Commit the async project image and save it</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon commit 27661f14 async</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon push async</p>
</div>

### Automate container creation with SpoonScript.

Powerful SpoonScript primitives allow automated configuration of containers and integration into continuous integration processes. Higher-order operators such as using allow transient consumption of containers within scripted build environments.

<div style="width: 605px; height: 230px; margin: 0 8px; min-height: 190px; background-color: #292929; color: #949799; padding: 15px; border-top: 15px solid #696969; border-radius: 4px; margin-bottom: 28px;">
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Use git and sbt to download and build the project sources</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">using git,sbt</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&nbsp;&nbsp;git clone https://github.com/scala/async.git</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&nbsp;&nbsp;cd async &amp;&amp; sbt clean test</p>
   <br>
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># git and sbt are no longer present in the image</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">commit 27661f14 async</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">push async</p>
</div>

### Install MSI packages within a container.

Utilize legacy MSI installation packages within containerized environments by simply running traditional install processes within containers.
 
<div style="width: 605px; height: 230px; margin: 0 8px; min-height: 190px; background-color: #292929; color: #949799; padding: 15px; border-top: 15px solid #696969; border-radius: 4px; margin-bottom: 28px;">
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Launch a container (requires admin privileges -- coming soon!) </p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run clean --admin</p>
   <br>
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Run the MSI installer process</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">(42fa1211)&gt; msiexec setup.msi</p>
</div>