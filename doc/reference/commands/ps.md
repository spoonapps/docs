### ps

The ps command returns a list of all the containerized processes running on the local machine. 

	# view all processes running in containers
	> spoon ps
	PID   Name     Container  	 User
	---   ----	   --------- 	 ----
	2252  cmd.exe  f1ea9fe59eeb  Administrator

	# view the "long-format" results for additional information
	> spoon ps -l
	PID   Name     Container  	 User	  		UTime	  KTime		Command
	---   ----	   --------- 	 ---- 			----- 	  -----		-------
	2252  cmd.exe  f1ea9fe59eeb  Administrator  00:01:05  00:01:10	"C:\Windows\system32\cmd.exe"

The **UTime** is the amount of CPU time the process spent in user-mode code. 

The **KTime** is the amount of time spent in system calls within the kernel. 