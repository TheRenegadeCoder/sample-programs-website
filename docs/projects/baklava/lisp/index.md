---
title: Baklava in Lisp
layout: default
date: 2019-11-09
featured-image: baklava-in-every-language.jpg
last-modified: 2019-11-09

---

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Lisp](https://sampleprograms.io/languages/lisp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lisp
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

[Baklava](https://sampleprograms.io/projects/baklava) in [Lisp](https://sampleprograms.io/languages/lisp) was written by:

- Parker Johansen
- Stuart Irwin

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 09 2020 11:45:55. The solution was first committed on Nov 09 2019 13:11:46. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).