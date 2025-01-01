---
authors:
- rzuckerm
date: 2025-01-01
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-01
layout: default
tags:
- baklava
- golo
title: Baklava in Golo
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/golo/how-to-implement-the-solution.md
- sources/programs/baklava/golo/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Golo](https://sampleprograms.io/languages/golo) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```golo
module baklava

function main = |args| {
    for (var n = -10, n <= 10, n = n + 1) {
        let numSpaces = Math.abs(n)
        let numStars = 21 - 2 * numSpaces
        println(" " * numSpaces + "*" * numStars)
    }
}

```

{% endraw %}

Baklava in [Golo](https://sampleprograms.io/languages/golo) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).