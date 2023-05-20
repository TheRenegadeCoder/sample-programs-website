---
title: Prime Number in Lisp
layout: default
date: 2020-10-01
featured-image: prime-number-in-every-language.jpg
last-modified: 2020-10-01

---

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

[Prime Number](https://sampleprograms.io/projects/prime-number) in [Lisp](https://sampleprograms.io/languages/lisp) was written by:

- Parker Johansen
- Renato

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 11 2020 06:48:59. The solution was first committed on Oct 01 2020 10:54:37. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).