---
authors:
- rzuckerm
date: 2025-01-13
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-13
layout: default
tags:
- baklava
- elena
title: Baklava in Elena
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/elena/how-to-implement-the-solution.md
- sources/programs/baklava/elena/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Elena](https://sampleprograms.io/languages/elena) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```elena
import extensions;
import extensions'text;
import extensions'math;

public program()
{
    int space := " "[0].toInt();
    int star := "*"[0].toInt();
    for (int n := -10; n <= 10; n++) {
        int num_spaces := abs(n);
        int num_stars := 21 - 2 * num_spaces;
        console.writeLine(String.fill(num_spaces, space) + String.fill(num_stars, star));
    }
}

```

{% endraw %}

Baklava in [Elena](https://sampleprograms.io/languages/elena) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).