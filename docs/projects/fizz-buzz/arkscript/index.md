---
authors:
- Zia
date: 2025-01-19
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-01-19
layout: default
tags:
- arkscript
- fizz-buzz
title: Fizz Buzz in Arkscript
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/arkscript/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/arkscript/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Arkscript](https://sampleprograms.io/languages/arkscript) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```arkscript
(mut i 1)
(
    while (<= i 100) {
    (
        if (= 0 (mod i 15)) (print "FizzBuzz") (
            if (= 0 (mod i 5)) (print "Buzz")
            (if (= 0 (mod i 3)) (print "Fizz")
            (print i))))
    (set i (+ i 1))
    }
)

```

{% endraw %}

Fizz Buzz in [Arkscript](https://sampleprograms.io/languages/arkscript) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).