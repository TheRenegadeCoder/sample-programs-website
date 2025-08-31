---
authors:
- rzuckerm
date: 2025-08-25
featured-image: longest-palindromic-substring-in-every-language.jpg
last-modified: 2025-08-31
layout: default
tags:
- longest-palindromic-substring
- m4
title: Longest Palindromic Substring in M4
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-palindromic-substring/m4/how-to-implement-the-solution.md
- sources/programs/longest-palindromic-substring/m4/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [M4](https://sampleprograms.io/languages/m4) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```m4
divert(-1)
define(`show_usage',
`Usage: please provide a string that contains at least one palindrome
m4exit(`1')')

dnl longest_palindromic_substring(str)
dnl start = 0
dnl max_len = 1
dnl _lps_outer(str, 2)
dnl Return str[start:start+max_len-1]
define(`longest_palindromic_substring',
`pushdef(`start', 0)dnl
pushdef(`max_len', 1)dnl
_lps_outer(`$1', 2)dnl
substr(`$1', start, max_len)`'dnl
popdef(`max_len')dnl
popdef(`start')dnl
'dnl
)

dnl _lps_outer(str, l)
dnl while l <= len(str):
dnl   _lps_inner(str, 0, l)
dnl   l = l + 1
define(`_lps_outer',
`ifelse(eval($2 <= len(`$1')), 1,
`_lps_inner(`$1', 0, $2)dnl
_lps_outer(`$1', incr($2))'dnl
)'dnl
)

dnl _lps_inner(str, k, l)
dnl while k <= len(str) - l and l > max_len:
dnl   if is_palindrome(str, k, k+l-1):
dnl     start = k
dnl     max_len = l
dnl   k = k + 1
define(`_lps_inner',
`ifelse(
eval($2 <= len(`$1') - $3 && $3 > max_len), 1,
`ifelse(
eval(is_palindrome(`$1', $2, eval($2 + $3 - 1))), 1,
`define(`start', $2)dnl
define(`max_len', $3)'dnl
)dnl
_lps_inner(`$1', incr($2), $3)'dnl
)'dnl
)

dnl is_palidrome(str, left, right)
dnl while left < right:
dnl   if str[left] != str[right]:
dnl     Return 0
dnl   left = left + 1
dnl   right = right - 1
dnl Return 1
define(`is_palindrome',
`ifelse(
    eval($2 >= $3), 1, `1',
    substr(`$1', $2, 1), substr(`$1', $3, 1), `is_palindrome(`$1', incr($2), decr($3))', `0'dnl
)'dnl
)
divert(0)dnl
ifelse(eval(ARGC < 1 || len(ARGV1) < 1), 1, `show_usage()')dnl
define(`result', longest_palindromic_substring(ARGV1))dnl
ifelse(eval(len(result) < 2), 1, `show_usage()', `result')

```

{% endraw %}

Longest Palindromic Substring in [M4](https://sampleprograms.io/languages/m4) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).