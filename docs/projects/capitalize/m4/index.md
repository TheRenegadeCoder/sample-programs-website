---
authors:
- rzuckerm
date: 2025-08-11
featured-image: capitalize-in-every-language.jpg
last-modified: 2025-08-11
layout: default
tags:
- capitalize
- m4
title: Capitalize in M4
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/m4/how-to-implement-the-solution.md
- sources/programs/capitalize/m4/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [M4](https://sampleprograms.io/languages/m4) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```m4
divert(-1)
define(`show_usage',
`Usage: please provide a string
m4exit(`1')')

dnl capitalize(str)
define(`capitalize', `translit(substr(`$1', 0, 1), `a-z', `A-Z')`'substr(`$1', 1)')
divert(0)dnl
ifelse(eval(ARGC < 1 || len(ARGV1) < 1), 1, `show_usage()', `capitalize(ARGV1)')

```

{% endraw %}

Capitalize in [M4](https://sampleprograms.io/languages/m4) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).