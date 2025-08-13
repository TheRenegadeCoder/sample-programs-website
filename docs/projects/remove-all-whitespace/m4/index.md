---
authors:
- rzuckerm
date: 2025-08-13
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2025-08-13
layout: default
tags:
- m4
- remove-all-whitespace
title: Remove All Whitespace in M4
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/m4/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/m4/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [M4](https://sampleprograms.io/languages/m4) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```m4
divert(-1)
define(`show_usage',
`Usage: please provide a string
m4exit(`1')')

define(`remove_all_whitespace', `patsubst(`$1', `\s')')
divert(0)dnl
ifelse(eval(ARGC < 1 || len(ARGV1) < 1), 1, `show_usage()', `remove_all_whitespace(ARGV1)')

```

{% endraw %}

Remove All Whitespace in [M4](https://sampleprograms.io/languages/m4) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).