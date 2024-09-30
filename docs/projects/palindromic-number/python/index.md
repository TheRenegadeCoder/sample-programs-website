---
authors:
- Jeremy Grifski
- manasmithamn
date: 2021-10-27
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2022-10-11
layout: default
tags:
- palindromic-number
- python
title: Palindromic Number in Python
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/python/how-to-implement-the-solution.md
- sources/programs/palindromic-number/python/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys


def palindromic_number(x):
    if x >= 0:
        reversed_number = 0

        noofdigits = 0
        temp = x
        while (temp > 0):
            noofdigits += 1
            reversed_number = (reversed_number * 10) + (temp % 10)
            temp = int(temp/10)

        if x == reversed_number:
            print("true")
        else:
            print("false")
    else:
        print("Usage: please input a non-negative integer")


def main():
    try:
        palindromic_number(int(sys.argv[1]))
    except (IndexError, ValueError):
        print("Usage: please input a non-negative integer")
        sys.exit(1)


if __name__ == "__main__":
    main()

```

{% endraw %}

Palindromic Number in [Python](https://sampleprograms.io/languages/python) was written by:

- Jeremy Grifski
- manasmithamn

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).