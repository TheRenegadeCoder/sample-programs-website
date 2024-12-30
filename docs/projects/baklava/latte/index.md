---
authors:
- rzuckerm
date: 2024-12-30
featured-image: baklava-in-every-language.jpg
last-modified: 2024-12-30
layout: default
tags:
- baklava
- latte
title: Baklava in Latte
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/latte/how-to-implement-the-solution.md
- sources/programs/baklava/latte/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Latte](https://sampleprograms.io/languages/latte) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```latte
def printRepeatString(s:String, n:int)
    if n > 0
        for i in 1.to(n)
            print(s)

for i in (-10).to(10)
    numSpaces:int = i
    if numSpaces < 0
        numSpaces = -numSpaces

    printRepeatString(" ", numSpaces)
    printRepeatString("*" , 21 - 2*numSpaces)
    println()

```

{% endraw %}

Baklava in [Latte](https://sampleprograms.io/languages/latte) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).