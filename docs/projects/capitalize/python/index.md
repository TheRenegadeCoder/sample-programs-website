---

title: Capitalize in Python
layout: default
date: 2021-10-24
last-modified: 2021-10-24
featured-image:
tags: [capitalize, python]
authors: [shubhragupta-code]

---

Welcome to the Capitalize in Python page! Here, you'll find the source code for this program as well as a description of how the program works.

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

Capitalize in Python was written by:

- Jeremy Grifski
- Manan Gill

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 15 2020 22:17:17. The solution was first committed on Oct 09 2019 21:02:30. As a result, documentation below may be outdated.

## How to Implement the Solution

Let's take a look on code for capitalize.py:

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

Now, we will consider this code block by block on the order of execution.

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
