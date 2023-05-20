---
title: Fizz Buzz in R
layout: default
date: 2019-10-24
featured-image: fizz-buzz-in-every-language.png
last-modified: 2019-10-24

---

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

[Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [R](https://sampleprograms.io/languages/r) was written by:

- Gabi Herman
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 18 2020 17:59:43. The solution was first committed on Oct 24 2019 16:13:46. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).