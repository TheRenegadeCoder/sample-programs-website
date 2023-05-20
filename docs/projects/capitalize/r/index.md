---
title: Capitalize in R
layout: default
date: 2020-10-19
featured-image: capitalize-in-every-language.jpg
last-modified: 2020-10-19

---

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [R](https://sampleprograms.io/languages/r) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```r
args<-commandArgs(TRUE)
if(length(args) > 0){
  if (args[1] != ""){
    len = length(args)
    array_string <- strsplit(args[1], "")[[1]]
    for (i in 1:len){
        if (i == 1){
          array_string[i] <- toupper(substr(array_string[i], 1, 1))
        }
        #Convert to Character Vector.... else prints with spaces in between 
        a = as.character(array_string)
        cat(a,fill = FALSE, sep = "")
    }
  }else{
    cat("Usage: please provide a string")
  }
}else{
    cat("Usage: please provide a string")
}
```

{% endraw %}

[Capitalize](https://sampleprograms.io/projects/capitalize) in [R](https://sampleprograms.io/languages/r) was written by:

- Veena ManikPrabhu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).