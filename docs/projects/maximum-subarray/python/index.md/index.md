# Maximum Subarray in Python

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Python
import sys


def maximum_subarray():
    # takes care of both empty input and no input
    str_input = (','.join(i for i in sys.argv[1:])).strip()
    if str_input == "":
        print("Usage: Please provide a list of at least two integers to sort in the format: '1, 2, 3, 4, 5'")
        return

    # split comma separated input string into list of integers
    arr = [int(num) for num in str_input.split(',')]
    ans = 0
    curr_sum = 0
    for i in range(len(arr)):
        if (curr_sum + arr[i] > 0):
            curr_sum += arr[i]
        else:
            curr_sum = 0
        ans = max(ans, curr_sum)
    print(ans)
    return


if __name__ == "__main__":
    maximum_subarray()  # call function to carry out kadane's algorithm

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.