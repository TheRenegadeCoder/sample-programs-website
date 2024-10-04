---
authors:
- rzuckerm
date: 2024-10-03
featured-image: baklava-in-every-language.jpg
last-modified: 2024-10-03
layout: default
tags:
- baklava
- wyvern
title: Baklava in Wyvern
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/wyvern/how-to-implement-the-solution.md
- sources/programs/baklava/wyvern/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Wyvern](https://sampleprograms.io/languages/wyvern) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```wyvern
require stdout

def strRepeat(n:Int, s:String): String
    if (n < 1) { "" } else { s + strRepeat(n - 1, s) }

def abs(n:Int): Int
    if (n < 0) { -n } else { n }

def baklava(n:Int, end:Int): Unit
    // This is definitely the weirdest formatting for an if-else statement that I've ever seen
    if (n > end)
            unit
        else
            val numSpaces:Int = abs(n)
            stdout.print(strRepeat(numSpaces, " ") + strRepeat(21 - 2 * numSpaces, "*") + "\n")
            baklava(n + 1, end)

baklava(-10, 10)

```

{% endraw %}

Baklava in [Wyvern](https://sampleprograms.io/languages/wyvern) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).