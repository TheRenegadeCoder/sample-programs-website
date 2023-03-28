[Befunge][1] is a programming language with some very unusual standards, 
as a two-dimensional, self-modifying, stack-based programming language. 
Apparently, it was designed in 1993 by Chris Pressey, merely to be as 
difficult to compile as possible.

All operations in Befunge are limited to a single character, and the 
source text can be traversed in any direction through the file. The 
"Instruction Pointer" starts in the upper left corner and proceeds 
to the right, running every character it crosses. When it reaches 
an arrow, `< > ^ v`, that pointer will turn and travel in the new 
indicated direction.

Instead of variables, all operations act on one global stack of 
integers, similar to Forth. 0-9 will just push their value, 
`+ - * / %` pop the top two values and push their normal result, 
`.` prints out the top number, and `,` prints the corresponding 
character instead.

[1]: https://en.wikipedia.org/wiki/Befunge
