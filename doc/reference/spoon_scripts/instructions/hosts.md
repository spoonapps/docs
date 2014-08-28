### hosts

```
hosts <ip address|local host name> <host name>
```

The hosts instruction modifies host name resolution within a container. The syntax for this command matches that of the **hosts** file in Windows -- the first parameter is a host name or IP address and the second parameter is the name to resolve the host name/IP address to. 

This setting will then be persisted to the constructed image so that any containers created from that image will have these DNS settings applied. 

	# Make the loopback ip resolve to mydomain.net
	hosts 127.0.0.1 mydomain.net

	# Redirect requests google.com to localhost
	hosts google.com localhost