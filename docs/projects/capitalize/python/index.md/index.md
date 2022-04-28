# Capitalize in Python

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Python
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.