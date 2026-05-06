---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-06
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2026-05-06
layout: default
tags:
- duplicate-character-counter
- r
title: Duplicate Character Counter in R
title1: Duplicate Character
title2: Counter in R
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/r/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/r/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [R](https://sampleprograms.io/languages/r) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```r
args <- commandArgs(trailingOnly = TRUE)

USAGE <- "Usage: please provide a string"

if (length(args) != 1 || !nzchar(x <- args[[1]])) {
  cat(USAGE, "\n")
  quit(status = 1)
}

chars <- strsplit(x, "")[[1]]
chars <- chars[grepl("[[:alnum:]]", chars)]

if (!length(chars)) {
  cat("No duplicate characters\n")
  quit(status = 0)
}

counts <- table(chars)

dups <- counts[counts > 1]
dups <- dups[order(match(names(dups), chars))]

if (!length(dups)) {
  cat("No duplicate characters\n")
} else {
  cat(paste(names(dups), dups, sep = ": "), sep = "\n")
}
```

{% endraw %}

Duplicate Character Counter in [R](https://sampleprograms.io/languages/r) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).