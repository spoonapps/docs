# Filesystem Compression

**Note**: Filesystem compression is only available in the Spoon IDE. 

To reduce executable size, Spoon IDE can compress virtual filesystem contents. This reduces virtual application size by approximately 50%, but also prevents profiling and streaming of the application. By default, the **Compress Payload** option in the **Process Configuration** area of the **Settings** panel is unchecked. Leave this box unchecked during the build process if the application will be optimized for streaming from Spoon Server.

**Note**: Disabling payload compression may significantly increase the size of the virtual application binary.