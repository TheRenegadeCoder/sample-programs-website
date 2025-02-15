---
authors:
- Haseeb Majid
- Jeremy Grifski
- Parker Johansen
- rzuckerm
date: 2018-12-22
featured-image: insertion-sort-in-every-language.jpg
last-modified: 2023-05-15
layout: default
tags:
- insertion-sort
- python
title: Insertion Sort in Python
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/insertion-sort/python/how-to-implement-the-solution.md
- sources/programs/insertion-sort/python/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys
from itertools import takewhile


def insertion_sort(xs):
    new_xs = []
    for x in xs:
        new_xs = insert(x, new_xs)
    return new_xs


def insert(x, xs):
    left = list(takewhile(lambda i: i < x, xs))
    right = xs[len(left):]
    return left + [x] + right


def input_list(list_str):
    return [int(x.strip(" "), 10) for x in list_str.split(',')]


def exit_with_error():
    print('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"')
    sys.exit(1)


def main(args):
    try:
        xs = input_list(args[0])
        if len(xs) <= 1:
            exit_with_error()
        print(insertion_sort(xs))
    except (IndexError, ValueError):
        exit_with_error()


if __name__ == "__main__":
    main(sys.argv[1:])

```

{% endraw %}

Insertion Sort in [Python](https://sampleprograms.io/languages/python) was written by:

- Haseeb Majid
- Jeremy Grifski
- Parker Johansen

This article was written by:

- Haseeb Majid
- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Let's dig into the code a bit. The following sections break
down the Insertion Sort in Python functionality.

### The Main Function

Breaking down this solution bottom up:

```python
if __name__ == "__main__":
    main(sys.argv[1:])
```

This bit of code checks to see if this is the `main` module run. If it is, it then calls the `main`
function and passes user input to it. In this case the user input would be a string of numbers to sort
like so: `"2, 1, 10, 5, 3"`.

```python
def main(args):
    try:
        xs = input_list(args[0])
        if len(xs) <= 1:
            exit_with_error()
        print(insertion_sort(xs))
    except (IndexError, ValueError):
        exit_with_error()
```

This is the `main` function of this file. It parses the input, then calls our insertion sort
function (and prints the results). It also deals with any errors raised.

### Transform Input Parameters

```python
def input_list(list_str):
    return [int(x.strip(" "), 10) for x in list_str.split(',')]
```

This function takes a string like `"2, 1, 10, 5, 3"`, and turns into a list of numbers.
It does this using a list comprehension. First, we need to convert our string into a
list `list_str.split(',')` which is a list of strings split by comma (`,`).
So our original input string becomes `["2", " 1", " 10", " 5", " 3"]`. Then for each
element in the list `for x in ...` ,  we do something to it.

In this example we convert it into a decimal integer, `int(x.strip(" "), 10)`. Then, `x.strip(" ")`
removes any whitespace so `" 1"` becomes `"1"`. After that, `int("1", 10)`
converts the string `"1"` into a decimal number in this case `1`. This is done
for every item in the list so our original input of `"2, 1, 10, 5, 3"` becomes `[2, 1, 10, 5, 3]`.

### Throw Errors

```python
def exit_with_error():
    print('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"')
    sys.exit(1)
```

This function prints a message and then exits the script with an error, `sys.exit(1)`.
If any non-zero value is returned then the program didn't complete properly. This function is called
if the user input isn't correct.

### Insertion Sort

```python
def insertion_sort(xs):
    new_xs = []
    for x in xs:
        new_xs = insert(x, new_xs)
    return new_xs
```

Let's take a look at the part of the program that sorts our list. The unsorted list is passed to the
`insertion_sort` method as the parameter `xs`. Meanwhile, `new_xs = []` is our new sorted listed which is
empty to begin with.

We loop through every element in the unsorted list `for x in xs`. Then we call the `insert()`
function to add `x` to the `new_xs` (the sorted list) in the correct position.
Each time the `insert()` function is called it returns a sorted list which we assign
to `new_xs`. Finally, when we've looped through every item in `xs`, we return the sorted list
`new_xs` which will then get printed on the terminal to the user.

Taking a look at an example where `xs = [5, 3, 10]`

1st

* `x = 5`
* `insert(5, [])`
* `new_xs = [5]`

2nd

* `x = 3`
* `insert(3, [5])`
* `new_xs = [3, 5]`

3rd

* `x = 10`
* `insert(10, [3, 5])`
* `new_xs = [3, 5, 10]`

### Insert

```python
def insert(x, xs):
    left = list(takewhile(lambda i: i < x, xs))
    right = xs[len(left):]
    return left + [x] + right
```

This function takes two parameters `x`, which is an element from our unsorted list, and
`xs`, which is the list to add `x` to such that `xs` remains sorted.
A High-level overview of this function is that the `left` variable will be a list that stores
all elements less than `x` from `xs` and `right` will store all elements greater than (or equal)
to `x`. That way we can "insert" `x` between these two lists. Hence the return statement
looking like `return left + [x] + right` and this returned list will therefore be sorted.

Let's take a look at the first line `left = list(takewhile(lambda i: i < x, xs))` it looks a bit
complicated so let's break it down. The first part `lambda i: i < x, xs` is a lambda function
which is a small anonymous unnamed function.
In this case `i` is an element of `xs` and we want all `i`'s less than `x`.

Then, we call `takewhile(lambda i: i < x, xs)` which takes a predicate (our lambda function) and a list.
It stops iterating over our list as soon as the lambda function evaluates to False. It then returns
all the elements up to that index.

Lets take a look at an example where `xs = [4, 7, 10]` and `x = 8`.
The first two items of `xs` would evaluate as True since 4 and 7 are
less than 8, so takewhile would store 4 and 7 but not 10.
The `takewhile()` function returns a `takewhile` object but we want a list so we convert that into a
list hence `list(takewhile(lambda i: i < x, xs))`. So the `left` variable will store all numbers
less than `x`, since `xs` is already sorted.

Moving onto `right = xs[len(left):]`, `len(left)` returns the length of the left list.
Then we do some index splicing; you can learn more about that
[here](https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/).
Index splicing is used to get part of a list in Python. In this case we are getting every element in
the list that's not already in `left`. We can do this because we know `xs` is already sorted.

If `xs = [1, 4, 6, 8]` and `x = 7` then `left = [1, 4, 6]` (all elements < 7). Then `len(left) = 3`
and `right = xs[3:]`. Where `[3:]` gets all elements from `xs` not including the first `3` elements,
so therefore `right = [8]`. Finally, we `return left + [x] + right` as we can simply "slot" `x` into the
correct position. We convert `x` to a list `[x]` first so we can do list concatenation using the
plus operator `+`.

Lets take a look at an example, `xs = [3, 4, 6, 8, 11, 15, 18]` and `x` is `5`. The variable `left`
will add consecutive elements from `xs` until `lambda i: i < x` (i < x) evaluates as False.
In this case `left = [3, 4]` as 6 > 5. Then we get the length of `left` which is `len(left) = 2`,
slice so we don't include the first two elements `xs[2:] = [6, 8, 11, 15, 18]`. Then we return
the following `left + [x] + right = [3, 4] + [5] + [6, 8, 11, 15, 18]` or
`[3, 4, 5, 6, 8, 11, 15, 18]`.


## How to Run the Solution

If we want to run this program, we should probably download a copy of [Insertion Sort in Python](https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/p/python/insertion_sort.py).
After that, we should make sure we have the latest Python interpreter. From there, we can run the following command in the terminal:

`python insertion-sort.py "3, 2, 10, 6, 1, 7"`

Alternatively, we can copy the solution into an [online Python interpreter](https://www.online-python.com/) and hit run.
