---

title: Even Odd in Lisp
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Even Odd in Lisp page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Lisp
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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).