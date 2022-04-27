# Reverse String in Lisp

## Solution

```Lisp
(defparameter input (cadr *posix-argv*))
(write-line (reverse input))

```