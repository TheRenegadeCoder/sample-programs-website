---
authors:
- allenres
date: 2025-10-29
featured-image: factorial-in-every-language.jpg
last-modified: 2025-10-29
layout: default
tags:
- factorial
- nim
title: Factorial in Nim
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/nim/how-to-implement-the-solution.md
- sources/programs/factorial/nim/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Nim](https://sampleprograms.io/languages/nim) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```nim
#[ 
    Factorial in Nim
    This program calculates the factorial of a non-negative integer.
]#

import os
import strutils

const UsageMessage = "Usage: please input a non-negative integer"

proc factorial(n: int): int =
  # Calculates the factorial of n (n!).
  if n == 0:
    return 1
  
  var result = 1
  for i in 1..n:
    result *= i
  
  return result

# The main execution block:
block:
  # Check 1: No input argument provided.
  if paramCount() == 0:
    quit(UsageMessage, 1)

  let inputStr = paramStr(1)

  # Check 2: Invalid Input (Empty String or Not a Number)
  var n: int
  try:
    n = parseInt(inputStr)
  except:
    quit(UsageMessage, 1)

  # Check 3: Invalid Input (Negative Number)
  if n < 0:
    quit(UsageMessage, 1)

  # Print the calculated result.
  echo factorial(n)

```

{% endraw %}

Factorial in [Nim](https://sampleprograms.io/languages/nim) was written by:

- allenres

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).