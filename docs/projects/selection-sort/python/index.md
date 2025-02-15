---
authors:
- Haseeb Majid
- Jeremy Grifski
- Parker Johansen
- rzuckerm
date: 2018-12-23
featured-image: selection-sort-in-every-language.jpg
last-modified: 2023-05-15
layout: default
tags:
- python
- selection-sort
title: Selection Sort in Python
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/selection-sort/python/how-to-implement-the-solution.md
- sources/programs/selection-sort/python/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Selection Sort](https://sampleprograms.io/projects/selection-sort) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys


def selection_sort(xs, sorted_xs=None):
    sorted_xs = sorted_xs or []
    if len(xs) <= 0:
        return sorted_xs
    x = min(xs)
    sorted_xs.append(x)
    xs.remove(x)
    return selection_sort(xs, sorted_xs)


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
        print(selection_sort(xs))
    except (IndexError, ValueError):
        exit_with_error()


if __name__ == "__main__":
    main(sys.argv[1:])

```

{% endraw %}

Selection Sort in [Python](https://sampleprograms.io/languages/python) was written by:

- Jeremy Grifski
- Parker Johansen

This article was written by:

- Haseeb Majid
- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Let's dig into the code a bit. The following sections break
down the Selection Sort in Python functionality.

### The Main Function

Breaking down this solution bottom up,

```python
if __name__ == "__main__":
    main(sys.argv[1:])
```

This bit of code checks to see if this is the `main` module run. If it is it then calls the `main`
function and passes user input to it. In this case the user input would be a string of numbers to sort
like so: `"2, 1, 10, 5, 3"`.

```python
def main(args):
    try:
        xs = input_list(args[0])
        if len(xs) <= 1:
            exit_with_error()
        print(selection_sort(xs))
    except (IndexError, ValueError):
        exit_with_error()
```

This is the `main` function of this file. It parses the input, then calls our selection sort
function (and prints the results). It also deals with any errors raised.

### Transform Input Parameters

```python
def input_list(list_str):
    return [int(x.strip(" "), 10) for x in list_str.split(',')]
```

This function takes a string like `"2, 1, 10, 5, 3"`, and turns into a list of numbers.
It does this using a list comprehension, first we need to convert our string into a
list `list_str.split(',')` which is a list of strings split by comma (`,`).
So our original input string becomes `["2", " 1", " 10", " 5", " 3"]`. Then for each
element in the list `for x in ...` ,  we do something to it.

In this example we convert it into a decimal integer, `int(x.strip(" "), 10)`. Then `x.strip(" ")`,
removes any whitespace so `" 1"` becomes `"1"`. Then `int("1", 10)`
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

### Selection Sort

```python
def selection_sort(xs, sorted_xs=None):
    sorted_xs = sorted_xs or []
    if len(xs) <= 0:
        return sorted_xs
    x = min(xs)
    sorted_xs.append(x)
    xs.remove(x)
    return selection_sort(xs, sorted_xs)
```

Now onto the main part of the program, this is the function that actually sorts our list.
The `selection_sort()` takes two parameters `xs` which is the unsorted list and `sorted_xs`
which funnily enough is the current sorted list. When you first call the `selection_sort()`
function you then pass it to your unsorted list as `sorted_xs=None` by default.

If the `sorted_xs` value is set (not `None`) then we make `sorted_xs` equal itself, else
`sorted_xs` equals `[]` (an empty list). You should never make a mutable object a default
argument in Python as you get can get unexpected result. You can get more
information [here](http://effbot.org/zone/default-values.htm). Therefore we set
`sorted_xs=None` instead of `sorted_xs=[]`.

Then we check if xs is empty (`<=0`), which would mean we have sorted every element,
then we return the `sorted_xs` which is the sorted this. We can do this because
as we sort element we move them from `xs` to `sorted_xs` ( items get removed from the `xs` list).

If `xs` still has items then that means we haven't completely sorted the list.
We found the smallest value in `x = min(xs)`. We append that value to `sorted_xs` and then we
remove it from the `xs` list. Finally, we call the selection sort function with the new `xs` and
`sorted_xs` values. This repeats until `xs` is empty and you are left with a completely sorted
`sorted_xs`.

Taking a look at a simple example where we want to sort `[5, 1, 3]`.

1st:

* Call `selection_sort([5, 1, 3])`
* `xs = [5, 1, 3]`, `sorted_xs=[]`
* Minimum value is `1`
* `xs = [5, 3]`, `sorted_xs = [1]`
* `selection_sort([5, 3], [1])`

2nd:

* `xs = [5, 3]`, `sorted_xs = [1]`
* Minimum value is `3`
* `xs = [5]`, `sorted_xs = [1, 3]`
* `selection_sort([5], [1, 3])`

3rd:

* `xs = [5]`, `sorted_xs = [1, 3]`
* Minimum value is `5`
* `xs = []`, `sorted_xs = [1, 3, 5]`
* `selection_sort([], [1, 3, 5])`

4th:

* `xs = []`, `sorted_xs = [1, 3, 5]`
* `len(xs) <= 0`, as we have 0 elements
* So we return `sorted_xs = [1, 3, 5]`


## How to Run the Solution

If we want to run this program, we should probably download a copy of [Selection Sort in Python](https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/p/python/selection_sort.py).
After that, we should make sure we have the [latest Python interpreter](https://www.python.org/downloads/). From there, we can run the following command in the terminal:

`python selection-sort.py "3, 2, 10, 6, 1, 7"`

Alternatively, we can copy the solution into an [online Python interpreter](https://www.online-python.com/) and hit run.
