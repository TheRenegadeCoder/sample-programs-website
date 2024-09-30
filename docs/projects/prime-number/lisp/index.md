---
authors:
- Parker Johansen
- Renato
date: 2020-10-01
featured-image: prime-number-in-every-language.jpg
last-modified: 2020-10-11
layout: default
tags:
- lisp
- prime-number
title: Prime Number in Lisp
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/lisp/how-to-implement-the-solution.md
- sources/programs/prime-number/lisp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Lisp](https://sampleprograms.io/languages/lisp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lisp
(defun primep (n)
 (cond
  ((= 0    n)          nil)
  ((= 1    n)          nil)
  ((= 2    n)          T)
   (t
   (loop
     :with root     = (isqrt n)
     :with divisors = (cons 2 (loop :for i :from 3 :to root :by 2 :collect i))
     :for d = (pop divisors)
     :if (zerop (mod n d))
     :do (return nil)
     :else :do (setf divisors (delete-if (lambda (x) (zerop (mod x d))) divisors))
     :while divisors
     :finally (return t)))))

(defun print-bool (b)
  (if b
    (write-line "prime")
    (write-line "composite")))

(defun maybe-pos-int (input)
  (cond
    ((null input) nil)
    ((string= input "") nil)
    ((every #'digit-char-p input) (parse-integer input))
    (t nil)))

(defparameter num (maybe-pos-int (cadr *posix-argv*)))
(cond
  ((null num) (write-line "Usage: please input a non-negative integer"))
  (t (print-bool (primep num))))

```

{% endraw %}

Prime Number in [Lisp](https://sampleprograms.io/languages/lisp) was written by:

- Parker Johansen
- Renato

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).