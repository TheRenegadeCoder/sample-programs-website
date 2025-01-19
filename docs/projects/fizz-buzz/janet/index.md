---
authors:
- Zia
date: 2025-01-19
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-01-19
layout: default
tags:
- fizz-buzz
- janet
title: Fizz Buzz in Janet
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/janet/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/janet/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Janet](https://sampleprograms.io/languages/janet) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```janet
(loop [n :range [1 101]]
  (print (cond
    (zero? (% n 15)) "FizzBuzz"
    (zero? (% n 5)) "Buzz"
    (zero? (% n 3)) "Fizz"
    n)))

```

{% endraw %}

Fizz Buzz in [Janet](https://sampleprograms.io/languages/janet) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).