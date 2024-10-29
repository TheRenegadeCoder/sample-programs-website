---
authors:
- rzuckerm
date: 2024-10-28
featured-image: baklava-in-every-language.jpg
last-modified: 2024-10-28
layout: default
tags:
- baklava
- shen
title: Baklava in Shen
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/shen/how-to-implement-the-solution.md
- sources/programs/baklava/shen/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Shen](https://sampleprograms.io/languages/shen) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```shen
(define string-repeat
  N C -> (if (> N 0) (cn C (string-repeat (- N 1) C)) "")
)

(define abs
  N -> (if (< N 0) (- 0 N) N)
)

(define spaces
  N -> (string-repeat (abs N) " ")
)

(define stars
  N -> (string-repeat (- 21 (* 2 (abs N))) "*")
)

(define baklava
  N -> (if (<= N 10)
    (do
      (output "~A~A~%" (spaces N) (stars N))
      (baklava (+ 1 N))
    )
    (output "")
  )
)

(baklava -10)

```

{% endraw %}

Baklava in [Shen](https://sampleprograms.io/languages/shen) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).