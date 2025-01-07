---
authors:
- rzuckerm
date: 2025-01-06
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-06
layout: default
tags:
- baklava
- fennel
title: Baklava in Fennel
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/fennel/how-to-implement-the-solution.md
- sources/programs/baklava/fennel/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Fennel](https://sampleprograms.io/languages/fennel) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```fennel
(for [i -10 10]
  (let [
    num-spaces (math.abs i)
    num-stars (- 21 (* 2 num-spaces))
  ]
    (print (.. (string.rep " " num-spaces) (string.rep "*" num-stars)))
  )
)

```

{% endraw %}

Baklava in [Fennel](https://sampleprograms.io/languages/fennel) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).