## Spoon Tour

Spoon containerization dramatically simplifies the way developers and IT managers build, test, and deploy software. Here are a few of the amazing things you can do with Spoon:

### Always Have a Clean Machine

Need a clean machine to install or test something? Create one in seconds with a single command.

<div style="width: 605px; height: 370px; margin: 0 8px; min-height: 190px; background-color: #292929; color: #949799; padding: 15px; border-radius: 4px; margin-bottom: 28px;">
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Launch a clean virtual machine</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run clean</p>
   <br>
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Command prompt for a clean virtual machine with id 4aa232b1</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">(4aa232b1)&gt; dir C:\</p>
   <br>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"> Volume in drive C has no label.</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"> Volume Serial Number is 7C90-F8ED</p>
   <br>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"> Directory of C:\</p>
   <br>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">06/10/2009  01:42 PM                24 autoexec.bat</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">06/10/2009  01:42 PM                10 config.sys</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">04/11/2011  06:24 PM    &lt;DIR&gt;          Program Files</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">11/14/2014  09:34 AM    &lt;DIR&gt;          Users</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">11/25/2013  03:40 PM    &lt;DIR&gt;          Windows</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">...</p>
   <br>
</div>

### Instant Environment Configuration

Easily create container environments by combining pre-configured base images for popular development tools and frameworks.

<div style="width: 605px; height: 230px; margin: 0 8px; min-height: 190px; background-color: #292929; color: #949799; padding: 15px; border-radius: 4px; margin-bottom: 28px;">
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Create a container with git, SBT, and Java</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run git,sbt,jdk</p>
   <br>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">(27661f14)&gt; git clone https://github.com/scala/async.git</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">(27661f14)&gt; cd async &amp;&amp; sbt clean test</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">(27661f14)&gt; exit</p>
</div>

### Install Existing MSI Packages

Install software from MSI installation packages or other traditional setups by simply running the regular setup processes within a container. There is no
longer any need for sequencing, snapshots, or other special packaging processes.
 
<div style="width: 605px; height: 230px; margin: 0 8px; min-height: 190px; background-color: #292929; color: #949799; padding: 15px; border-radius: 4px; margin-bottom: 28px;">
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Launch a clean virtual machine (MSI requires --admin)</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run --admin clean</p>
   <br>
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Run the MSI installer process</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">(42fa1211)&gt; setup.msi</p>
</div>

### Run Multiple Browser Versions Simultaneously

Run multiple browser versions side-by-side on a single device. Dynamically add browser plugins and runtimes such as Java, .NET, and Flash.

<div style="width: 605px; height: 230px; margin: 0 8px; min-height: 190px; background-color: #292929; color: #949799; padding: 15px; border-radius: 4px; margin-bottom: 28px;">
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Run a server application on Java 7 and 8</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run jre:8,server</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run jre:7,server</p>
   <br>
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Run multiple versions of Firefox simultaneously</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run firefox:33</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run firefox:32</p>
   <br>
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Launch another browser instance in a Java 6 environment</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run jre:6,firefox</p>
</div>

### Container Skinning

Skinning makes it easy to visually distinguish between container contexts.

<div style="width: 605px; height: 230px; margin: 0 8px; min-height: 190px; background-color: #292929; color: #949799; padding: 15px; border-radius: 4px; margin-bottom: 28px;">
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Identify different Java versions by window skin</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run jre:8,firefox+skin(green)</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run jre:7,firefox+skin(red)</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run jre:6,firefox+skin(0x0000ff)</p>   
   <br>
</div>

### Share Development Environments

Create pre-configured developer images including compilers, build tools, development frameworks, and other build dependencies. Share ready-to-use build environments with project collaborators.

<div style="width: 605px; height: 230px; margin: 0 8px; min-height: 190px; background-color: #292929; color: #949799; padding: 15px; border-radius: 4px; margin-bottom: 28px;">
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

### Network Virtualization

Develop and test client/server applications on a single developer box. Containerize multi-server applications and execute in virtualized production network environments. Test with actual domain names and IP configurations.
No more "localhost:8080".

<div style="width: 605px; height: 230px; margin: 0 8px; min-height: 190px; background-color: #292929; color: #949799; padding: 15px; border-radius: 4px; margin-bottom: 28px;">
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Launch a WordPress server, block external network connectivity</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run -d --name=web --route-block=tcp,udp wordpress</p>
   <br>
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Connect a Firefox browser instance to the WordPress server and</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># map the domain awesome.com to the server container's port 8080</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&gt; spoon run --link=web:awesome.com firefox http://awesome.com:8080</p>
</div>


### SpoonScript Automation

Powerful SpoonScript primitives allow automated configuration of containers and integration into continuous integration processes. Higher-order operators such as using allow transient consumption of containers within scripted build environments.

<div style="width: 605px; height: 230px; margin: 0 8px; min-height: 190px; background-color: #292929; color: #949799; padding: 15px; border-radius: 4px; margin-bottom: 28px;">
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># Use git and sbt to download and build the project sources</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">using git,sbt</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&nbsp;&nbsp;git clone https://github.com/scala/async.git</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">&nbsp;&nbsp;cd async &amp;&amp; sbt clean test</p>
   <br>
   <p style="font-size: 13px; margin-bottom: 0; color: #00FF00; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;"># git and sbt are no longer present in the image</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">commit async</p>
   <p style="font-size: 13px; margin-bottom: 0; color: #A2DFFC; font-family: Consolas, 'Liberation Mono', Menlo, Courier, monospace;">push async</p>
</div>

