ArkScript is
- small: the core fit under 8000 lines of code ; also small in terms of keywords (only 9)
- a scripting language: very easy to embed it in your projects. Registering your own functions in the language is made easy
- portable: a unique bytecode which can be run everywhere the virtual machine is
- a functional language: every parameter is passed by value, everything is immutable unless specified
- powerful: provides closures and explicit capture
- promoting functionalities before performances: expressiveness often brings more productivity, though performances aren't left behind
- a Lisp inspired language, with fewer parentheses: `[...]` is expanded to `(list ...)` and `{...}` to `(begin ...)`
- extensible: supports C++ module to use it in the language, adding functionalities

Also, it has:
- macros: if/else, values, and functions
- tail call optimization
- a REPL with autocompletion and coloration

Example:

```arkscript
(let fibo (fun (n)
    (if (< n 2)
        n
        (+ (fibo (- n 1)) (fibo (- n 2))))))

(print (fibo 28))  # display 317811
```

On the first line:
- we define a variable named `fibo`, using the `let` keyword
- we define its value as a function with `fun`, taking a single argument, `n`

On the second line, we check if n is less than 2 (all functions and keywords are always after an opened paren `(`).

If the condition is true, on line 3 we return the value of `n`.

Otherwise, on line 4, we return the addition of `(fibo (- n 1))` and `(fibo (- n 2))`.

Then on line 6 we call `print` with the function call `(fibo 28)` as its argument.

