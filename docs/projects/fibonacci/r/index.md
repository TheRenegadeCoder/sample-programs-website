---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-06
featured-image: fibonacci-in-every-language.jpg
last-modified: 2026-05-06
layout: default
tags:
- fibonacci
- r
title: Fibonacci in R
title1: Fibonacci
title2: in R
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/r/how-to-implement-the-solution.md
- sources/programs/fibonacci/r/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [R](https://sampleprograms.io/languages/r) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```r
USAGE <- "Usage: please input the count of fibonacci numbers to output"
args <- commandArgs(trailingOnly = TRUE)

if (length(args) != 1 || nchar(args[1]) == 0) {
  cat(USAGE, "\n")
  quit(status = 1)
}

n <- suppressWarnings(as.numeric(args[1]))

if (is.na(n) || n %% 1 != 0) {
  cat(USAGE, "\n")
  quit(status = 1)
}

if (n <= 0) {
  quit(status = 0)
}

fib <- numeric(n)
fib[1] <- 1

if (n >= 2) {
  fib[2] <- 1
}

if (n >= 3) {
  for (i in 3:n) {
    fib[i] <- fib[i - 1] + fib[i - 2]
  }
}

indices <- 1:n
output <- paste0(indices, ": ", fib, collapse = "\n")
cat(output, "\n")
```

{% endraw %}

Fibonacci in [R](https://sampleprograms.io/languages/r) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).