---
title: Fibonacci in Objective C
layout: default
date: 2020-10-01
featured-image: fibonacci-in-every-language.jpg
last-modified: 2020-10-01

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Objective C](https://sampleprograms.io/languages/objective-c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```objective_c
#include <stdio.h>

int fibonacci(int n)
{
    return ( n<=2 ? 1 : fibonacci(n-1) + fibonacci(n-2) );
}

int main(void)
{
    int n;
    for (n=1; n<=16; n++)
        printf("%d, ", fibonacci(n));
    printf("...\n");
    return 0;
}
```

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Objective C](https://sampleprograms.io/languages/objective-c) was written by:

- Renato

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).