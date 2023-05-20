---
title: Maximum Array Rotation in Python
layout: default
date: 2021-10-05
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2021-10-05

---

Welcome to the [Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys

def findMax(arr):
    maxSum = 0
    for i in range(len(arr)):
        val = arr.pop(0)
        arr.append(val)
        sum_ = [ele*j for j,ele in enumerate(arr)]
        sum_ = sum(sum_)
        if sum_ > maxSum:
            maxSum = sum_
    return maxSum

try:
    arr = [int(ele) for ele in sys.argv[1].split(",")]
    print(str(findMax(arr)))

except:
    print('Usage: please provide a list of integers (e.g. "8, 3, 1, 2")')
```

{% endraw %}

[Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [Python](https://sampleprograms.io/languages/python) was written by:

- Jeremy Grifski
- Tanisha Banik

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 10 2022 00:44:08. The solution was first committed on Oct 05 2021 21:06:14. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).