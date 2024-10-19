---
authors:
- rzuckerm
date: 2024-10-17
featured-image: baklava-in-every-language.jpg
last-modified: 2024-10-17
layout: default
tags:
- baklava
- red
title: Baklava in Red
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/red/how-to-implement-the-solution.md
- sources/programs/baklava/red/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Red](https://sampleprograms.io/languages/red) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```red
Red [Title: "Bakalava"]

s: ""
repeat i 21 [
    numSpaces: i - 11
    if numSpaces < 0 [numSpaces: 0 - numSpaces]
    clear s
    insert/dup tail s " " numSpaces
    insert/dup tail s "*" (21 - (2 * numSpaces))
    print s
]

```

{% endraw %}

Baklava in [Red](https://sampleprograms.io/languages/red) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).