---
authors:
- Jeremy Grifski
- Niraj Kamdar
- rzuckerm
date: 2019-10-16
featured-image: fraction-math-in-every-language.jpg
last-modified: 2023-05-15
layout: default
tags:
- fraction-math
- python
title: Fraction Math in Python
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fraction-math/python/how-to-implement-the-solution.md
- sources/programs/fraction-math/python/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fraction Math](https://sampleprograms.io/projects/fraction-math) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import operator
import sys
from fractions import Fraction

d = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "==": lambda x, y: int(operator.eq(x, y)),
    "<": lambda x, y: int(operator.lt(x, y)),
    ">": lambda x, y: int(operator.gt(x, y)),
    "<=": lambda x, y: int(operator.le(x, y)),
    ">=": lambda x, y: int(operator.ge(x, y)),
    "!=": lambda x, y: int(operator.ne(x, y)),
}


def main(args):
    if len(args) != 3:
        print("Usage: ./fraction-math operand1 operator operand2")
        sys.exit(1)
    else:
        try:
            o1 = Fraction(args[0])
        except ValueError:
            print(f"Invalid operand: {args[0]}")
        try:
            o2 = Fraction(args[2])
        except ValueError:
            print(f"Invalid operand: {args[2]}")
        try:
            print(d[args[1]](o1, o2))
        except KeyError:
            print(f"Invalid operator: {args[1]}")


if __name__ == "__main__":
    main(sys.argv[1:])

```

{% endraw %}

Fraction Math in [Python](https://sampleprograms.io/languages/python) was written by:

- Jeremy Grifski
- Niraj Kamdar

This article was written by:

- Jeremy Grifski
- Niraj Kamdar
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Let's first take a look at the solution.

### Imports

In our sample, we import three standard library utilities:

```python
import operator
import sys
from fractions import Fraction
```

Here, we have imported `sys` for taking arguments from console. `operator` are to perform artithmatic and relational operation. `Fraction` class provide various methods for working with fractions.

### Mapping operator

```python
d = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "==": lambda x, y: int(operator.eq(x, y)),
    "<": lambda x, y: int(operator.lt(x, y)),
    ">": lambda x, y: int(operator.gt(x, y)),
    "<=": lambda x, y: int(operator.le(x, y)),
    ">=": lambda x, y: int(operator.ge(x, y)),
    "!=": lambda x, y: int(operator.ne(x, y)),
}
```

Here, we are mapping operator entered in the string to actual operator method so that `Fraction class` can perform that.

### Check number of arguments

Our `main` function takes arguments as parameter.

```python
def main(args):
    if len(args) != 3:
        print("Usage: ./fraction-math operand1 operator operand2")
        sys.exit(1)
```

Here, we check if number of arguments entered are three, if it's not then print `Usage: python fraction.py operand1 operator operand2` on console and exit.

### Perform operation

```python
    else:
        try:
            o1 = Fraction(args[0])
        except ValueError:
            print(f"Invalid operand: {args[0]}")
        try:
            o2 = Fraction(args[2])
        except ValueError:
            print(f"Invalid operand: {args[2]}")
        try:
            print(d[args[1]](o1, o2))
        except KeyError:
            print(f"Invalid operator: {args[1]}")
```

Now, we check if we can convert entered `args` into `Fraction` type if we can't then we print `Invalid operand: (entered operand)` on console. After that we check if operator is valid and if it's not then we print `Invalid operator: (entered operator)` on console. If everything is good then it prints desired output on console

### Taking arguments from console

```python
if __name__ == "__main__":
    main(sys.argv[1:])
```

Here, `sys.argv` contains arguments passed from the console. We know that first argument is name of file itself.
so, all we need is arguments that are passed after that. We then give it to the `main` function.


## How to Run the Solution

To run the fractions operation in python program, grab a copy of the `fractions.py` file
from GitHub. After that, get the latest version of python interpreter. Now, all you have to
do is run the following from the command line:

```console
python fraction.py "1/4" "+" "5/8"
```

Alternatively, you can always copy the source code into an online python interpreter. Just make sure you pass some input to your program before you run it.
