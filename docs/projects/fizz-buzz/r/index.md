---
authors:
- Gabi Herman
- Jeremy Grifski
date: 2019-10-24
featured-image: fizz-buzz-in-every-language.png
last-modified: 2020-10-18
layout: default
tags:
- fizz-buzz
- r
title: Fizz Buzz in R
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/r/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/r/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [R](https://sampleprograms.io/languages/r) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```r
fizz_buzz <- function(){
  for (x in 1:100){
    out<-''
    mod3<- x%%3==0
    mod5 <- x%%5==0
    if (!mod3 && !mod5){
      out=x
    }
    if (mod3){
      out='Fizz'
    }
    if (mod5){
      out=paste0(out,'Buzz')
    }
    cat(out, "\n")
  }
}

fizz_buzz()

```

{% endraw %}

Fizz Buzz in [R](https://sampleprograms.io/languages/r) was written by:

- Gabi Herman
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).