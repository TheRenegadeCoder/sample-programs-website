---

title: Reverse String in R
layout: default
date: 2022-04-28
last-modified: 2022-04-28

---

Welcome to the Reverse String in R page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```R
args<- commandArgs(TRUE)
if(length(args) > 0 ){
  if (args[1] != ""){
    splits <- strsplit(args, "")[[1]]
    reversed <- rev(splits)
    reversed <-as.character(rev(splits))
    j <- paste(reversed, collapse = '')
    cat(noquote(j))
  }
}

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.