---
authors:
- Jeremy Grifski
date: 2022-05-12
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2022-05-12
layout: default
tags:
- python
- remove-all-whitespace
title: Remove All Whitespace in Python
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/python/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/python/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys

error = "Usage: please provide a string"

if len(sys.argv) == 1 or sys.argv[1] == "":
    print(error)
    sys.exit(1)

input_string = sys.argv[1]
print("".join(input_string.split()))

```

{% endraw %}

Remove All Whitespace in [Python](https://sampleprograms.io/languages/python) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).