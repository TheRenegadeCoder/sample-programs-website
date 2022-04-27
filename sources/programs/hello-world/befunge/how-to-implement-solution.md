There are many valid ways to set up a Befunge program. People tend to design for either artistic or compactness purposes. A typical example for a Hello World looks a little something like this:

```befunge
"!dlroW ,olleH"> , v
               | : <
               @
```

As stated earlier, everything works off of a stack. A stack in programming is a list of values, set up sort of like a stack of papers. Only the top number can be retrieved, and new numbers are always placed on the very top. Because of this, strings have to be read in backwards, as the last letter in will be the first letter out.

The program starts out in string mode to read in the characters. At the end of the first line, our stack will look something like this: (with translated characters below)

```
33 100 108 114 111 87 32 44 111 108 108 101 72
!  d   l   r   o   W     ,  o   l   l   e   H
```

The following section is a literal loop, to print out each of the values off the stack:

```befunge
> , v
| : <
@
```

In order, the arrow sends it right, `,` prints out the H, the arrows loop it back around, `:` copies the top value of the stack, and `|` takes that copy for an if statement.

With `|`, if the top value is 0 (or null), then the pointer starts to go downwards, otherwise it is sent up. `_` works the same way, except it means right on 0 and left for anything else.

The pointer will continue to run through the loop until the stack is empty. When it finishes, the if bar drops it down to the bottom. The `@`  indicates end of program. 
