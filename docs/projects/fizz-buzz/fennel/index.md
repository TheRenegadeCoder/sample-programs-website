---
authors:
- Zia
date: 2025-01-19
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-01-19
layout: default
tags:
- fennel
- fizz-buzz
title: Fizz Buzz in Fennel
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/fennel/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/fennel/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Fennel](https://sampleprograms.io/languages/fennel) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```fennel
(for [i 1 100]
  (if (= 0 (% i 15))
    (print "FizzBuzz")
    (if (= 0 (% i 5))
      (print "Buzz")
      (if (= 0 (% i 3))
        (print "Fizz")
        (print i)))))

```

{% endraw %}

Fizz Buzz in [Fennel](https://sampleprograms.io/languages/fennel) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).