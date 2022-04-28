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
