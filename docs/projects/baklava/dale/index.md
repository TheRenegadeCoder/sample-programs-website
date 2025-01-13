---
authors:
- rzuckerm
date: 2025-01-13
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-13
layout: default
tags:
- baklava
- dale
title: Baklava in Dale
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/dale/how-to-implement-the-solution.md
- sources/programs/baklava/dale/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Dale](https://sampleprograms.io/languages/dale) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```dale
(import cstdio)
(import stdlib)
(import cmath)
(import cstring)

(def main (fn extern-c int (void)
  (def n (var auto int))
  (def num-spaces (var auto int))
  (def num-stars (var auto int))
  (def line (var auto (array-of 22 char)))

  (for (setv n -10) (<= n 10) (incv n)
    (do
      (setv num-spaces (abs n))
      (setv num-stars (- 21 (* 2 num-spaces)))

      ; Fill line with num-spaces " "
      (memset (cast line (p void)) #\SPACE num-spaces)

      ; Append num-stars "*" to line
      (memset (cast ($ line num-spaces) (p void)) #\* num-stars)

      ; Null terminate line
      (setf ($ line (+ num-spaces num-stars)) #\NULL)

      (printf "%s\n" line)
    )
  )
))

```

{% endraw %}

Baklava in [Dale](https://sampleprograms.io/languages/dale) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).