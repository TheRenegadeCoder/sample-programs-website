---
authors:
- Jeremy Grifski
- Parker Johansen
date: 2018-12-23
featured-image: rot13-in-every-language.jpg
last-modified: 2020-10-15
layout: default
tags:
- python
- rot13
title: Rot13 in Python
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/python/how-to-implement-the-solution.md
- sources/programs/rot13/python/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys
from string import ascii_uppercase, ascii_lowercase


def rot_13(string):
    return ''.join([encrypt_char(c) for c in string])


def encrypt_char(c):
    if c in ascii_uppercase:
        ltrs = ascii_uppercase
    elif c in ascii_lowercase:
        ltrs = ascii_lowercase
    else:
        return c
    new_index = (ltrs.index(c) + 13) % 26
    return ltrs[new_index]


def exit_with_error():
    print('Usage: please provide a string to encrypt')
    sys.exit(1)


def main(args):
    try:
        string = args[0]
        if len(string) <= 0:
            exit_with_error()
        print(rot_13(string))
    except (IndexError, ValueError):
        exit_with_error()


if __name__ == "__main__":
    main(sys.argv[1:])

```

{% endraw %}

Rot13 in [Python](https://sampleprograms.io/languages/python) was written by:

- Jeremy Grifski
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).