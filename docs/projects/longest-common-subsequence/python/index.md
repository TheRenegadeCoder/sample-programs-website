---
authors:
- Boot-Error
- Parker Johansen
date: 2018-10-16
featured-image: longest-common-subsequence-in-every-language.jpg
last-modified: 2019-03-21
layout: default
tags:
- longest-common-subsequence
- python
title: Longest Common Subsequence in Python
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-common-subsequence/python/how-to-implement-the-solution.md
- sources/programs/longest-common-subsequence/python/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Common Subsequence](https://sampleprograms.io/projects/longest-common-subsequence) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys


def input_list(list_str):
    return [int(x.strip(" "), 10) for x in list_str.split(',')]


def longest(s1, s2):
    return s1 if len(s1) > len(s2) else s2


def lcs(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return []
    elif s1[-1] == s2[-1]:
        return lcs(s1[:-1], s2[:-1]) + [s1[-1]]
    elif s1[-1] != s2[-1]:
        return longest(lcs(s1, s2[:-1]), lcs(s1[:-1], s2))


def exit_with_error():
    print('Usage: please provide two lists in the format "1, 2, 3, 4, 5"')
    sys.exit(1)


def main(args):
    try:
        lst1 = input_list(args[0])
        lst2 = input_list(args[1])
        print(lcs(lst1, lst2))
    except (IndexError, ValueError):
        exit_with_error()


if __name__ == "__main__":
    main(sys.argv[1:])

```

{% endraw %}

Longest Common Subsequence in [Python](https://sampleprograms.io/languages/python) was written by:

- Boot-Error
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).