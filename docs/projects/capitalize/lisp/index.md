---

title: Capitalize in Lisp
layout: default
date: 2022-04-28
last-modified: 2022-05-10

---

Welcome to the Capitalize in Lisp page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).