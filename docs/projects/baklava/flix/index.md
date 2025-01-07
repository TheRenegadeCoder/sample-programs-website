---
authors:
- rzuckerm
date: 2025-01-06
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-06
layout: default
tags:
- baklava
- flix
title: Baklava in Flix
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/flix/how-to-implement-the-solution.md
- sources/programs/baklava/flix/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Flix](https://sampleprograms.io/languages/flix) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```flix
def baklavaLine(n: Int32): String =
    let numSpaces = Int32.abs(n);
    let numStars = 21 - 2 * numSpaces;
    String.repeat(numSpaces, " ") + String.repeat(numStars, "*")

def main(): Unit \ IO =
    List.range(-10, 11) |>
    List.map(baklavaLine) |>
    List.forEach(println)

```

{% endraw %}

Baklava in [Flix](https://sampleprograms.io/languages/flix) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).