---
title: Prime Number in R
layout: default
date: 2020-10-19
featured-image: prime-number-in-every-language.jpg
last-modified: 2020-10-19

---

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [R](https://sampleprograms.io/languages/r) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```r
# Program to check if the input number is prime or not
args<-commandArgs(TRUE)
if(length(args) > 0){
  a1 = args[1]
  # Check Numeral only, ..
  numbers_only <- function(a) !grepl("\\D", a1)
  if(numbers_only(a1) == TRUE){
    if (a1 >= 0){
      a = as.integer(a1)
    if(a == 2){
      cat("Prime")
      # If 0, or 1 or Even Number
    }else if (a == 0 || a == 1 || a %% 2 == 0 ) {
      cat("Composite")
    }else{
      flag = 1
      r = a %/% 2
      for(i in 2:r) {
        if (a %% i == 0) {
           flag = 0
          break
          }
       }
       if(flag == 1) {
         cat("Prime")
        } else {
          cat("Composite")
        }
    }
  }else{# Empty Input
  cat("Usage: please input a non-negative integer")
}
}else{  # Negative Input
  cat("Usage: please input a non-negative integer")
}
}else{    # Empty Input
  cat("Usage: please input a non-negative integer")
}
```

{% endraw %}

[Prime Number](https://sampleprograms.io/projects/prime-number) in [R](https://sampleprograms.io/languages/r) was written by:

- Veena ManikPrabhu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).