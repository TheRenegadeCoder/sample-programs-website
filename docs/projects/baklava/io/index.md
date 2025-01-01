---
authors:
- rzuckerm
date: 2025-01-01
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-01
layout: default
tags:
- baklava
- io
title: Baklava in Io
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/io/how-to-implement-the-solution.md
- sources/programs/baklava/io/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Io](https://sampleprograms.io/languages/io) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```io
baklavaLine := method(n,
    num_spaces := n abs
    num_stars := 21 - (2 * num_spaces)
    (" " repeated(num_spaces)) .. ("*" repeated(num_stars))
)

for(n, -10, 10, baklavaLine(n) println)

```

{% endraw %}

Baklava in [Io](https://sampleprograms.io/languages/io) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).