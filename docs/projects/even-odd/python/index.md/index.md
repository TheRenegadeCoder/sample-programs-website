# Even Odd in Python

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

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.