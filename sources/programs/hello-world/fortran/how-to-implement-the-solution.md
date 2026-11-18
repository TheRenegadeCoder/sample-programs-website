Let's dig into Hello World in Fortran, line by line.

First, we have the `program` statement, which starts the main program and
gives it a name, `helloworld`. Every Fortran executable has exactly one main
program.

Next is `implicit none`. Without it, Fortran guesses the type of any
undeclared variable from its first letter: names starting with I through N
are integers, and everything else is real. That rule dates back to the
earliest Fortran, and it turns a typo into a brand new variable instead of an
error. `implicit none` switches the rule off, so every variable has to be
declared. This program has no variables, but the line is a good habit, and
most modern Fortran code starts with it.

Then comes the line that does the work:

```fortran
print '(A)', 'Hello, World!'
```

The `print` statement writes to standard output. Its first argument is a
format: `'(A)'` says to write one character value exactly as it is. We could
have written `print *, 'Hello, World!'` instead, where `*` means "list-directed"
output and the compiler picks the layout. Many compilers, gfortran among them,
then start the line with a space, so the explicit format keeps the output to
exactly `Hello, World!`.

Finally, `end program helloworld` closes the main program. Repeating the name
is optional, but it makes the end of a long program easy to match with its
start.
