---
authors:
- Jeremy Grifski
- Parker Johansen
- rzuckerm
date: 2018-12-22
featured-image: even-odd-in-every-language.jpg
last-modified: 2023-05-15
layout: default
tags:
- even-odd
- python
title: Even Odd in Python
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/python/how-to-implement-the-solution.md
- sources/programs/even-odd/python/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys


def even_odd(x):
    return "Even" if x % 2 == 0 else "Odd"


def exit_with_error():
    print('Usage: please input a number')
    sys.exit(1)


def main(args):
    try:
        num = int(args[0])
        print(even_odd(num))
    except (IndexError, ValueError):
        exit_with_error()


if __name__ == "__main__":
    main(sys.argv[1:])

```

{% endraw %}

Even Odd in [Python](https://sampleprograms.io/languages/python) was written by:

- Jeremy Grifski
- Parker Johansen

This article was written by:

- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Let's look at the code in detail:  

Here we have a function called `even_odd` that returns "Even" if a number is even and "Odd" if it is odd. We are checking this using the modulus operator (%) which returns the remainder after division. The result after a modulo operation of an even integer will always be 0 while the result after a modulo operation of an odd integer will always be 1.

Ex.
* 14 % 2 => 0 (14 / 2 is 7 with no remainder)
* 15 % 2 => 1 (15 / 2 is 7 with a remainder of 1)


## How to Run the Solution

If we want to run this program, we should probably download a copy of
Hello World in Python. After that, we should make sure we have the
[latest Python interpreter][1]. From there, we can simply run the following
command in the terminal:

```console
python even-odd.py <input>
```

With <input> being any integer. For example

```console
python even-odd.py 12
```

Alternatively, we can copy the solution into an [online Python interpreter][2]
and hit run.

[1]: https://docs.python.org/3/tutorial/interpreter.html
[2]: https://www.onlinegdb.com/online_python_interpreter
