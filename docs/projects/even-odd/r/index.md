---
title: Even Odd in R
layout: default
date: 2021-10-22
featured-image: even-odd-in-every-language.jpg
last-modified: 2021-10-22

---

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [R](https://sampleprograms.io/languages/r) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```r
args<-commandArgs(TRUE)
number = args[1]

if (length(args) < 1 || !suppressWarnings(!is.na(as.numeric(number)))) {
  cat("Usage: please input a number")
}else {
  number = as.numeric(number)
  if (number %% 2 == 0) {
    cat("Even")
  }else {
    cat("Odd")
  }
}
```

{% endraw %}

[Even Odd](https://sampleprograms.io/projects/even-odd) in [R](https://sampleprograms.io/languages/r) was written by:

- Grooble

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).