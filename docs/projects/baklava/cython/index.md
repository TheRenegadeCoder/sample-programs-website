---
authors:
- rzuckerm
date: 2025-10-31
featured-image: baklava-in-every-language.jpg
last-modified: 2025-10-31
layout: default
tags:
- baklava
- cython
title: Baklava in Cython
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/cython/how-to-implement-the-solution.md
- sources/programs/baklava/cython/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Cython](https://sampleprograms.io/languages/cython) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cython
from libc.stdio cimport printf


cdef main():
    cdef int n
    cdef int num_spaces
    cdef int num_stars
    cdef bytes buffer
    for n in range(-10, 11):
        num_spaces = abs(n)
        num_stars = 21 - 2 * num_spaces
        buffer = b" " * num_spaces + b"*" * num_stars
        printf(b"%s\n", buffer)


if __name__ == "__main__":
    main()

```

{% endraw %}

Baklava in [Cython](https://sampleprograms.io/languages/cython) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).