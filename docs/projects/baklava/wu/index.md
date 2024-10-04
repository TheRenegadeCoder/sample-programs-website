---
authors:
- rzuckerm
date: 2024-10-03
featured-image: baklava-in-every-language.jpg
last-modified: 2024-10-03
layout: default
tags:
- baklava
- wu
title: Baklava in Wu
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/wu/how-to-implement-the-solution.md
- sources/programs/baklava/wu/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Wu](https://sampleprograms.io/languages/wu) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```wu
repeatString: fun(c: str, count: int) -> str {
    s: str = ""
    while count > 0 {
        s ++= c
        count -= 1
    }

    s
}

i: int = -10
while i <= 10 {
    numSpaces: int = if i >= 0 { i } else { -i }
    print(repeatString(" ", numSpaces) ++ repeatString("*", 21 - 2 * numSpaces))
    i += 1
}

```

{% endraw %}

Baklava in [Wu](https://sampleprograms.io/languages/wu) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).