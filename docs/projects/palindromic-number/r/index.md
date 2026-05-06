---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-06
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2026-05-06
layout: default
tags:
- palindromic-number
- r
title: Palindromic Number in R
title1: Palindromic
title2: Number in R
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/r/how-to-implement-the-solution.md
- sources/programs/palindromic-number/r/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [R](https://sampleprograms.io/languages/r) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```r
args <- commandArgs(trailingOnly = TRUE)

USAGE <- "Usage: please input a non-negative integer"

if (length(args) != 1 || !nzchar(x <- args[[1]]) || !grepl("^[0-9]+$", x)) {
  cat(USAGE, "\n")
  quit(status = 1)
}

n <- as.numeric(x)
orig <- n
rev_num <- 0

while (n > 0) {
  rev_num <- rev_num * 10 + (n %% 10)
  n <- n %/% 10
}

cat(tolower(orig == rev_num), "\n")
```

{% endraw %}

Palindromic Number in [R](https://sampleprograms.io/languages/r) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).