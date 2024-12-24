---
authors:
- rzuckerm
date: 2024-12-23
featured-image: baklava-in-every-language.jpg
last-modified: 2024-12-23
layout: default
tags:
- baklava
- orc
title: Baklava in Orc
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/orc/how-to-implement-the-solution.md
- sources/programs/baklava/orc/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Orc](https://sampleprograms.io/languages/orc) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```orc
def Baklava(start, end) =
    Ift(start <= end) >>
        Println(BaklavaLine(start)) >>
        Baklava(start + 1, end)

def BaklavaLine(n) = 
    val num_spaces = abs(n)
    val num_stars = 21 - 2 * num_spaces
    RepeatString(" ", num_spaces) + RepeatString("*", num_stars)

def RepeatString(s, n) = if n <: 1 then "" else s + RepeatString(s, n - 1)

Baklava(-10, 10) >>
stop

```

{% endraw %}

Baklava in [Orc](https://sampleprograms.io/languages/orc) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).