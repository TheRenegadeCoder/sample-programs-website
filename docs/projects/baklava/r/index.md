---
authors:
- rzuckerm
date: 2024-10-22
featured-image: baklava-in-every-language.jpg
last-modified: 2024-10-22
layout: default
tags:
- baklava
- r
title: Baklava in R
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/r/how-to-implement-the-solution.md
- sources/programs/baklava/r/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [R](https://sampleprograms.io/languages/r) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```r
for (i in -10:10) {
  numSpaces = abs(i)
  s <- strrep(" ", numSpaces)
  s = paste0(s, strrep("*", 21 - 2 * numSpaces))
  cat(s, "\n", sep="")
}

```

{% endraw %}

Baklava in [R](https://sampleprograms.io/languages/r) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).