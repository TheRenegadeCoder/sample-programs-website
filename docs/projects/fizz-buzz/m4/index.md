---
authors:
- rzuckerm
date: 2025-08-09
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-08-09
layout: default
tags:
- fizz-buzz
- m4
title: Fizz Buzz in M4
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/m4/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/m4/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [M4](https://sampleprograms.io/languages/m4) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```m4
divert(-1)
define(`fizzbuzz',
`ifelse(eval($1 <= $2), 1,
`ifelse(eval($1 % 15), 0, FizzBuzz,
`ifelse(eval($1 % 3), 0, Fizz,
`ifelse(eval($1 % 5), 0, Buzz, $1)')')'
`fizzbuzz(eval($1 + 1), $2)', )'dnl
)
divert(0)dnl
fizzbuzz(1, 100)dnl

```

{% endraw %}

Fizz Buzz in [M4](https://sampleprograms.io/languages/m4) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).