---
authors:
- rzuckerm
date: 2025-08-13
featured-image: reverse-string-in-every-language.jpg
last-modified: 2025-08-13
layout: default
tags:
- m4
- reverse-string
title: Reverse String in M4
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/m4/how-to-implement-the-solution.md
- sources/programs/reverse-string/m4/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [M4](https://sampleprograms.io/languages/m4) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```m4
divert(-1)
dnl Commas are intepreted as argument separators, so need to change them to something that
dnl won't appear in the argument and then change them back
define(`escape', `translit(``$1'', `,', `«')')
define(`unescape', `translit(``$1'', `«', `,')')

dnl reverse(str)
define(`reverse', `unescape(_reverse(escape(`$1')))')
define(`_reverse', `ifelse(len(`$1'), 0, , `_reverse(substr(`$1', 1))`'substr(`$1', 0, 1)')')
divert(0)dnl
ifelse(ARGC, 0, , `reverse(ARGV1)')

```

{% endraw %}

Reverse String in [M4](https://sampleprograms.io/languages/m4) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).