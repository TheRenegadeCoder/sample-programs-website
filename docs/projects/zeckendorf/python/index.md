---
authors:
- rzuckerm
date: 2026-01-19
featured-image: zeckendorf-in-every-language.png
last-modified: 2026-01-19
layout: default
tags:
- python
- zeckendorf
title: Zeckendorf in Python
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/zeckendorf/python/how-to-implement-the-solution.md
- sources/programs/zeckendorf/python/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Zeckendorf](https://sampleprograms.io/projects/zeckendorf) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys
from typing import NoReturn


def usage() -> NoReturn:
    print("Usage: please input a non-negative integer")
    sys.exit(1)


def fibonacci_up_to(n: int) -> list[int]:
    result: list[int] = []
    a = 1
    b = 2
    while a <= n:
        result.append(a)
        a, b = b, a + b

    return result


def zeckendorf(n: int) -> list[int]:
    result: list[int] = []
    fibs = fibonacci_up_to(n)
    idx = len(fibs) - 1
    while idx >= 0 and n > 0:
        fib = fibs[idx]
        if fib <= n:
            n -= fib
            result.append(fib)
            idx -= 2
        else:
            idx -= 1

    return result


def main() -> int:
    if len(sys.argv) < 2:
        usage()

    try:
        n = int(sys.argv[1])
    except ValueError:
        usage()

    if n < 0:
        usage()

    result = zeckendorf(n)
    print(result)


if __name__ == "__main__":
    main()

```

{% endraw %}

Zeckendorf in [Python](https://sampleprograms.io/languages/python) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).