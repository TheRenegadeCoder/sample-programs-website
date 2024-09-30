---
authors:
- rzuckerm
date: 2023-02-16
featured-image: baklava-in-every-language.jpg
last-modified: 2023-02-16
layout: default
tags:
- baklava
- euphoria
title: Baklava in Euphoria
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/euphoria/how-to-implement-the-solution.md
- sources/programs/baklava/euphoria/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Euphoria](https://sampleprograms.io/languages/euphoria) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```euphoria
include std/io.e
include std/math.e

for n = -10 to 10
do
    integer num_spaces = abs(n)
    integer num_stars = 21 - 2 * num_spaces
    printf(STDOUT, "%s%s\n", {repeat(' ', num_spaces), repeat('*', num_stars)})
end for

```

{% endraw %}

Baklava in [Euphoria](https://sampleprograms.io/languages/euphoria) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).