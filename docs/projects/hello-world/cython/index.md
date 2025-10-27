---
authors:
- rzuckerm
date: 2025-10-27
featured-image: hello-world-in-every-language.jpg
last-modified: 2025-10-27
layout: default
tags:
- cython
- hello-world
title: Hello World in Cython
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/cython/how-to-implement-the-solution.md
- sources/programs/hello-world/cython/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Cython](https://sampleprograms.io/languages/cython) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cython
from libc.stdio cimport printf


cdef main():
    printf(b"%s\n", b"Hello, World!")


if __name__ == "__main__":
    main()

```

{% endraw %}

Hello World in [Cython](https://sampleprograms.io/languages/cython) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).