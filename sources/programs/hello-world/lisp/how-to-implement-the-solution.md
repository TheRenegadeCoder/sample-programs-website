Unfortunately, Lisp has many flavors which means the following implementation 
of Hello World will likely only be applicable to handful of those flavors:

That said, I'm happy to dig into this implementation of Hello World in Lisp.

First things first, we have the `format` keyword. In Common Lisp, `forma`t is 
basically the equivalent to `printf` in C. It basically takes some string and 
outputs it to some destination.

That brings us to this mysterious letter `t`. According to gigamonkeys, `t` is 
actually the destination of the output. More specifically, `t` indicates standard 
output. Another option is `NIL` which causes the string to be returned.

Finally, we have our Hello World string. This is obviously what gets printed 
to standard output.
