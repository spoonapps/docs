### batch

The `batch` instruction is used for embedding batch files in the SpoonScript.

```
batch
	<line 1>
	<line 2>
	<...>
```

Each indented line after the batch line is part of a single batch file. The first non-indented line terminates the batch section and resumes normal command processing.
