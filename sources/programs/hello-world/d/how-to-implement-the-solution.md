At any rate, let's get to the implementation of Hello World in D.

At this point, you may be questioning whether or not D is even a new 
language. After all, this Hello World implementation looks a lot like 
C/C++.

Well, then it should come as no surprise the solution is pretty much 
the same. We have basically three main parts: the `import` statement, 
the `main` function, and the print function.

Just like C/C++, the first thing we do is import our standard IO 
library. In this case, D references `std.stdio` as opposed to `stdio.h`
in C.

Up next, we have our usual `main` function. At this point in the series, 
we're pretty use to this syntax.

Finally, we have our typical print function. In this case, we call 
`writeln` and pass a string to it.
