With the background out of the way, let's get right into our 
implementation of Hello World in Julia.

And unsurprisingly, that's it! We can implement Hello World 
in Julia in a single line.

Despite how easy the print functionality seems in Julia, there's 
actually a lot going on. First of all, `println` makes a call to 
print with an added newline character.

The print function handles any sort of IO, so we could theoretically 
pass our string to any IO stream. In this case, we leave the default 
standard output.

Regardless, print makes a call to a function named show. At that 
point, I'm not sure what happens, but I suspect there's some C-level 
call to `printf`.
