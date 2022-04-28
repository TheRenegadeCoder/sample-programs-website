# Factorial in Python

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Python
import sys


def factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n - 1)


def exit_with_error(msg=None):
    msg = msg or 'Usage: please input a non-negative integer'
    print(msg)
    sys.exit(1)


def main(args):
    try:
        n = int(args[0])
        if n < 0:
            exit_with_error()
        elif n >= 996:
            msg = f'{n}! is out of the reasonable bounds for calculation'
            exit_with_error(msg)
        print(factorial(n))
    except (IndexError, ValueError):
        exit_with_error()


if __name__ == "__main__":
    main(sys.argv[1:])

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.