Personally, I'm getting hints of Java and
Python here just in terms of syntax.

At any rate, let's break it down. Obviously, we only have
one line, but it's at least a little more interesting than
most scripting languages.

For starters, we have the built-in `System` class. This class
comes with the core module along with a few other goodies like
`String`, `Sequence`, `Fiber`, and `Bool`.

Now, one of the functions of `System` is `print`. Obviously, `print`
writes text to standard output. But, I find Wren's `print`
functionality particularly interesting because it's similar to
Java. In fact, it accepts any object as input. If the input is
not a `String`, `print` will convert it to a `String` using the
`toString` functionality, a method available to all objects.

So, basically we call the static method print of the `System` class
which prints the input to the user. How cool is that?
