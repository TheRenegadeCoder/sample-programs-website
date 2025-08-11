---
authors:
- rzuckerm
date: 2025-08-11
featured-image: fibonacci-in-every-language.jpg
last-modified: 2025-08-11
layout: default
tags:
- fibonacci
- m4
title: Fibonacci in M4
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/m4/how-to-implement-the-solution.md
- sources/programs/fibonacci/m4/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [M4](https://sampleprograms.io/languages/m4) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```m4
divert(-1)
define(`show_usage',
`Usage: please input the count of fibonacci numbers to output
m4exit(`1')')

dnl is_valid(n)
define(`is_valid', `eval(regexp(`$1', `^\s*-?[0-9]+\s*$') >= 0)')

dnl fibonacci(n)
define(`fibonacci',
`ifelse(`$#', 0, ``$0'',
`ifelse(eval(`$1' >= 1), 1, `_fibonacci(`$1', 1, 0, 1)')'dnl
)'dnl
)
dnl _fibonacci(n, k, prev_state, curr_state)
dnl while k <= n:
dnl   Output k ": " curr_state
dnl   prev_state, curr_state = curr_state, prev_state + curr_state
dnl   k = k + 1
define(`_fibonacci',
`ifelse(eval(`$2' <= `$1'), 1,
`$2: $4
_fibonacci(`$1', incr($2), `$4', `eval($3 + $4)')dnl
')')
divert(0)dnl
ifelse(eval(ARGC < 1 || len(ARGV1) < 1 || !is_valid(ARGV1)), 1, `show_usage()', `fibonacci(ARGV1)')dnl

```

{% endraw %}

Fibonacci in [M4](https://sampleprograms.io/languages/m4) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).