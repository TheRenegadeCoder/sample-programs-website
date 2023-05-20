---
title: Factorial in R
layout: default
date: 2020-10-19
featured-image: factorial-in-every-language.jpg
last-modified: 2020-10-19

---

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [R](https://sampleprograms.io/languages/r) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```r
args<-commandArgs(TRUE)
if(length(args) > 0){
  a = args[1]
  # Check if String or numeral only, ..
  numbers_only <- function(a) !grepl("\\D", a)
  if(numbers_only(a) == TRUE){
  if(a == 0){
    cat("1")
  }else if (a > 0){
  fact = 1
  for(i in 1:a){
    fact = fact * i
  }
  cat(fact)
  # else a < 0
    } else{
      cat("Usage: please input a non-negative integer")
          }
  #  Negative Input
  }else{
    cat("Usage: please input a non-negative integer")
     }
# Empty Command Line Param
}else{
    cat("Usage: please input a non-negative integer")
     }
```

{% endraw %}

[Factorial](https://sampleprograms.io/projects/factorial) in [R](https://sampleprograms.io/languages/r) was written by:

- Veena ManikPrabhu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).