---
title: Longest Word in C
layout: default
date: 2022-10-08
featured-image: longest-word-in-every-language.jpg
last-modified: 2022-10-08

---

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void error(){
    printf("Usage: please provide a string\n");
    exit(0);
}
int main(int argc, char *argv[])
{
    if(argc<2){
        error();
    }
    if(strlen(argv[1])<=0){
        error();
    }
    int max = -1;
    char* word = strtok(argv[1], " ,\n\t");
    while (word != NULL) {
        int len = strlen(word);
        if(len>max){
            max = len;
        }
        word = strtok(NULL, " ,\n\t");
    }

    printf("%d",max);
      
    
    return 0;
}
```

{% endraw %}

[Longest Word](https://sampleprograms.io/projects/longest-word) in [C](https://sampleprograms.io/languages/c) was written by:

- sachchu007

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).