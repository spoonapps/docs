SQL Sandbox allows to run any number of preconfigured database servers and tools on a single machine. All apps running in a SQL Sandbox are connected together in a virtual network. It makes it possible to run multiple identically-configured database server instances without having to worry about conflicting port numbers or instance names.

[http://spoon.net/sql](/sql)

Every container has a unique name assigned, and this name can be used to connect to the container from within the virtual network, e.g., in order to connect SSMS or other tool to a SQL Server instance. You can see the container name in the bottom-right corner of the Sandbox page when the container is running or below its icon at the top. It is also visible in the command prompt of the container, if there is any.

#### Connecting to SQL Server

To connect to a SQL Server instance, SQL Server Authentication must be used. In the server name field in the tool you are intending to connect to your SQL Server instance you can simply specify the SQL Server container's name. It will connect to the server on default TCP port 1433. The images are preconfigured to allow these login credentials:

* **Login**: sa
* **Password**: password1
