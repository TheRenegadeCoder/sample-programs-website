---
authors:
- rzuckerm
- Subhayu Roy
date: 2020-10-02
featured-image: fibonacci-in-every-language.jpg
last-modified: 2023-11-13
layout: default
tags:
- boo
- fibonacci
title: Fibonacci in Boo
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/boo/how-to-implement-the-solution.md
- sources/programs/fibonacci/boo/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Boo](https://sampleprograms.io/languages/boo) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```boo
import System

def usage():
    print("Usage: please input the count of fibonacci numbers to output")
    Environment.Exit(0)

def fib(n):
    a, b = 0L, 1L       # The 'L's make the numbers double word length (typically 64 bits)
    for index in range(n):
        yield index + 1, b
        a, b = b, a + b

# Print the first n numbers in the series:
try:
    n = int.Parse(argv[0])
    for index as int, element in fib(n):
        print("${index}: ${element}")
except _ as IndexOutOfRangeException:
    usage()
except _ as FormatException:
    usage()

```

{% endraw %}

Fibonacci in [Boo](https://sampleprograms.io/languages/boo) was written by:

- rzuckerm
- Subhayu Roy

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).