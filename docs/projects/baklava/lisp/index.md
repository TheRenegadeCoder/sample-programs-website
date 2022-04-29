---

title: Baklava in Lisp
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Baklava in Lisp page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Lisp
(defparameter space_list '(#\space))
(defparameter star_list '(#\*))
(dotimes (run 9)
	(push #\space space_list))
(dotimes (run 10)
    (write-line (concatenate 'string space_list star_list))
    (pop space_list)
    (push #\* star_list)
    (push #\* star_list)
)
(dotimes (run 11)
    (write-line (concatenate 'string space_list star_list))
    (pop star_list)
    (pop star_list)
    (push #\space space_list)
)
```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.