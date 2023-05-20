---
title: Fibonacci in Python
layout: default  
last-modified: 2020-10-13
featured-imaged: fibonacci-in-every-language.jpg
tags: [python, fibonacci]  
authors: [shubhragupta-code]

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys


def fibonacci(n):
    fib = fibs()
    for i in range(1, n + 1):
        print(f'{i}: {next(fib)}')


def fibs():
    first = 1
    second = 1
    yield first
    yield second
    while True:
        new = first + second
        yield new
        first = second
        second = new


def main(args):
    try:
        fibonacci(int(args[0]))
    except (IndexError, ValueError):
        print("Usage: please input the count of fibonacci numbers to output")
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
```

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Python](https://sampleprograms.io/languages/python) was written by:

- Marius
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Apr 07 2019 00:40:32. The solution was first committed on Oct 06 2018 15:20:01. As a result, documentation below may be outdated.

## How to Implement the Solution

Now, we will consider this code block by block on the order of execution.

```python
if __name__ == "__main__":
    main(sys.argv[1:])
```

This code checks if the `main` module is run. If it is, it then passes control to `main` function passing argument string provided by the user.  

```python
def main(args):
    try:
        fibonacci(int(args[0]))
    except (IndexError, ValueError):
        print("Usage: please input the count of fibonacci numbers to output")
        sys.exit(1)
```

This main function was invoked earlier with argument string. Next line invokes `fibonacci()` function. If the function raises [`IndexError`][1] *(Raised when a sequence subscript is out of range)* or [`ValueError`][2] *(Raised for an non-integer value)*, it prints correct usage pattern. And program exits with exit status `1` which specifies abnormal termination.  

```python
def fibonacci(n):
    fib = fibs()
    for i in range(1, n + 1):
        print(f'{i}: {next(fib)}')

def fibs():
    first = 1
    second = 1
    yield first
    yield second
    while True:
        new = first + second
        yield new
        first = second
        second = new
```

In `fibonacci()` function, function `fibs()` is called. In `fibs()`, [`yield`][3] function returns generator which iterates to store and get values. Value of `first` and `second` are initially stored in generator as 1 and 2. In the while loop, values of fibonacci sequence is added using rule `third_num = first_num + second_num`. Control goes back to `fibonacci()` which prints values returned by `next()` which returns next item in iterator. This sequence is repeated till the user specified input times.

[1]: https://docs.python.org/3/library/exceptions.html#IndexError
[2]: https://docs.python.org/3/library/exceptions.html#ValueError
[3]: https://docs.python.org/3/reference/simple_stmts.html#the-yield-statement


## How to Run the Solution

Fibonacci in Python. After that, we should make sure we have the
[latest Python interpreter][4]. From there, we can simply run the following
command in the terminal:

```console
python fibonacci.py
```

Alternatively, we can copy the solution into an [online Python interpreter][5]
and hit run.

[4]: https://docs.python.org/3/tutorial/interpreter.html
[5]: https://www.onlinegdb.com/online_python_interpreter
