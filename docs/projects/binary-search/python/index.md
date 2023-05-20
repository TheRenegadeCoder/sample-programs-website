---
title: Binary Search in Python
layout: default
last-modified: 2020-05-02
featured-imaged: binary-search-in-every-language.jpg
tags: [python, binary_search]
authors:
  - rayavarapuvikram1

---

Welcome to the [Binary Search](https://sampleprograms.io/projects/binary-search) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys


def binary_search(array_list, key):
    start = 0
    end = len(array_list)
    while start < end:
        mid = (start + end) // 2
        if array_list[mid] > key:
            end = mid
        elif array_list[mid] < key:
            start = mid + 1
        else:
            return mid
    return -1


def input_list(list_str):
    array_of_numbers = list_str
    array_of_numbers = array_of_numbers.split(",")
    array_of_numbers = [int(x) for x in array_of_numbers]
    return array_of_numbers


def exit_with_error():
    print('Usage: please provide a list of sorted integers ("1, 4, 5, 11, 12") and the integer to find ("11")')
    sys.exit(1)


if __name__ == "__main__":
    try:
        array_of_numbers = sys.argv[1]
        value_to_be_found = int(sys.argv[2])
        array_of_numbers = input_list(array_of_numbers)

        if array_of_numbers != sorted(
                array_of_numbers) or len(array_of_numbers) < 1:
            exit_with_error()
        index = binary_search(array_of_numbers, value_to_be_found)
        if index < 0:
            print(False)
        else:
            print(True)
    except (IndexError, ValueError):
        exit_with_error()
```

{% endraw %}

[Binary Search](https://sampleprograms.io/projects/binary-search) in [Python](https://sampleprograms.io/languages/python) was written by:

- Jeremy Grifski
- Vikram Rayavarapu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 15 2020 22:17:17. The solution was first committed on Oct 27 2019 02:01:55. As a result, documentation below may be outdated.

## How to Implement the Solution

### The Main Function

Breaking down this solution from bottom to top,

```python
if __name__ == "__main__":
    try:
        array_of_numbers = sys.argv[1]
        value_to_be_found = int(sys.argv[2])
        array_of_numbers = input_list(array_of_numbers)

        if array_of_numbers != sorted(
                array_of_numbers) or len(array_of_numbers) < 1:
            exit_with_error()
        index = binary_search(array_of_numbers, value_to_be_found)
        if index < 0:
            print(False)
        else:
            print(True)
    except (IndexError, ValueError):
        exit_with_error()
```

This bit of code checks to see if this is the main module run. If it is then it starts exectuing the code
function and passes user input to main program. In this case the user inputs are two strings
for example they are like as follows`"1, 4, 5, 11, 12"` `"11"`.

```python
def binary_search(alist, key_value):
    start = 0
    end = len(alist)
    while start < end:
        mid = (start + end)//2
        if alist[mid] > key_value:
            end = mid
        elif alist[mid] < key_value:
            start = mid + 1
        else:
            return mid
    return -1

```

This is the main function of this file. It parses the input, then calls our binary search function
(and returns mid (index of our key_value) or -1 (If key_value is not avaliable)).

### Transform Input Parameters

```python
def input_list(list_str):
    array_of_numbers = list_str
    array_of_numbers = array_of_numbers.split(",")
    array_of_numbers = [int(x) for x in array_of_numbers]
    return array_of_numbers
```

This function takes a string like `"1, 4, 5, 11, 12"`, and turns into a list of numbers.
It does this using a list comprehension, first we need to convert our string into a
list `array_of_numbers.split(',')` which is a list of strings split by comma (,). So our
original input string becomes `["1", " 4", " 5", " 11", " 12"]`.
Then for each element in the list `for x in ...` ,  we convert it to an `int`. For example,
the string `" 4"` is converted into a decimal number in this case `4` (it removes the " "(space) too). This is done
for every item in the list so our original input `"1, 4, 5, 11, 12"` becomes `[1, 4, 5, 11, 12]`.

### Throws Error

```python
def exit_with_error():
    print('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"')
    sys.exit(1)
```

This function prints a message and then exits the script with an error, `sys.exit(1)`.
If any non-zero value is returned after execution of program then the program didn't complete properly.
The above function (`exit_with_error()`) is called everytime whenever the user input isn't correct.

### Binary Search

```python
def binary_search(alist, key_value):
    start = 0
    end = len(alist)
    while start < end:
        mid = (start + end) // 2
        if alist[mid] > key_value:
            end = mid
        elif alist[mid] < key_value:
            start = mid + 1
        else:
            return mid
    return -1
```

This function takes a sorted integer list and a value and returns the index of the item found (or `-1` if not)
using the binary search algorithm.

For example, if `[1, 4, 5, 11, 12]` is the input:

* First we take `start = 0`, `end = len(alist)`

* while `start` is less than `end`, we keep on iterating loop

* first we take middle value of array with the expression (`mid = (start + end) // 2`)

* Then we compare the middle value that we got (`mid`) with `key_value`

* If the middle value (`mid`) is greater than `key_value` then we take `end` as middle value (`mid`) and continue searching.

* If the middle value (`mid`) is less than `key_value` then we take end as middle value + 1 (`mid + 1`) and continue searching.

* If key_value is neither greater nor lesser than that of the middle value, then it means that the value that we are searching is at `mid`. So we return the index of the `key_value` (if value in the given list) or `-1` (if not).


## How to Run the Solution

If we want to run this program, we should probably download a copy of Binary Search in Python.
After that, we should make sure we have the latest Python interpreter.
From there, we can run the following command in the terminal:

`python binary_search.py "1, 4, 5, 11, 12" "11"`

Alternatively, we can copy the solution into an online Python interpreter and hit run then you need to modify `sys.argv[i]` to your inputs.
