---
authors:
- Zia
date: 2025-01-15
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2025-01-15
layout: default
tags:
- elvish
- remove-all-whitespace
title: Remove All Whitespace in Elvish
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/elvish/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/elvish/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Elvish](https://sampleprograms.io/languages/elvish) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```elvish
use re

if (> 1 (count $args)) {
  echo "Usage: please provide a string"
  exit 1
}

if (> 1 (count $args[0])) {
  echo "Usage: please provide a string"
  exit 1
}

echo (re:replace '\s' '' $args[0])

```

{% endraw %}

Remove All Whitespace in [Elvish](https://sampleprograms.io/languages/elvish) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).