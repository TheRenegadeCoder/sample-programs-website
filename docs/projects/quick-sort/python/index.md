---
authors:
- Haseeb Majid
- Jeremy Grifski
- Parker Johansen
- rzuckerm
date: 2018-12-23
featured-image: quick-sort-in-every-language.jpg
last-modified: 2023-05-15
layout: default
tags:
- python
- quick-sort
title: Quick Sort in Python
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quick-sort/python/how-to-implement-the-solution.md
- sources/programs/quick-sort/python/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys


def quick_sort(xs):
    if len(xs) <= 0:
        return []

    left = quick_sort([l for l in xs[1:] if l <= xs[0]])
    right = quick_sort([r for r in xs[1:] if r > xs[0]])
    return left + xs[:1] + right


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
        print(quick_sort(xs))
    except (IndexError, ValueError):
        exit_with_error()


if __name__ == "__main__":
    main(sys.argv[1:])

```

{% endraw %}

Quick Sort in [Python](https://sampleprograms.io/languages/python) was written by:

- Jeremy Grifski
- Parker Johansen

This article was written by:

- Haseeb Majid
- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Let's dig into the code a bit. The following sections break
down the Quick Sort in Python functionality.

### The Main Function

Breaking down this solution bottom up,

```python
if __name__ == "__main__":
    main(sys.argv[1:])
```

This bit of code checks to see if this is the `main` module run. If it is, it then calls the `main`
function and passes user input to it. In this case the user input would be a string of numbers
like so `"2, 1, 10, 5, 3"` (to sort).

```python
def main(args):
    try:
        xs = input_list(args[0])
        if len(xs) <= 1:
            exit_with_error()
        print(quick_sort(xs))
    except (IndexError, ValueError):
        exit_with_error()
```

This is the `main` function of this file. It parses the input, then calls our quick sort
function (and prints the results). It also deals with any errors raised.

Finally we wrap this entire block in a `try ... except`, and we catch two exceptions: `IndexError`
and `ValueError`. `IndexError` will be thrown if `args` is empty, and we try to access `args[0]`.
`ValueError` will be thrown if we try to convert a non-integer string into an integer.
For example if `args[0]` was "a" -> `int("a")`. If any exceptions are raised, then we call
the `exit_with_error()` function.

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

In this example we convert it into a decimal integer, `int(x.strip(" "), 10)`
`x.strip(" ")`, removes any whitespace so `" 1"` becomes `"1"`, then `int("1", 10)`
converts the string `"1"` into a decimal number in this case `1`. This is done
for every item in the list, so our original input of `"2, 1, 10, 5, 3"`
becomes `[2, 1, 10, 5, 3]`.

### Throw Errors

```python
def exit_with_error():
    print('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"')
    sys.exit(1)
```

This function prints a message and then exits the script with an error, `sys.exit(1)`.
If any non-zero value is returned, then the program didn't complete properly. This function is called
if the user input isn't correct.

### Quick Sort

```python
def quick_sort(xs):
    if len(xs) <= 0:
        return []

    left = quick_sort([l for l in xs[1:] if l <= xs[0]])
    right = quick_sort([r for r in xs[1:] if r > xs[0]])
    return left + xs[:1] + right
```

Now onto the main part of the program. This is the function that actually sorts our list.
The first part `len(xs) <= 0` checks if the list is empty. If it is, then it returns an
empty list `return []`.

In each iteration of the quicksort we have to pick a pivot element. This element is used to break
down the current list into two smaller lists. One list contains all numbers larger than the pivot
and the other list contains all elements smaller (or equal) to the pivot. There are a few ways to
pick a pivot element but in our code we will be using the first element of each list (`xs[0]`).

We create two sub-lists from our list. `left` will contain all elements smaller than `xs[0]`,
the first element in our list. `right` will contain all elements larger than `xs[0]`.
These lists aren't actually sorted yet so we call the `quick_sort()` function on these sub-lists
recursively until they are sorted. Each of these sub-lists is broken down into two lists every
time the `quick_sort()` function is called.

```python
left = quick_sort([l for l in xs[1:] if l <= xs[0]])
```

Taking a closer look at how we generate the left sub-list, we use a list comprehension
which is a way to generate lists in Python. In this example `[l for l in xs[1:] if l <= xs[0]]`
we loop through the unsorted list `xs`. Examining the first part `[l for l in xs[1:]]` this would
generate a list which would contain every element in `xs` except the first one. `xs[1:]` means that
the list includes every element except the first one, hence the `[1:]`. This is called index
splicing in Python, and you can learn more about it [here](https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/).

For example, if `xs = [3, 2, 4, 1]`, then the generated list would be `left = [2, 4, 1]`.
Now including the final part of the list comprehension `[l for l in xs[1:] if l <= xs[0]]`,
`l` is only added to the list if it's less or equal to the first element of `xs`, `if l <= xs[0]`.
So again using our example `xs = [3, 2, 4, 1]` the generated list would be`left = [2, 1]`,
since `4 > 3` and `xs[0] = 3`. This new list is then passed to our quick sort function.

The `right = quick_sort([r for r in xs[1:] if r > xs[0]])` is very similar except it stores elements
strictly greater than `xs[0]`. But other than that it generates the list in much the same way `left`
does. So using the same example `xs = [3, 2, 4, 1]` then `right = [4]`. Since `4` is the only element
great then `xs[0] = 3`.

Finally, those two lists are combined into a single list and returned
`return left + xs[:1] + right`, where left contains all elements less than or equal to
`xs[0]` and right contains all the items great than `xs[0]`. `xs[:1]` in this example gets
the first element, except this also works if `xs` is empty. If `xs = []` and you try to get
`xs[0]` the program will throw an `IndexError` whereas `xs[:1] = []` an empty list.

Let's take a look at an example where `xs = [5, 1, 10]`

#### Main Quick Sort

* `xs[0] = 5`
* `left = quick_sort([1])`
* `right = quick_sort([10])`

##### Left Quick Sort

* `xs[0] = 1`
* `left = quick_sort([])`
* `right = quick_sort([])`

Since the lists are empty `quick_sort` will return `[]` an empty list back so.

* `left = []`
* `right = []`
* `return [] + [1] + []`

#### Right Quick Sort

* `xs[0] = 10`
* `left = quick_sort([])`
* `right = quick_sort([])`

Since the lists are empty `quick_sort` will return `[]` an empty list back so.

* `left = []`
* `right = []`
* `return [] + [10] + []`

#### Back to Main Quick Sort

* `left = [1]`
* `right = [10]`
* `xs[0] = 5`
* `return [1] + [5] + [10]`

So the final sorted list is [1, 5, 10]


## How to Run the Solution

If we want to run this program, we should probably download a copy of [Quick Sort in Python](https://github.com/TheRenegadeCoder/sample-programs/blob/main/archive/p/python/quick_sort.py).
After that, we should make sure we have the [latest Python interpreter](https://www.python.org/downloads/). From there, we can run the following command in the terminal:

`python quick-sort.py "3, 2, 10, 6, 1, 7"`

Alternatively, we can copy the solution into an [online Python interpreter](https://www.online-python.com/) and hit run.
