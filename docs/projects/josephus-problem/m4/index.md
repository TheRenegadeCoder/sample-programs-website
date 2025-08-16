---
authors:
- rzuckerm
date: 2025-08-16
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2025-08-16
layout: default
tags:
- josephus-problem
- m4
title: Josephus Problem in M4
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/josephus-problem/m4/how-to-implement-the-solution.md
- sources/programs/josephus-problem/m4/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [M4](https://sampleprograms.io/languages/m4) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```m4
divert(-1)
define(`show_usage',
`Usage: please input the total number of people and number of people to skip.
m4exit(`1')')

dnl is_valid(n)
define(`is_valid', `eval(regexp(`$1', `^\s*-?[0-9]+\s*$') >= 0)')

dnl josephus_problem(n, k)
dnl Reference: https://en.wikipedia.org/wiki/Josephus_problem#The_general_case
dnl
dnl Use zero-based index algorithm:
dnl
dnl     g(1, k) = 0
dnl     g(m, k) = [g(m - 1, k) + k] MOD m, for m = 2, 3, ..., n
dnl
dnl Final answer is g(n, k) + 1 to get back to one-based index
define(`josephus_problem', `_josephus_problem(`$1', `$2', 0, 2)')

dnl _josephus_problem(n, k, g, m)
dnl while m <= n:
dnl   g = (g + k) % m
dnl   m = m + 1
dnl Return g + 1
define(`_josephus_problem',
`ifelse(eval(`$4' <= `$1'), 1,
    `_josephus_problem(`$1', `$2', eval((`$3' + `$2') % `$4'), incr(`$4'))',
    `incr(`$3')'dnl
)'dnl
)
divert(0)dnl
ifelse(eval(ARGC < 2 || !is_valid(ARGV1) || !is_valid(ARGV2)), 1,
    `show_usage()', `josephus_problem(ARGV1, ARGV2)')

```

{% endraw %}

Josephus Problem in [M4](https://sampleprograms.io/languages/m4) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).