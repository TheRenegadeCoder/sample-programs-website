---
title: Reverse String in R
layout: default
date: 2020-10-19
featured-image: reverse-string-in-every-language.jpg
last-modified: 2020-10-19

---

Welcome to the [R](https://sampleprograms.io/languages/r)everse String in [R](https://sampleprograms.io/languages/r) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

[R](https://sampleprograms.io/languages/r)everse String in [R](https://sampleprograms.io/languages/r) was written by:

- Veena ManikPrabhu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).