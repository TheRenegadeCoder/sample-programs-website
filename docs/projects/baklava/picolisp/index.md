---
authors:
- rzuckerm
date: 2024-12-21
featured-image: baklava-in-every-language.jpg
last-modified: 2024-12-21
layout: default
tags:
- baklava
- picolisp
title: Baklava in Picolisp
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/picolisp/how-to-implement-the-solution.md
- sources/programs/baklava/picolisp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Picolisp](https://sampleprograms.io/languages/picolisp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```picolisp
(de repeat_string (S N)
  (if (> N 0)
    (pack S (repeat_string S (- N 1)))
    ""
  )
)

(for X 21
  (setq N (- X 11))
  (setq NSP (abs N))
  (setq NST (- 21 (* 2 NSP)))
  (prinl (pack (repeat_string " " NSP) (repeat_string "*" NST)))
)
(bye)

```

{% endraw %}

Baklava in [Picolisp](https://sampleprograms.io/languages/picolisp) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).