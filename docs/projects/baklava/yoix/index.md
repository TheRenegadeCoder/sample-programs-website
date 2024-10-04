---
authors:
- rzuckerm
date: 2024-10-03
featured-image: baklava-in-every-language.jpg
last-modified: 2024-10-03
layout: default
tags:
- baklava
- yoix
title: Baklava in Yoix
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/yoix/how-to-implement-the-solution.md
- sources/programs/baklava/yoix/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Yoix](https://sampleprograms.io/languages/yoix) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```yoix
import yoix.stdio.putchar;
import yoix.math.abs;

printRepeat(int c, int count) {
    int i;
    for (i = 0; i < count; i++) {
        putchar(c);
    }
}

int i;
for (i = -10; i <= 10; i++) {
    int numSpaces = abs(i);
    int numStars = 21 - 2 * numSpaces;
    printRepeat(' ', numSpaces);
    printRepeat('*', numStars);
    putchar('\n');
}

```

{% endraw %}

Baklava in [Yoix](https://sampleprograms.io/languages/yoix) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).