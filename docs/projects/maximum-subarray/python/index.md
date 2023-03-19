---

title: Maximum Subarray in Python
layout: default
last-modified: 2020-10-14
featured-image:
tags: [python, maximum-subarray]
authors:
  - Senpai1199

---

Welcome to the [Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys
from typing import List


def error_handling(argv: List) -> List[int]:
    str_input = (','.join(i for i in argv[1:])).strip()
    if str_input == "":
        print('Usage: Please provide a list of integers in the format: "1, 2, 3, 4, 5"')
        sys.exit(1)
    nums = [int(num) for num in str_input.split(',')]
    return nums


def maximum_subarray(nums: List[int]) -> int:
    local_max = 0
    global_max = nums[0]
    for num in nums:
        local_max += num
        if (local_max < 0):
            local_max = 0
        elif global_max < local_max:
            global_max = local_max
    return global_max


if __name__ == "__main__":
    nums = error_handling(sys.argv)
    print(maximum_subarray(nums))
```

{% endraw %}

[Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [Python](https://sampleprograms.io/languages/python) was written by:

- Divyansh Agarwal
- Jeremy Grifski
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Feb 06 2023 19:40:54. The solution was first committed on Nov 03 2020 08:56:37. As a result, documentation below may be outdated.

## How to Implement the Solution

Let's look at the code in detail:

code for [maximum_subarray.py](https://github.com/TheRenegadeCoder/sample-programs/blob/master/archive/p/python/maximum_subarray.py):-

```python
#!/usr/bin/env python
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

### The main Function

Let us breakdown the code in smaller parts,

```python
if __name__ == "__main__":
    maximum_subarray()
```

This bit of code checks to see if this is the main module run. If true, then it calls the `maximum_subarray()` function which carries out the kadane's algorithm which includes taking array input from standard input(via sys args through the terminal) and computing max subarray sum value and printing the result to standard output.

```python
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
```

This is the main function of this file which implements all the algorithm logic. It takes a comma separated string of integers from the standard input (via the sys args). It then converts the string into an array of integers and carries out Kadane's algorithm for that array and prints the result. It also deals with the edge case which arises when there is no input or the input string is empty(blank string).

If the string is not empty, the function initialises `ans` (final value to be returned from the function) and `curr_sum` as 0. It then iterates through the array, keeps adding values to `curr_sum` until `curr_sum > 0`. If `curr_sum` goes to less than 0, then `curr_sum` is set to 0 again and process is carried on for the remaining elements of the array.
Finally, `ans` is set to the maximum of `0` and `curr_sum`, and it's value is printed.

1. For example, if `` is the input:

- First we compare, if str_input == ""
- True
- print "Usage: Please provide a list of at least two integers to sort in the format: '1, 2, 3, 4, 5'"
- return

2. For example, if `-1, -2, 1, 2, 3` is the input:

- First we compare, if str_input == ""
- False
- Convert str_input into array of integers
- Initialise `curr_sum` and `ans` to 0.
- Now while iterating through the array, index `i` goes from 0 to 4.
- For i = 0 and 1, the initial value of `curr_sum` is 0. 0 + (-1) < 0 and 0 + (-2) < 0, so -1 and -2 are skipped.
- For i = 2,3,4 the values 1,2,3 are added to curr_sum iteratively and finally curr_sum value is `1 + 2 + 3 = 6`
- Max of 0 and 6 is 6. So `ans` gets the value 6.
- Print 6 and return from function.


## How to Run the Solution

If you want to run this program, you can download a copy of [Maximum Subarray in Python](https://github.com/TheRenegadeCoder/sample-programs/blob/master/archive/p/python/maximum_subarray.py).

Next, make sure you have the latest Python interpreter (latest stable version of Python 3 will do).

Finally, open a terminal in the directory of the downloaded file and run the following command:

`python maximum_subarray.py 1,2,3,4`

Replace `1,2,3,4` with input of your choice(comma separated integers)

Alternatively, copy the solution into an online [Python interpreter](https://colab.research.google.com) and hit run.
