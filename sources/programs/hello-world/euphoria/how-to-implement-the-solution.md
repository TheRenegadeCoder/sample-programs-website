The syntax of Euphoria is similar to C in some respects but without
braces and semicolons, and the `include` statement does not need
quotes or angle brackets around the file that is being included.

```euphoria
include std/io.e

puts(STDOUT, "Hello, World!\n")
```

The `std/io.e` include file contains the definitions for standard
I/O file numbers. `STDOUT`, as expected, has the value of `1`. While
it is not necessary to include this, it makes the code more readable
since the intent of `STDOUT` is more obvious than just a hard-coded
value of `1`. The `puts` function is similar to the `fputs` function
in C. The first argument is the file number, whereas in C, this is
a `FILE` pointer. The second argument is the string to output.
