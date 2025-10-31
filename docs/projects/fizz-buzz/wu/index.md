---
authors:
- jmakho01
date: 2025-10-31
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-10-31
layout: default
tags:
- fizz-buzz
- wu
title: Fizz Buzz in Wu
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/wu/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/wu/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Wu](https://sampleprograms.io/languages/wu) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```wu
i: int = 1
while i <= 100 {
    o: str = ""
    if i % 3 == 0 {
        o ++= "Fizz"
    } 
    if i % 5 == 0 {
        o ++= "Buzz"
    }
    if i % 3 != 0 and i % 5 != 0 {
        o ++= i
    }
    print(o)
    i += 1
}
```

{% endraw %}

Fizz Buzz in [Wu](https://sampleprograms.io/languages/wu) was written by:

- jmakho01

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).