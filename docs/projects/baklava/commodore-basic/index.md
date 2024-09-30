---
authors:
- rzuckerm
date: 2023-09-16
featured-image: baklava-in-every-language.jpg
last-modified: 2023-09-16
layout: default
tags:
- baklava
- commodore-basic
title: Baklava in Commodore Basic
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/commodore-basic/how-to-implement-the-solution.md
- sources/programs/baklava/commodore-basic/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Commodore Basic](https://sampleprograms.io/languages/commodore-basic) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```commodore_basic
10 FOR I = -10 TO 10
20     NSP% = ABS(I)
30     SP$ = ""
40     IF NSP% = 0 GOTO 80
50     FOR J = 1 TO NSP%
60         SP$ = SP$ + " "
70     NEXT J
80     ST$ = ""
90     FOR J = 1 TO 21 - 2 * NSP%
100         ST$ = ST$ + "*"
110     NEXT J
120     PRINT SP$ + ST$
130 NEXT I

```

{% endraw %}

Baklava in [Commodore Basic](https://sampleprograms.io/languages/commodore-basic) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).