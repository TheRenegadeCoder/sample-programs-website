---
authors:
- rzuckerm
date: 2025-10-31
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-10-31
layout: default
tags:
- cython
- fizz-buzz
title: Fizz Buzz in Cython
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/cython/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/cython/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Cython](https://sampleprograms.io/languages/cython) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cython
from libc.stdio cimport printf


cdef main():
    cdef int n
    cdef bytes buffer
    for n in range(1, 101):
        buffer = b""
        buffer += b"Fizz" if n % 3 == 0 else b""
        buffer += b"Buzz" if n % 5 == 0 else b""
        buffer += bytes(str(n).encode("ascii")) if not buffer else b""
        printf("%s\n", buffer)

if __name__ == "__main__":
    main()

```

{% endraw %}

Fizz Buzz in [Cython](https://sampleprograms.io/languages/cython) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).