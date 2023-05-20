---
title: Factorial in Lisp
layout: default
date: 2020-10-01
featured-image: factorial-in-every-language.jpg
last-modified: 2020-10-01

---

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

[Factorial](https://sampleprograms.io/projects/factorial) in [Lisp](https://sampleprograms.io/languages/lisp) was written by:

- Parker Johansen
- Renato

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 11 2020 06:48:59. The solution was first committed on Oct 01 2020 17:40:32. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).