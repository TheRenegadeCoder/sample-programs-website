---

title: Even Odd in R
layout: default
date: 2022-04-28
last-modified: 2022-04-28

---

Welcome to the Even Odd in R page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```R
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.