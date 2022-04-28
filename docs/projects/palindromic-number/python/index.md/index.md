---

---

Welcome to the Palindromic Number in Python page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Python
#Check if number is palindromic
import sys
import math

# accept an integer, reverse it, compare it with original
# print true, if original and reversed number are same
# print false, if original and reversed number are same
def palindromic_number(x):
    reversed_number = 0

    # Count no. of digits
    noofdigits = 0;
    temp = x
    while (temp > 0):
      noofdigits += 1
      reversed_number = (reversed_number * 10) + (temp % 10);
      temp = int(temp/10)


    # Need minimum 2 Digits in input integer
    if (noofdigits>=2):
      if x == reversed_number:
        print("true")
      else:
        print("false")

    else:
      print("Usage: please input a number with at least two digits")
    
def main(args):
    try:
        # palindromic_number(int(args[1]))
        palindromic_number(int(sys.argv[1]))
    except (IndexError, ValueError):
        print("Usage: please input a number with at least two digits")
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])


```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.