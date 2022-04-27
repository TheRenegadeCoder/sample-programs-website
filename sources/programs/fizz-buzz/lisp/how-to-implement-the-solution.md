Lisp has many flavors and variations, so we will be using Clisp, the most common and general form.
The code follows a pre-fix format, where a function or operator is followed by its arguments, even in the case of `+` or `=`.
Every set of parenthesis is its own function.

```lisp
(dotimes (run 100)
    (setq num (+ run 1))
    (write-line (cond
        ((and (= (mod num 3) 0) (= (mod num 5) 0)) "FizzBuzz")
        ((= (mod num 3) 0) "Fizz")
        ((= (mod num 5) 0) "Buzz")
        (t (write-to-string num))
    ))
)
```

As a quick note, here are the rules to the problem:

    If a number is divisible by 3, print the word ‘Fizz’ instead of the number.
    If the number is divisible by 5, print the word ‘Buzz’ instead of the number.
    Finally, if the number is divisible by both 3 and 5, print ‘FizzBuzz’ instead
    of the number. Otherwise, just print the number.

### The Loop

The first line of code sets up the loop, running the functions inside 100 times, with an index variable named `run`.

```lisp
(dotimes (run 100) ...)
```

The dots show where more lines of code will be placed, such as `setq` which creates a new integer variable.

```lisp
(dotimes (run 100) (setq num (+ run 1)) ...)
```

The new variable is named `num`, and set to the current `run` value + 1.

### The output

The next lines are used to print out the actual ouput, but only one of those is a print statement.
`write-line` will take a string input and print it out as a line to console. Inside it is `cond`, which creates essentially a list of if-else statements, expecting pairs of boolean + executable.

```lisp
(write-line (cond
	...
))
```

Each following line is one possible output, starting with the "FizzBuzz" phrase.

```lisp
((and (= (mod num 3) 0) (= (mod num 5) 0)) "FizzBuzz")
```

To restate this in a more traditional format,

```c
if(num % 3 == 0 && num % 5 == 0) then "FizzBuzz"
```

The next two checks are simaler, just testing for each option.

```lisp
((= (mod num 3) 0) "Fizz")
((= (mod num 5) 0) "Buzz")
```

Finally, the last line in the set has no if statement, and is the default alternative, just writing the `num` variable to a string.

```lisp
(t (write-to-string num))
```

The code will run through each if statement until one of them is true, then use the connected string as an argument for `write-line`, printing it out to the console.
