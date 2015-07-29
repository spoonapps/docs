## Spoon Shell

Spoon Shell, `spsh`, is a REPL-like interactive interface that understands SpoonScript syntax.

When Spoon Shell starts, it creates a working container and starts an interactive prompt. Optionally, given a path to a SpoonScript file as an argument, it can instead start by executing the SpoonScript and only giving up execution control when the script issues a `yield` instruction. At the end of a Spoon Shell session, the working container is removed unless `keep on` instruction has been issued.

Spoon Shell scripting capabilities are superset of capabilities offered by `spoon build`. The differences:

* The working container is never implicitly committed to an image
* The `copy` instruction can be used to copy from anywhere on the host OS
* There are a number of additional commands available

### Additional Command Reference