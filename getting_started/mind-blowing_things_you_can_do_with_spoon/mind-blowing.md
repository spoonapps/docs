## Mind-Blowing Things You Can Do with Spoon

### Test multiple browsers and server configurations on a single box.

Run multiple browser versions side-by-side without conflicts on a single device. Dynamically add browser plugins and runtimes such as Java, .NET, and Flash.
 
<div class="console">
   <p># Run a server application on Java 7 and 8</p>
   <p class="cmd">&gt; spoon run jre:7.51,server</p>
   <p class="cmd">&gt; spoon run jre:8.0,server</p>
   <br>
   <p># Run multiple versions of Firefox simultaneously</p>
   <p class="cmd">&gt; spoon run firefox:33</p>
   <p class="cmd">&gt; spoon run firefox:32</p>
   <br>
   <p># Launch another browser instance in a Java 6 environment</p>
   <p class="cmd">&gt; spoon run jre:6.45,firefox</p>
</div>

### Containerize and share existing desktop development environments.

Create pre-configured developer images including compilers, build tools, development frameworks, and other build dependencies. Share ready-to-use build environments with project collaborators.

<div class="console">
   <p># Run your favorite build tools and development environments</p>
   <p class="cmd">&gt; spoon run golang/go,atom</p>
   <br>
   <p># Use existing package managers like NuGet and Chocolatey</p>
   <p class="cmd">&gt; spoon run nuget</p>
   <p class="cmd">(9ac7bf21)&gt; nuget install MvcScaffolding</p>
   <br>
   <p># Push ready-to-use development images out to collaborators</p>
   <p class="cmd">&gt; spoon push dev-image</p>
</div>

### Connect multiple containers with virtual networking.

Develop and test client/server applications on a single developer box. Containerize multi-server applications and execute in virtualized production network environments. No more "localhost".

<div class="console">
   <p># Launch a WordPress server, block external network connectivity</p>
   <p class="cmd">&gt; spoon run -d --name=web --route-block=tcp,udp wordpress</p>
   <br>
   <p># Connect a Firefox browser instance to the WordPress server and</p>
   <p># map the domain awesome.com to the server container's port 8080</p>
   <p class="cmd">&gt; spoon run --link=web:awesome.com firefox http://awesome.com:8080</p>
</div>

### Inherit multiple base images in a single container.

Easily synthesize complex container environments by combining pre-configured base images for popular build, source control, and test tools.

<div class="console">
   <p># Create a container with git, SBT, and Java</p>
   <p class="cmd">&gt; spoon run git,sbt,jdk</p>
   <p class="cmd">(27661f14)&gt; git clone https://github.com/scala/async.git</p>
   <p class="cmd">(27661f14)&gt; cd async &amp;&amp; sbt clean test</p>
   <p class="cmd">(27661f14)&gt; exit</p>
   <br>
   <p># Commit the async project image and save it</p>
   <p class="cmd">&gt; spoon commit 27661f14 async</p>
   <p class="cmd">&gt; spoon push async</p>
</div>

### Automate container creation with SpoonScript.

Powerful SpoonScript primitives allow automated configuration of containers and integration into continuous integration processes. Higher-order operators such as using allow transient consumption of containers within scripted build environments.

<div class="console">
   <p># Use git and sbt to download and build the project sources</p>
   <p class="cmd">using git,sbt</p>
   <p class="cmd">&nbsp;&nbsp;git clone https://github.com/scala/async.git</p>
   <p class="cmd">&nbsp;&nbsp;cd async &amp;&amp; sbt clean test</p>
   <br>
   <p># git and sbt are no longer present in the image</p>
   <p class="cmd">commit 27661f14 async</p>
   <p class="cmd">push async</p>
</div>

### Install MSI packages within a container.

Utilize legacy MSI installation packages within containerized environments by simply running traditional install processes within containers.
 
<div class="console">
   <p># Launch a container (requires admin privileges -- coming soon!) </p>
   <p class="cmd">&gt; spoon run clean --admin</p>
   <br>
   <p># Run the MSI installer process</p>
   <p class="cmd">(42fa1211)&gt; msiexec setup.msi</p>
</div>