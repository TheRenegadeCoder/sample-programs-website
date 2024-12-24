---
authors:
- rzuckerm
date: 2024-12-23
featured-image: baklava-in-every-language.jpg
last-modified: 2024-12-23
layout: default
tags:
- baklava
- owl-lisp
title: Baklava in Owl Lisp
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/owl-lisp/how-to-implement-the-solution.md
- sources/programs/baklava/owl-lisp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Owl Lisp](https://sampleprograms.io/languages/owl-lisp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```owl_lisp
(define (string-repeat n str)
  (fold string-append "" (make-list n str))
)

(define (baklava-line n)
  (define num-spaces (abs n))
  (define num-stars (- 21 (* 2 num-spaces)))
  (print (string-repeat num-spaces " ") (string-repeat num-stars "*"))
)

(define (baklava n ne)
  (if (<= n ne)
    (begin
      (baklava-line n)
      (baklava (+ n 1) ne)
    )
  )
)

(λ (args) (baklava -10 10))

```

{% endraw %}

Baklava in [Owl Lisp](https://sampleprograms.io/languages/owl-lisp) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).