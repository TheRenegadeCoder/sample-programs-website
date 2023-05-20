---
title: Fibonacci in Lisp
layout: default
date: 2020-10-10
featured-image: fibonacci-in-every-language.jpg
last-modified: 2020-10-10

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Lisp](https://sampleprograms.io/languages/lisp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lisp
(defun fibonacci (n &optional (a 1) (b 1) (acc))
  (if (<= n 0)
      (reverse acc)
      (fibonacci (- n 1) b (+ a b) (cons a acc))))

(defun countfibs(acc n fibs)
  (if (< (length fibs) 1)
      (reverse acc)
      (countfibs (cons (list n (car fibs)) acc) (+ 1 n) (cdr fibs))))

(defun maybe-pos-int (input)
  (cond
    ((null input) nil)
    ((string= input "") nil)
    ((every #'digit-char-p input) (parse-integer input))
    (t nil)))

(defparameter num (maybe-pos-int (cadr *posix-argv*)))
(cond
  ((null num) (write-line "Usage: please input the count of fibonacci numbers to output"))
  (t (dolist (item (countfibs (list) 1 (fibonacci num)))
    (format t "~D: ~D~%" (car item) (cadr item)))))
```

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Lisp](https://sampleprograms.io/languages/lisp) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 11 2020 10:18:56. The solution was first committed on Oct 10 2020 18:17:08. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).