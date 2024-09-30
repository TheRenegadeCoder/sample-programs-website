---
authors:
- Parker Johansen
date: 2020-10-11
featured-image: even-odd-in-every-language.jpg
last-modified: 2020-10-11
layout: default
tags:
- even-odd
- lisp
title: Even Odd in Lisp
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/lisp/how-to-implement-the-solution.md
- sources/programs/even-odd/lisp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Lisp](https://sampleprograms.io/languages/lisp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lisp
(defun even-odd (x)
   (cond
     ((evenp x) "Even")
     ((oddp x) "Odd")))

(defun maybe-int (input)
  (cond
    ((null input) nil)
    ((string= input "") nil)
    ((every #'digit-char-p (string-left-trim "-" input)) (parse-integer input))
    (t nil)))

(defparameter num (maybe-int (cadr *posix-argv*)))
(cond
  ((null num) (write-line "Usage: please input a number"))
  (t (write-line (even-odd num))))

```

{% endraw %}

Even Odd in [Lisp](https://sampleprograms.io/languages/lisp) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).