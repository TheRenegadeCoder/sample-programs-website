---
authors:
- Haseeb Majid
- Jeremy Grifski
- Parker Johansen
- rzuckerm
date: 2018-12-04
featured-image: bubble-sort-in-python.jpg
last-modified: 2023-05-15
layout: default
tags:
- bubble-sort
- python
title: Bubble Sort in Python
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/bubble-sort/python/how-to-implement-the-solution.md
- sources/programs/bubble-sort/python/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys
from functools import reduce


def bubble_sort(xs):
    def pass_list(xs):
        if len(xs) <= 1:
            return xs
        x0 = xs[0]
        x1 = xs[1]
        if x1 < x0:
            del xs[1]
            return [x1] + pass_list(xs)
        return [x0] + pass_list(xs[1:])
    return reduce(lambda acc, _: pass_list(acc), xs, xs[:])


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
        print(bubble_sort(xs))
    except (IndexError, ValueError):
        exit_with_error()


if __name__ == "__main__":
    main(sys.argv[1:])

```

{% endraw %}

Bubble Sort in [Python](https://sampleprograms.io/languages/python) was written by:

- Jeremy Grifski
- Parker Johansen

This article was written by:

- Haseeb Majid
- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

At this point, let's dig into the code a bit. The following sections break
down the Bubble Sort in Python functionality.

### The Main Function

Breaking down this solution bottom up:

```python
if __name__ == "__main__":
    main(sys.argv[1:])
```

This bit of code checks to see if this is the `main` module run. If it is it then calls the `main`
function and passes user input to it. In this case the user input would be a string of numbers
to sort like so: `"2, 1, 10, 5, 3"`.

```python
def main(args):
    try:
        xs = input_list(args[0])
        if len(xs) <= 1:
            exit_with_error()
        print(bubble_sort(xs))
    except (IndexError, ValueError):
        exit_with_error()
```

This is the `main` function of this file. It parses the input, then calls our bubble sort function
(and prints the results). It also deals with any errors raised.

### Transform Input Parameters

```python
def input_list(list_str):
    return [int(x.strip(" "), 10) for x in list_str.split(',')]
```

This function takes a string like `"2, 1, 10, 5, 3"`, and turns into a list of numbers.
It does this using a list comprehension, first we need to convert our string into a
list `list_str.split(',')` which is a list of strings split by comma (,). So our
original input string becomes `["2", " 1", " 10", " 5", " 3"]`.
Then for each element in the list `for x in ...` ,  we do something to it.

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
If any non-zero value is returned then the program didn't complete properly.
This function is called if the user input isn't correct.

### Bubble Sort

```python
def bubble_sort(xs):
    def pass_list(xs):
        if len(xs) <= 1:
            return xs
        x0 = xs[0]
        x1 = xs[1]
        if x1 < x0:
            del xs[1]
            return [x1] + pass_list(xs)
        return [x0] + pass_list(xs[1:])
    return reduce(lambda acc, _ : pass_list(acc), xs, xs[:])
```

Finally we're at the real meat and potatoes of the script. This function takes an unsorted integer
list and returns a sorted list, using the bubble sort algorithm. This function `bubble_sort` has
another function inside of it `pass_list`, also called a closure. The nested function can access
the variables of the parent function but as read-only, they cannot change the variable values.

The `pass_list` function does one pass of the list and makes sure it's sorted, it does by deleting
elements from the list if they're sorted and comparing the next two.

For example, if `[3, 2, 5, 1]` is the input:

* First we compare 2, 3
* 2 < 3
* Delete 2 from the list `del xs[1]`
* Call `pass_list`, `[2] + pass_list(3,5,1)`

So we combine the output of pass_list with 2.

Taking a look at the time `pass_list` is called.

* Compare 3, 5
* 3 < 5
* This time we don't delete 3, we then pass every element of the list except the first one (3) `xs[1:]`
* Call `pass_list`, `[3] + pass_list(5,1)`.

The final bit of the code is what calls `pass_list`, where `acc` parameter is the `xs` list.
The `reduce` function is used to call `pass_list`, multiple times and `xs[:]` is a copy of the
`xs` so when `xs` is changed `xs[:]` is unaffected. The `reduce` function is used to loop
through every element, it (`reduce`) it uses the output of the last iteration as input to
the next one.

For example:

* For input `[10, 3, 2, 5, 7]` output is `[3, 2, 5, 7, 10]`
* Then input is `[3, 2, 5, 7, 10]` output is `[2, 3, 5, 7, 10]`
* Then input is `[2, 3, 5, 7, 10]` output is `[2, 3, 5, 7, 10]`
* ...


## How to Run the Solution

If we want to run this program, we should probably download a copy of [Bubble Sort in Python](https://github.com/TheRenegadeCoder/sample-programs/blob/master/archive/p/python/bubble-sort.py). 
After that, we should make sure we have the latest Python interpreter.
From there, we can run the following command in the terminal:

`python bubble-sort.py "3, 2, 10, 6, 1, 7"`

Alternatively, we can copy the solution into an online Python interpreter and hit run.
