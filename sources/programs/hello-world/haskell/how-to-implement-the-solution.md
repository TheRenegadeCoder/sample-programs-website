As usual, let's get right to our implementation of Hello World in Haskell.

First thing we will probably notice is that Haskell syntax is very different
from Lisp and Scheme. Despite all three of those languages being functional,
Haskell seems to have ditched the parentheses. In fact, even function calls
lack parentheses in Haskell. That's a new one for me.

After the syntax, the next thing we should probably look at is that first line.
As usual, we have a module declaration which basically declares this file as
the main file. In other words, execution begins with this module. We saw
something similar in our Hello World in Go article.

Finally, we have our `main` function. For someone who has never played with anything
like Haskell, this syntax is a bit bizarre. In fact, the main function doesn't look
like a function definition at all. At least, it doesn't look like what we've come to
expect from this series.

That said, the `main` function does make a lot of sense if we think about it in terms
of mathematics. After all, math functions follow the exact same form: `f(x) = x`.

At any rate, let's get back to the code. In this final line, we have the `main` keyword
which indicates the entry point to the program. From there, we compute the expression
on the other side of the equals sign. In this case, we have a print function (`putStrLn`) and our
string, and that's it. Pretty simple!
