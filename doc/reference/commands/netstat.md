### netstat

The `netstat` command displays active port mappings, name resolution information, and links for the specified container.

```
Usage: spoon netstat <container>
```

```
> spoon run --route-add=:80 --route-add=:8081 --hosts=localhost:lhost --link=0218:service -d <image> 63621076457c4b4fb7fff3fcbfda06b1
> spoon netstat 6362

Active port mappings:
49767:80

Name resolution overrides:
localhost lhost

Container links:
021833f5b86c4a80980eff9e5e9f39e2 as service
```

**Note**: only active port mappings are printed. Since the container in the example did not expose any service on tcp port 8081, the mapping corresponding to flag `--route-add=:8081` was not present in the output.
