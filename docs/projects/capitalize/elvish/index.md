---
authors:
- Zia
date: 2025-01-18
featured-image: capitalize-in-every-language.jpg
last-modified: 2025-01-18
layout: default
tags:
- capitalize
- elvish
title: Capitalize in Elvish
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/elvish/how-to-implement-the-solution.md
- sources/programs/capitalize/elvish/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Elvish](https://sampleprograms.io/languages/elvish) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```elvish
use str

fn die {
  echo 'Usage: please provide a string'
  exit 1
}

if (> 1 (count $args)) {
  die
}

var s = $args[0]

if (> 1 (count $s)) {
  die
}

echo (str:join '' [(str:to-upper $s[0]) $s[1..]])

```

{% endraw %}

Capitalize in [Elvish](https://sampleprograms.io/languages/elvish) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).