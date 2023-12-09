At long last, here's Hello World in C*.

As we can see, Hello World in C* looks similar to C. That said, C*
is a superset of C, so this shouldn't be too much of a surprise. At any rate,
let's dig in.

Unlike C, there is no `include` statement. As far as I can tell, the language
does not actually have an `include` statement or header files. Somehow, the
compiler know where to pull the definition for standard libraries.

Next, we have our usual `main` function declaration which serves as the drop in
function for our program. We should be used to seeing this convention since it's
common in the popular industrial languages like C++ and Java.

Finally, we make a call to `println` which is a special print function that outputs
the specified string with a newline character. Of course, all we're going to pass
to it is the "Hello, World!" string. And, that's it!
