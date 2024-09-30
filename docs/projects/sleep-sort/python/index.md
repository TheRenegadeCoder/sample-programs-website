---
authors:
- aymaneMx
- Jeremy Grifski
date: 2020-10-02
featured-image: sleep-sort-in-every-language.jpg
last-modified: 2020-10-15
layout: default
tags:
- python
- sleep-sort
title: Sleep Sort in Python
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/sleep-sort/python/how-to-implement-the-solution.md
- sources/programs/sleep-sort/python/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [Python](https://sampleprograms.io/languages/python) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```python
import sys
import threading
from time import sleep


def arg_to_list(string):
    return [int(x.strip(" "), 10) for x in string.split(',')]


def sleep_sort(i, output):
    sleep(i)
    output.append(i)


def error_and_exit():
    print('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"')
    sys.exit()


def main():
    if len(sys.argv) == 1 or not sys.argv[1] or len(sys.argv[1].split(",")) == 1:
        error_and_exit()

    array = arg_to_list(sys.argv[1])

    threads = []
    output = []
    for i in array:
        arg_tuple = (i, output)
        thread = threading.Thread(target=sleep_sort, args=arg_tuple)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(output)


main()

```

{% endraw %}

Sleep Sort in [Python](https://sampleprograms.io/languages/python) was written by:

- aymaneMx
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).