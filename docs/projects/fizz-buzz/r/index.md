---

title: Fizz Buzz in R
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Fizz Buzz in R page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```R
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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).