---
authors:
- Parker Johansen
- Renato
date: 2020-10-01
featured-image: factorial-in-every-language.jpg
last-modified: 2020-10-11
layout: default
tags:
- factorial
- lisp
title: Factorial in Lisp
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/lisp/how-to-implement-the-solution.md
- sources/programs/factorial/lisp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Lisp](https://sampleprograms.io/languages/lisp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lisp
(defun factorial (n)
  (if (= n 0)
      1
      (* n (factorial (- n 1))) ) )

(defun maybe-pos-int (input)
  (cond
    ((null input) nil)
    ((string= input "") nil)
    ((every #'digit-char-p input) (parse-integer input))
    (t nil)))

(defparameter num (maybe-pos-int (cadr *posix-argv*)))
(cond
  ((null num) (write-line "Usage: please input a non-negative integer"))
  (t (print (factorial num)))
)
```

{% endraw %}

Factorial in [Lisp](https://sampleprograms.io/languages/lisp) was written by:

- Parker Johansen
- Renato

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).