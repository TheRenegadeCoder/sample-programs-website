---
authors:
- rzuckerm
date: 2025-04-17
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-04-17
layout: default
tags:
- boo
- fizz-buzz
title: Fizz Buzz in Boo
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/boo/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/boo/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Boo](https://sampleprograms.io/languages/boo) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```boo
for n in range(1, 101):
    s = ""
    s += "Fizz" if n % 3 == 0
    s += "Buzz" if n % 5 == 0
    s += "$(n)" if not s
    print s

```

{% endraw %}

Fizz Buzz in [Boo](https://sampleprograms.io/languages/boo) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).