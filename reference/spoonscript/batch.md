### batch

The `batch` instruction is used for embedding batch files in the SpoonScript.

```
batch
	<line 1>
	<line 2>
	<...>
```

Each indented line after the batch line is part of a single batch file. The first non-indented line terminates the batch section and resumes normal command processing.

#### Example

You can use the batch instruction to execute a series of commands that share their state.

```
# Create a new directory with a text file inside of it.
batch
  mkdir c:\new_folder
  cd c:\new_folder
  echo text content > text_file.txt
```