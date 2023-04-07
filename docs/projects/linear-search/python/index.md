---
title: Linear Search in Python
layout: default
last-modified: 2020-05-02
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

Let us check out the entire code first, then we will break it into parts and get a deeper understanding of the entire code.

### Solution

```python
#!/usr/bin/env python
import sys

def sysarg_to_list(string):
    return [int(x.strip(" "), 10) for x in string.split(',')]

key = int(sys.argv[1])
array = sysarg_to_list(sys.argv[2])
size = len(array)

flag = 0
pos = -1

for i in range(size):
    if array[i] == key:
        flag = 1
        pos = i
        break

if(flag):
    print(key, "found at position", pos, ".")
else:
    print(key, "not in the array.")
```

### Getting user input and processing it

```python
def sysarg_to_list(string):
    return [int(x.strip(" "), 10) for x in string.split(',')]

key = int(sys.argv[1])
array = sysarg_to_list(sys.argv[2])
size = len(array)
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

The first argument passed to the python code should be the key to search followed by the string containing the elements of array in which the key is to be searched.

### Set flags

```python
flag = 0
pos = -1
```

The following are the uses of these variables:
1) flag: The flag variable is used to check whether a key is present in the array or not. 0 value means that the key is not present in the array and 1 means that key is in the array.
2) pos: The pos variable is used to keep track of the position in the array where key is found. It has a default value of -1 which indicates it is not found.

### Linear Search

```python
for i in range(size):
    if array[i] == key:
        flag = 1
        pos = i
        break
```

Finally we have the actual loop which performs the linear search operation.
This iterates from 0 till size (which is the length of the array).
In each iteration it compares the key with the element of array at the current iteration.
If it is found the flag is set to 1 and pos is set to current iteration (i), finally the loop is stopped there using break statement.

### Result

```python
if(flag):
    print(key, "found at position", pos, ".")
else:
    print(key, "not in the array.")
```

We then check the value of the flag variable.
If it has a value of 0, then it means that the key is not present in the array.
On the other hand, if the value of flag is 1, then it means that the key is found in the array and the corresponding position is displayed to the user.


## How to Run the Solution

If we want to run this program, we should probably download a copy of [Linear Search in Python](https://github.com/TheRenegadeCoder/sample-programs/blob/master/archive/p/python/linear-search.py).
After that, we should make sure we have the latest Python interpreter.
From there, we can run the following command in the terminal:

`python linear-search.py 2 "3, 2, 6, 1, 7"`

Alternatively, we can copy the solution into an online Python interpreter and hit run.
