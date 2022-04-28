---

title: Even Odd in Python  
layout: default  
last-modified: 2020-05-02
featured-image: even-odd-in-every-language-featured-image.JPEG 
tags: [python, even-odd]  
authors: [ MandyMericle ]

---

Welcome to the Even Odd in Python page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Python
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

## How to Implement the Solution

Let's look at the code in detail:  

code for even-odd.py:-  

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
    except (IndexError,ValueError):
        exit_with_error()


if __name__ == "__main__":
    main(sys.argv[1:])

```

Here we have a function called even_odd that returns "Even" if a number is even and "Odd" if it is odd. We are checking this using the modulus operator (%) which returns the remainder after division. The result after a modulo operation of an even integer will always be 0 while the result after a modulo operation of an odd integer will always be 1.

Ex.
14 % 2 => 0 (14 / 2 is 7 with no remainder)
15 % 2 => 1 (15 / 2 is 7 with a remainder of 1)


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
