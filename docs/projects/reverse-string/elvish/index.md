---
authors:
- Zia
date: 2025-01-15
featured-image: reverse-string-in-every-language.jpg
last-modified: 2025-01-15
layout: default
tags:
- elvish
- reverse-string
title: Reverse String in Elvish
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/elvish/how-to-implement-the-solution.md
- sources/programs/reverse-string/elvish/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Elvish](https://sampleprograms.io/languages/elvish) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```elvish
if (> 1 (count $args)) {
  echo ''
  exit
}

echo $args[0] | rev

```

{% endraw %}

Reverse String in [Elvish](https://sampleprograms.io/languages/elvish) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).