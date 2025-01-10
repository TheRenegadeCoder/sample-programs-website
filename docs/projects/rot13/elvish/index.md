---
authors:
- Zia
date: 2025-01-10
featured-image: rot13-in-every-language.jpg
last-modified: 2025-01-10
layout: default
tags:
- elvish
- rot13
title: Rot13 in Elvish
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/elvish/how-to-implement-the-solution.md
- sources/programs/rot13/elvish/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Elvish](https://sampleprograms.io/languages/elvish) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```elvish
use str

if (> 1 (count $args)) {
  echo "Usage: please provide a string to encrypt"
  exit 1
}
if (== 0 (str:compare $args[0] '')) {
  echo "Usage: please provide a string to encrypt"
  exit 1
}

echo $@args | tr 'A-Za-z' 'N-ZA-Mn-za-m'

```

{% endraw %}

Rot13 in [Elvish](https://sampleprograms.io/languages/elvish) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).