The syntax of Euphoria is similar to C in some respects but without
braces and semicolons, and the `include` statement does not have
quotes or angle brackets around the file that is being included.

```euphoria
include std/io.e
```

The `std/io.e` include file contains the definitions for standard
I/O file numbers. `STDOUT`, as expected, has the value of `1`. While
it is not necessary to include this, it makes the code more readable
since the intent of `STDOUT` is more obvious than just a hard-coded
value of `1`.

```euphoria
puts(STDOUT, "Hello, World!\n")
```

The `puts` function is similar to the `fputs` function
in C, but the parameters are reversed. The first argument is the file
number. The second argument is the string to output. In C, the first
argument is the string to output, and the second argument is a
`FILE` pointer.
