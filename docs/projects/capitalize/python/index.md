---
authors:
- Jeremy Grifski
- Manan Gill
- rzuckerm
- shubhragupta-code
date: 2019-10-09
featured-image: capitalize-in-every-language.jpg
last-modified: 2023-05-15
layout: default
tags:
- capitalize
- python
title: Capitalize in Python
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/python/how-to-implement-the-solution.md
- sources/programs/capitalize/python/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys


def capitalize(input):
    if len(input) > 0:
        print(input[0].capitalize() + input[1:])


if __name__ == '__main__':
    if(len(sys.argv) == 1 or len(sys.argv[1]) == 0):
        print('Usage: please provide a string')
    else:
        capitalize(sys.argv[1])

```

{% endraw %}

Capitalize in [Python](https://sampleprograms.io/languages/python) was written by:

- Jeremy Grifski
- Manan Gill

This article was written by:

- Jeremy Grifski
- rzuckerm
- shubhragupta-code

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

We will consider this code block by block on the order of execution.

```python
if __name__ == '__main__':
    if(len(sys.argv) == 1 or len(sys.argv[1]) == 0):
        print('Usage: please provide a string')
    else:
        capitalize(sys.argv[1])
```
This code checks if the main module is run. If it is, it then checks if the length of argument string provided by the user is 1 or empty string. If it is, it then prints correct usage pattern. Otherwise, it passes control to capitalize function passing argument string provided by the user.

```python
def capitalize(input):
    if len(input) > 0:
        print(input[0].capitalize() + input[1:])
```
If the length provided by the user string is greater than 0, then it prints first letter of the string capitalized and concatenates the rest of the string.


## How to Run the Solution

Capitalize in Python. After that, we should make sure we have the
[latest Python interpreter][1]. From there, we can simply run the following
command in the terminal:

```console
python capitalize.py
```

Alternatively, we can copy the solution into an [online Python interpreter][2]
and hit run.

[1]: https://docs.python.org/3/tutorial/interpreter.html
[2]: https://www.onlinegdb.com/online_python_interpreter
