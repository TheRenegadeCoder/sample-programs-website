---
authors:
- Jeremy Grifski
date: 2022-05-13
featured-image: transpose-matrix-in-every-language.jpg
last-modified: 2022-05-13
layout: default
tags:
- python
- transpose-matrix
title: Transpose Matrix in Python
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/transpose-matrix/python/how-to-implement-the-solution.md
- sources/programs/transpose-matrix/python/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Transpose Matrix](https://sampleprograms.io/projects/transpose-matrix) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys

if len(sys.argv) != 4 or any(not x for x in sys.argv[1:]):
    print("Usage: please enter the dimension of the matrix and the serialized matrix")
    sys.exit(1)
    
columns = int(sys.argv[1])
rows = int(sys.argv[2])
serial_matrix = [int(x) for x in sys.argv[3].split(',')]
matrix = [[serial_matrix[i * columns + j] for j in range(columns)] for i in range(rows)]
transposed_matrix = [[matrix[j][i] for j in range(rows)] for i in range(columns)]
serial_transposed_matrix = [x for row in transposed_matrix for x in row]
print(serial_transposed_matrix)

```

{% endraw %}

Transpose Matrix in [Python](https://sampleprograms.io/languages/python) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).