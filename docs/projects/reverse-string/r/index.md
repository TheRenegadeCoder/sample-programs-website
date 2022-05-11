---

title: Reverse String in R
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Reverse String in R page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```r
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

Reverse String in R was written by:

- Veena ManikPrabhu

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).