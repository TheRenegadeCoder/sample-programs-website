---
authors:
- Zia
date: 2025-01-07
featured-image: even-odd-in-every-language.jpg
last-modified: 2025-01-07
layout: default
tags:
- elvish
- even-odd
title: Even Odd in Elvish
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/elvish/how-to-implement-the-solution.md
- sources/programs/even-odd/elvish/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Elvish](https://sampleprograms.io/languages/elvish) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```elvish
use re

if (> 1 (count $args)) {
  echo "Usage: please input a number"
  exit 1
}

if (not (re:match '^[+-]?[0-9]+(\.[0-9]+)?$' $args[0])) {
  echo "Usage: please input a number"
  exit 1
}

if (== 0 (% $args[0] 2)) {
  echo Even
} else {
  echo Odd
}

```

{% endraw %}

Even Odd in [Elvish](https://sampleprograms.io/languages/elvish) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).