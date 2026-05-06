---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-06
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2026-05-06
layout: default
tags:
- r
- remove-all-whitespace
title: Remove All Whitespace in R
title1: Remove All
title2: Whitespace in R
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/r/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/r/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [R](https://sampleprograms.io/languages/r)emove All Whitespace in [R](https://sampleprograms.io/languages/r) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```r
args <- commandArgs(trailingOnly = TRUE)

if (length(args) != 1 || !nzchar(args[[1]])) {
  cat("Usage: please provide a string\n")
  quit(status = 1)
}

cat(gsub("\\s+", "", args[[1]]), "\n")
```

{% endraw %}

[R](https://sampleprograms.io/languages/r)emove All Whitespace in [R](https://sampleprograms.io/languages/r) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).