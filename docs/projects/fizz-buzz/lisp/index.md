---
title: Fizz Buzz in Lisp
layout: default
last-modified: 2020-05-02
featured-image: fizz-buzz-in-lisp.jpg
tags: [lisp, fizz-buzz]
authors:
  - stuin

---

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Lisp](https://sampleprograms.io/languages/lisp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lisp
(defun divides-by (num divisor)
    (= (mod num divisor) 0))

(dotimes (num 100)
    (write-line
      (cond
        ((and (divides-by (+ num 1) 3) (divides-by (+ num 1) 5)) "FizzBuzz")
        ((divides-by (+ num 1) 3) "Fizz")
        ((divides-by (+ num 1) 5) "Buzz")
        (t (write-to-string (+ num 1))))))
```

{% endraw %}

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Lisp](https://sampleprograms.io/languages/lisp) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 11 2020 10:18:56. The solution was first committed on Oct 10 2020 18:18:40. As a result, documentation below may be outdated.

## How to Implement the Solution

Lisp has many flavors and variations, so we will be using Clisp, the most common and general form.
The code follows a pre-fix format, where a function or operator is followed by its arguments, even in the case of `+` or `=`.
Every set of parenthesis is its own function.

As a quick note, here are the rules to the problem:

    If a number is divisible by 3, print the word 'Fizz' instead of the number.
    If the number is divisible by 5, print the word 'Buzz' instead of the number.
    Finally, if the number is divisible by both 3 and 5, print 'FizzBuzz' instead
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

Each following line is one possible output, starting with the `"FizzBuzz"` phrase.

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


## How to Run the Solution

There are many options for running the code, though make sure to be using a CLisp based tool.

To run on a local machine, we can download a copy of [Steel Bank Common Lisp][1]
as well as a copy of the solution. Assuming SBCL is in the path,
we can run a lisp file like a script as follows:

```
sbcl --script fizz-buzz.lsp
```

For an easy online interpreter, here are some options:

- [CompileOnline CLISP][2]
- [Jdoodle CLISP][3]

[1]: https://www.sbcl.org/
[2]: https://ideone.com/l/clips
[3]: https://www.jdoodle.com/execute-clisp-online/
