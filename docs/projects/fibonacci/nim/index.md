---

title: Fibonacci in Nim
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Fibonacci in Nim page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Nim
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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).