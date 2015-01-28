### copy

The `copy` instruction is used to copy a file or directory from spoon.me script
or .xappl configuration directory.

```
copy <source> <destination>

# There is also an alias:
cp <source> <destination>
```

Source path may point to an inner subdirectory of the one mentioned above,
but must not point above it.

Destination may either be absolute path, or relative. In the second case,
file is copied into a location related to the current working directory.

Examples:
```
copy spoon.me .
copy setup\installer.msi C:\setup\
cp app-1.2.3.4.msi setup\installer.msi
```
