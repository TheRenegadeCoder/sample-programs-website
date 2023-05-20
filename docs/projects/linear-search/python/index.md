---
title: Linear Search in Python
layout: default
last-modified: 2020-05-02
featured-imaged: linear-search-in-every-language.jpg
tags: [python, linear-search]
authors:
  - frankhart2017

---

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys


def sysarg_to_list(string: str):
    return [int(x.strip(" "), 10) for x in string.split(',')]


def linear_search(array: list, key: int) -> bool:
    for item in array:
        if item == key:
            return True
    return False


if len(sys.argv) != 3 or not sys.argv[1]:
    print('Usage: please provide a list of integers ("1, 4, 5, 11, 12") and the integer to find ("11")')
else:
    key = int(sys.argv[2])
    array = sysarg_to_list(sys.argv[1])
    print(linear_search(array, key))
```

{% endraw %}

[Linear Search](https://sampleprograms.io/projects/linear-search) in [Python](https://sampleprograms.io/languages/python) was written by:

- frankhart2017
- Jeremy Grifski
- rzuckerm
- Siddhartha Dhar Choudhury

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Jan 29 2023 21:43:56. The solution was first committed on Oct 17 2019 18:06:11. As a result, documentation below may be outdated.

## How to Implement the Solution

Let's break up the code into parts to get a deeper understanding of the entire code.

### Convert String to List of Integers

```python
def sysarg_to_list(string: str):
    return [int(x.strip(" "), 10) for x in string.split(',')]
```

This function takes a string like `"2, 1, 10, 5, 3"`, and turns into a list of numbers.
It does this using a list comprehension, first we need to convert our string into a
list `string.split(',')` which is a list of strings split by comma (`,`). So our
original input string becomes `["2", " 1", " 10", " 5", " 3"]`.
Then for each element in the list `for x in ...` ,  we do something to it.

In this example we convert it into a decimal integer, `int(x.strip(" "), 10)`. Then `x.strip(" ")`,
removes any whitespace so `" 1"` becomes `"1"`. Then `int("1", 10)`
converts the string `"1"` into a decimal number in this case `1`. This is done
for every item in the list so our original input of `"2, 1, 10, 5, 3"` becomes `[2, 1, 10, 5, 3]`.

### Linear Search

```python
def linear_search(array: list, key: int) -> bool:
    for item in array:
        if item == key:
            return True
    return False
```

This function loops through each element in `array` comparing current value (`item`) to the
desired value (`key`). When a match is found, `True` is returned. When all values have been
compared, and no match is found, `False` is returned.

### Get User Input and Process It

```python
if len(sys.argv) != 3 or not sys.argv[1]:
    print('Usage: please provide a list of integers ("1, 4, 5, 11, 12") and the integer to find ("11")')
else:
    key = int(sys.argv[2])
    array = sysarg_to_list(sys.argv[1])
    print(linear_search(array, key))
```

The first command-line argument is a string containing a comma-separated list of integers, and the
second command-line argument is the value to find. If the number of arguments is not correct, or
the first argument is empty, a user statement is displayed. Otherwise, the following is done:

* Convert the value to find (`sys.argv[2]`) to an integer
* Call `sysarg_to_list` to convert the string to a list of integers
* Call `linear_search` to search for the value in the list
* Call `print` to display the result of the search


## How to Run the Solution

If we want to run this program, we should probably download a copy of [Linear Search in Python](https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/p/python/linear_search.py).
After that, we should make sure we have the [latest Python interpreter](https://www.python.org/downloads/).
From there, we can run the following command in the terminal:

```
python linear-search.py "3, 2, 6, 1, 7" "2"
```

Alternatively, we can copy the solution into an [online Python interpreter](https://www.online-python.com/) and hit run.
