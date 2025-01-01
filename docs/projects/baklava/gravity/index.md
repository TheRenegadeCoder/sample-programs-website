---
authors:
- rzuckerm
date: 2025-01-01
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-01
layout: default
tags:
- baklava
- gravity
title: Baklava in Gravity
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/gravity/how-to-implement-the-solution.md
- sources/programs/baklava/gravity/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Gravity](https://sampleprograms.io/languages/gravity) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```gravity
func main() {
    for (var n in -10...10) {
        var numSpaces = Math.abs(n)
        var numStars = 21 - 2 * numSpaces
        var spaces = (numSpaces > 0) ? " ".repeat(numSpaces) : ""
        var stars = "*".repeat(numStars)
        System.print(spaces + stars)
    }
}

```

{% endraw %}

Baklava in [Gravity](https://sampleprograms.io/languages/gravity) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).