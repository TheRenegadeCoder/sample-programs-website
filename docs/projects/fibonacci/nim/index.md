---
title: Fibonacci in Nim
layout: default
date: 2019-10-16
featured-image: fibonacci-in-every-language.jpg
last-modified: 2019-10-16

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Nim](https://sampleprograms.io/languages/nim) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```nim
# Fibonacci Sample Program in Nim
# Input the number of iterations as a command-line parameter
import os
import strutils

var n: BiggestUInt
try:
    n = paramStr(1).parseBiggestUInt
except IndexError, ValueError:
    echo "Usage: please input the count of fibonacci numbers to output"
    quit(1)

var previouspreviousInt: BiggestUInt
var previousInt: BiggestUInt = 0
var currentInt: BiggestUInt = 1

if n == 0:
    echo ""
    quit(0)

for i in 1..n:
    echo i, ": ", currentInt
    previouspreviousInt = previousInt
    previousInt = currentInt
    currentInt = previouspreviousInt + previousInt
```

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Nim](https://sampleprograms.io/languages/nim) was written by:

- Michael Olson

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 16 2019 23:58:35. The solution was first committed on Oct 16 2019 20:14:08. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).