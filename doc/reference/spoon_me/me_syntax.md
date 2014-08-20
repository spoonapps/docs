## Syntax

1. `.me` scripts are line-delimited and must only contain 1 instruction per line. Line continuation is supported. 
2. All lines must follow the general structure: `INSTRUCTION <**args>`
3. Inline comments are not supported. Comments must be applied at the beginning of a line and are applied to the entire line. 

#### Comments

Comments are denoted by the `#` character. 

	#this is a comment

Comments cannot be made inline with a command. Comments must be specified at the beginning of a line. 

	#this is a valid comment

	FROM spoonbrew/node  #this is not a valid comment