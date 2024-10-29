---
authors:
- rzuckerm
date: 2024-10-28
featured-image: baklava-in-every-language.jpg
last-modified: 2024-10-28
layout: default
tags:
- baklava
- scheme
title: Baklava in Scheme
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/scheme/how-to-implement-the-solution.md
- sources/programs/baklava/scheme/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Scheme](https://sampleprograms.io/languages/scheme) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```scheme
(define (string-repeat n str)
  (fold string-append "" (make-list n str))
)

(define (baklava-line i)
  (define numSpaces (abs i))
  (define numStars (- 21 (* 2 numSpaces)))
  (when (<= i 10)
    (display (string-repeat numSpaces " "))
    (display (string-repeat numStars "*"))
    (newline)
    (baklava-line (+ i 1))
  )
)

(baklava-line -10)

```

{% endraw %}

Baklava in [Scheme](https://sampleprograms.io/languages/scheme) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).