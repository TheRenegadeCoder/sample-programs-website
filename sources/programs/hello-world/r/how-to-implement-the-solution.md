Fortunately, this task can be solved in a concise one-liner.

You can see the string "Hello, World!" as the argument of the function `cat`.
This function does all the work. If you are familiar with Bash, you may already
know the `cat` tool which prints the content of one or several files.

Analogously, you can pass one or several strings to the `cat` function which prints
the input to the standard output. The function allows an optional argument `sep`
that represents the separator to use when you pass multiple strings. As a
consequence, the following is an equivalent alternative to the solution above:

```r
cat("Hello", "World!", sep=", ")
```

In this call, "Hello" and "World!" are glued together by placing the specified
separator ", " between the two strings, resulting in the desired output
"Hello, World!".

Now, we know what we need to produce the output. The next section explains how
we can also see the output of our program.
