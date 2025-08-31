---
authors:
- rzuckerm
date: 2025-08-15
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2025-08-31
layout: default
tags:
- m4
- palindromic-number
title: Palindromic Number in M4
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/m4/how-to-implement-the-solution.md
- sources/programs/palindromic-number/m4/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [M4](https://sampleprograms.io/languages/m4) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```m4
divert(-1)
define(`show_usage',
`Usage: please input a non-negative integer
m4exit(`1')')

dnl is_valid(n)
define(`is_valid', `eval(regexp(`$1', `^\s*-?[0-9]+\s*$') >= 0)')

dnl is_palindrome(str)
define(`is_palindrome', `_is_palindrome(`$1', 0, decr(len(`$1')))')

dnl _is_palidrome(str, left, right)
dnl while left < right:
dnl   if str[left] != str[right]:
dnl     Return 0
dnl   left = left + 1
dnl   right = right - 1
dnl Return 1
define(`_is_palindrome',
`ifelse(
    eval($2 >= $3), 1, `1',
    substr(`$1', $2, 1), substr(`$1', $3, 1), `_is_palindrome(`$1', incr($2), decr($3))', `0'dnl
)'dnl
)
divert(0)dnl
ifelse(eval(ARGC < 1 || len(ARGV1) < 1 || !is_valid(ARGV1)), 1, `show_usage()')dnl
ifelse(eval(ARGV1 < 0), 1, `show_usage()',)dnl
ifelse(is_palindrome(ARGV1), 1, `true', `false')

```

{% endraw %}

Palindromic Number in [M4](https://sampleprograms.io/languages/m4) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).