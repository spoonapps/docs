SQL Sandbox allows launching any number of preconfigured database servers and tools on a single machine. All VMs in a SQL Sandbox are connected together in a virtual network. Identically-configured database server instances run without having to worry about conflicting port numbers or instance names.

Every VM has a unique name assigned, and this name can be used to connect to the VM from within the virtual network, e.g., in order to connect SSMS or other tool to a SQL Server instance. You can see the VM name in the bottom-right corner of the Sandbox page when the VM is running or below its icon at the top. It is also visible in the command prompt of the container.

#### Connecting to SQL Server

To connect to a SQL Server instance, SQL Server Authentication must be used. In the Server Name field of the tool you are intending to connect to your SQL Server instance you can simply specify the SQL Server VM's name. It will connect to the server on default TCP port 1433. The images are preconfigured to allow the following login credentials:

* **Login**: sa
* **Password**: password1
