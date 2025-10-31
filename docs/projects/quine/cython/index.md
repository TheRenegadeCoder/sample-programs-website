---
authors:
- rzuckerm
date: 2025-10-31
featured-image: quine-in-every-language.jpg
last-modified: 2025-10-31
layout: default
tags:
- cython
- quine
title: Quine in Cython
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quine/cython/how-to-implement-the-solution.md
- sources/programs/quine/cython/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quine](https://sampleprograms.io/projects/quine) in [Cython](https://sampleprograms.io/languages/cython) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cython
from libc.stdio cimport printf

def main():
    cdef bytes s = b"""from libc.stdio cimport printf

def main():
    cdef bytes s = b%c%c%c%s%c%c%c
    printf(s, 34, 34, 34, s, 34, 34, 34)

if __name__ == "__main__":
    main()"""
    printf(s, 34, 34, 34, s, 34, 34, 34)

if __name__ == "__main__":
    main()

```

{% endraw %}

Quine in [Cython](https://sampleprograms.io/languages/cython) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).