---
authors:
- rzuckerm
date: 2025-01-01
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-01
layout: default
tags:
- baklava
- gerbil
title: Baklava in Gerbil
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/gerbil/how-to-implement-the-solution.md
- sources/programs/baklava/gerbil/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Gerbil](https://sampleprograms.io/languages/gerbil) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```gerbil
(import :std/iter)
(import :std/misc/func)

(export main)

(def (string-repeat n str)
    (string-join (repeat str n) "")
)

(def (main . args)
  (for (i (in-range -10 11))
    (def num-spaces (abs i))
    (def num-stars (- 21 (* 2 num-spaces)))
    (displayln (string-repeat num-spaces " ") (string-repeat num-stars "*"))
  )
)

```

{% endraw %}

Baklava in [Gerbil](https://sampleprograms.io/languages/gerbil) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).