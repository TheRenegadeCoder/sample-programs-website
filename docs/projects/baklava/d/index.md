---
authors:
- Jeremy Grifski
date: 2018-09-17
featured-image: baklava-in-every-language.jpg
last-modified: 2018-09-17
layout: default
tags:
- baklava
- d
title: Baklava in D
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/d/how-to-implement-the-solution.md
- sources/programs/baklava/d/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [D](https://sampleprograms.io/languages/d) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```d
import std.stdio, std.array;

void main (string[ ] args)
{

    for (byte i = 0; i < 10; i++)
        writeln (
            " ".replicate (10 - i), "*".replicate (i * 2 + 1)
        );

    for (byte i = 10; -1 < i; i--)
        writeln (
            " ".replicate (10 - i), "*".replicate (i * 2 + 1)
        );

}

```

{% endraw %}

Baklava in [D](https://sampleprograms.io/languages/d) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).