Since C predates both Java and Python, the syntax is naturally a bit archaic.
That said, you'll find that the syntax for Hello World in C is still easier to
understand than Java.

At the top, we'll notice an `include` statement. Basically, this statement copies
in functionality from the standard IO library of C. This includes the `printf`
functionality we'll need to actually write our string to the command line.

Like Java, we'll notice that we have a `main` function. In C, the `main` function is
much simpler. In fact, we don't even have classes in C, so we don't have to bother
with that extra layer of abstraction. Instead, we can define the `main` function
directly. Again, we can only define one of these per program.

Inside the `main` function, we'll find our usual call to print. However, in C,
we use `printf` which allows us to format strings as well.

Finally, we'll notice that we return zero. That's because the `main` function is
like any other function, so it has a return type. In this case, the return type
is an integer, and that integer is used to indicate status codes. A status code
of zero means no errors occurred.
