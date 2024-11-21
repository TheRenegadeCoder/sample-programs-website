---
authors:
- Tav Singh
date: 2024-11-21
featured-image: longest-word-in-every-language.jpg
last-modified: 2024-11-21
layout: default
tags:
- longest-word
- r
title: Longest Word in R
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/r/how-to-implement-the-solution.md
- sources/programs/longest-word/r/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [R](https://sampleprograms.io/languages/r) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```r
longest_word_length <- function(input_string) {
  # Checking input
  args <- commandArgs(trailingOnly = TRUE)
  
  if (length(args) == 0 || args == "") {
    cat("Usage: please provide a string\n")
  } else {
    # Split the string by whitespace and find the maximum word length in one line
    cat(max(nchar(unlist(strsplit(args[1], "[ \t\n\r]+")))), "\n")
  }
}

longest_word_length()
```

{% endraw %}

Longest Word in [R](https://sampleprograms.io/languages/r) was written by:

- Tav Singh

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).