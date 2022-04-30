---

title: Factorial in R
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Factorial in R page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```R
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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).