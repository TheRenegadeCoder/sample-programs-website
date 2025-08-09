---
authors:
- rzuckerm
date: 2025-08-09
featured-image: baklava-in-every-language.jpg
last-modified: 2025-08-09
layout: default
tags:
- baklava
- m4
title: Baklava in M4
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/m4/how-to-implement-the-solution.md
- sources/programs/baklava/m4/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [M4](https://sampleprograms.io/languages/m4) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```m4
divert(-1)
dnl repeat(string, count)
define(`repeat', `ifelse(eval(($2) > 0), 1, `$1'`'`repeat($1, eval(($2) - 1))', )')
dnl indent(count, string)
define(`indent', `ifelse(eval(($1) > 0), 1, `format(`%$1s%s', `', $2)', $2)')
dnl abs(n)
define(`abs', `ifelse(eval(($1) >= 0), 1, eval($1), eval(0 - $1))')
dnl baklava(n, stop)
define(`baklava',
`ifelse(eval($1 <= $2), 1, `baklava_line($1)
baklava(eval($1 + 1), $2)', )'dnl
)
dnl baklava_line(n)
define(`baklava_line', `indent(abs($1), repeat(`*', 21 - 2 * abs($1)))')
divert(0)dnl
baklava(-10, 10)dnl

```

{% endraw %}

Baklava in [M4](https://sampleprograms.io/languages/m4) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).