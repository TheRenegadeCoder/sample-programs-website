---
authors:
- Jeremy Grifski
- Tanisha Banik
date: 2021-10-05
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2022-05-10
layout: default
tags:
- maximum-array-rotation
- python
title: Maximum Array Rotation in Python
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-array-rotation/python/how-to-implement-the-solution.md
- sources/programs/maximum-array-rotation/python/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

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

Maximum Array Rotation in [Python](https://sampleprograms.io/languages/python) was written by:

- Jeremy Grifski
- Tanisha Banik

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).