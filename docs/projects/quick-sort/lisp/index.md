---
title: Quick Sort in Lisp
layout: default
date: 2020-10-04
featured-image: quick-sort-in-every-language.jpg
last-modified: 2020-10-04

---

Welcome to the [Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Lisp](https://sampleprograms.io/languages/lisp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lisp
(defun qsort (L)
  (cond
    ((null L) nil)
    (t
      (append
        (qsort (list< (car L) (cdr L)))
        (cons (car L) nil) 
        (qsort (list>= (car L) (cdr L)))))))

(defun list< (a b)
  (cond
    ((or (null a) (null b)) nil)
    ((< a (car b)) (list< a (cdr b)))
    (t (cons (car b) (list< a (cdr b))))))

(defun list>= (a b)
  (cond
    ((or (null a) (null b)) nil)
    ((>= a (car b)) (list>= a (cdr b)))
    (t (cons (car b) (list>= a (cdr b))))))

;;Taken from the Common Lisp Cookbook Project (strings page)
(defun split-string (string)
    (loop for i = 0 then (1+ j)
          as j = (position #\, string :start i)
          collect (subseq string i j)
          while j))

(defun join-string (lst)
  (reduce
    (lambda (acc n)
      (concatenate 'string acc ", " (princ-to-string n))) (cdr lst)
        :initial-value (princ-to-string (car lst))))

(defun maybe-int (input)
  (cond
    ((null input) nil)
    ((string= input "") nil)
    ((every #'digit-char-p (string-left-trim "-" input)) (parse-integer input))
    (t nil)))

(defun maybe-int-list (input-list &optional (acc))
  (cond
    ((<= (length input-list) 0) acc)
    (t
      (let ((i (maybe-int (string-trim " " (car input-list)))))
        (cond
          ((null i) nil)
          (t (maybe-int-list (cdr input-list) (cons i acc))))))))


(defparameter input (maybe-int-list (split-string (cadr *posix-argv*))))
(cond
  ((or (null input) (= (length input) 1)) (write-line "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\""))
  (t (write-line (join-string (qsort input)))))
```

{% endraw %}

[Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Lisp](https://sampleprograms.io/languages/lisp) was written by:

- Palash Dubey
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 11 2020 09:45:24. The solution was first committed on Oct 04 2020 18:08:31. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).