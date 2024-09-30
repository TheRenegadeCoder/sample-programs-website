ArkScript programs do not require a `main` function as in C or C++. Every expression is executed, thus a single `(print "Hello, World!")` can write to the console.

A modular way to write the program could be as follows:

```arkscript
(let say (fun (to)
  (print (str:format "Hello, {}!" to))))

(say "World")
```

1. The first line, `(let say (fun (to)`, declares a function named `say`, taking a single argument, `to`.
2. On the second line, we have a call to `str:format`: it takes a format string and values to be formatted
    1. This is then wrapped in a call to `print` to write the resulting string to the console
3. On the last line, we call the `say` function with the argument `World`, printing `Hello, World!`

