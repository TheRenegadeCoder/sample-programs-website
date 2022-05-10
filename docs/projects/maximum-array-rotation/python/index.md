---

title: Maximum Array Rotation in Python
layout: default
date: 2022-04-28
last-modified: 2022-05-10

---

Welcome to the Maximum Array Rotation in Python page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).