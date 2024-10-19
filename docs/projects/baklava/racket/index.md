---
authors:
- rzuckerm
date: 2024-10-19
featured-image: baklava-in-every-language.jpg
last-modified: 2024-10-19
layout: default
tags:
- baklava
- racket
title: Baklava in Racket
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/racket/how-to-implement-the-solution.md
- sources/programs/baklava/racket/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Racket](https://sampleprograms.io/languages/racket) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```racket
#lang racket
(for ([i (in-range -10 11)])
    (define numSpaces (abs i))
    (define numStars (- 21 (* numSpaces 2)))
    (define s (make-string numSpaces #\ ))
    (define t (make-string numStars #\*))
    (printf "~a~a\n" s t)
)

```

{% endraw %}

Baklava in [Racket](https://sampleprograms.io/languages/racket) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).