---
authors:
- Parker Johansen
- Stuart Irwin
date: 2019-11-09
featured-image: baklava-in-every-language.jpg
last-modified: 2020-10-09
layout: default
tags:
- baklava
- lisp
title: Baklava in Lisp
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/lisp/how-to-implement-the-solution.md
- sources/programs/baklava/lisp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

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

Baklava in [Lisp](https://sampleprograms.io/languages/lisp) was written by:

- Parker Johansen
- Stuart Irwin

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).