---
title: Capitalize in Lisp
layout: default
date: 2020-10-09
featured-image: capitalize-in-every-language.jpg
last-modified: 2020-10-09

---

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Lisp](https://sampleprograms.io/languages/lisp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lisp
;;Taken from the Common Lisp Cookbook Project (strings page)
(defun split-string (string)
    (loop for i = 0 then (1+ j)
          as j = (position #\Space string :start i)
          collect (subseq string i j)
          while j))

(defun join-string (lst)
  (when lst
    (concatenate 'string (car lst) " " (join-string (cdr lst)))))

 (defun capitalize (str)
   (concatenate 'string
     (string-upcase (subseq str 0 1)) (subseq str 1)))

(defparameter input (split-string (cadr *posix-argv*)))
(cond
  ((= (length (car input)) 0) (write-line "Usage: please provide a string"))
  (t (write-line (join-string (cons (capitalize (car input)) (cdr input))))))
```

{% endraw %}

[Capitalize](https://sampleprograms.io/projects/capitalize) in [Lisp](https://sampleprograms.io/languages/lisp) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 11 2020 10:18:56. The solution was first committed on Oct 09 2020 11:46:14. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).