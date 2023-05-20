---
title: Reverse String in Lisp
layout: default
date: 2020-10-11
featured-image: reverse-string-in-every-language.jpg
last-modified: 2020-10-11

---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Lisp](https://sampleprograms.io/languages/lisp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```lisp
(defparameter input (cadr *posix-argv*))
(cond
  ((null input) ())
  (t (write-line (reverse input)))
)
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Lisp](https://sampleprograms.io/languages/lisp) was written by:

- Parker Johansen
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 19 2023 22:24:49. The solution was first committed on Oct 11 2020 06:55:14. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).