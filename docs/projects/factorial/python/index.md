---
authors:
- Anuj Singh
- Bharath
- Jeremy Grifski
- Parker Johansen
- rzuckerm
date: 2018-12-22
featured-image: factorial-in-every-language.jpg
last-modified: 2023-05-15
layout: default
tags:
- factorial
- python
title: Factorial in Python
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/python/how-to-implement-the-solution.md
- sources/programs/factorial/python/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys


def factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n - 1)


def exit_with_error(msg=None):
    msg = msg or 'Usage: please input a non-negative integer'
    print(msg)
    sys.exit(1)


def main(args):
    try:
        n = int(args[0])
        if n < 0:
            exit_with_error()
        elif n >= 996:
            msg = f'{n}! is out of the reasonable bounds for calculation'
            exit_with_error(msg)
        print(factorial(n))
    except (IndexError, ValueError):
        exit_with_error()


if __name__ == "__main__":
    main(sys.argv[1:])

```

{% endraw %}

Factorial in [Python](https://sampleprograms.io/languages/python) was written by:

- Bharath
- Jeremy Grifski
- Parker Johansen

This article was written by:

- Anuj Singh
- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Let's look at the 
code for [factorial.py](https://github.com/TheRenegadeCoder/sample-programs/blob/master/archive/p/python/factorial.py).


### The Main Function

Let us breakdown the code in smaller parts,

```python
if __name__ == "__main__":
    main(sys.argv[1:])
```
This bit of code checks to see if this is the `main` module run. If true then it calls the `main` function and passes user input to it. In this case the user input would be a number like `0` or `1` or `50` or `n` (`0<=n<996`).

```python
def main(args):
    try:
        n = int(args[0])
        if n < 0:
            exit_with_error()
        elif n >= 996:
            msg = f'{n}! is out of the reasonable bounds for calculation'
            exit_with_error(msg)
        print(factorial(n))
    except (IndexError, ValueError):
        exit_with_error()
```

This is the `main` function of this file. It parses the input into an integer, then calls our `factorial` function (and prints the results). It also deals with any errors which arise when the input `n` is such that it violates the property: (`0<=n<996`), i.e. `n` is greater than equal to `0` and less than `996`.

### Throw Errors

```python
def exit_with_error(msg=None):
    msg = msg or 'Usage: please input a non-negative integer'
    print(msg)
    sys.exit(1)
```

This function prints a message if given (else default) and then exits the script with an error, `sys.exit(1)`. If any non-zero value is returned then the program didn't complete properly. This function is called if the user input is either less than zero or greater than equal to 996.

### Factorial

```python
def factorial(n):
    if n <= 0:
        return 1
    return n * factorial (n - 1)
```

Finally, the real deal. This function takes a positive integer (less than 996) and returns the factorial of that number. This function `factorial` is a recursive function that calls itself repeatedly while decreasing the input parameter by one on each subsequent call, until the base case is reached 
(`n <= 0`).

Once the base case is reached the call-stack unfolds itself propagating the results to the subsequent calling function, which in this case will be the same function itself.

For example, if `3` is the input:

* First we compare, if 3 <= 0
* False
* return 3 * factorial(3-1)
* Call `factorial(2)`

Now, for `2` as the input:  

* First we compare, if 2 <= 0
* False
* return 2 * factorial(2-1) 
> meanwhile the original call would look like: 
> return 3 * 2 * factorial(2-1)
* Call `factorial(1)`

Now, for `1` as the input:
* First we compare, if 1 <= 0
* False
* return 1 * factorial(1-1) 
> meanwhile the original call would look like:
> return 3 * 2 * 1 * factorial(1-1)
* Call `factorial(0)`

Now, for `0` as the input:
* First we compare, if 0 <= 0
* True
* return 1

Since we reached the base case, now we calculate the the values while moving up towards the original function call.

    factorial(0) = 1  (base-case)
    
    factorial(1) = 1 * factorial(1-1) = 1 * factorial(0) = 1 * 1 = 1
    
    factorial(2) = 2 * factorial(2-1) = 2 * factorial(1) = 2 * 1 = 2
    
    factorial(3) = 3 * factorial(3-1) = 3 * factorial(2) = 3 * 2 = 6


## How to Run the Solution

If you want to run this program, you can download a copy of [Factorial in Python](https://github.com/TheRenegadeCoder/sample-programs/blob/master/archive/p/python/factorial.py).

Next, make sure you have the latest Python interpreter (latest stable version of Python 3 will do).

Finally, open a terminal in the directory of the downloaded file and run the following command:  

`python factorial.py 3`

Alternatively, copy the solution into an online [Python interpreter](https://colab.research.google.com) and hit run.
