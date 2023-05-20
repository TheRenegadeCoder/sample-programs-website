---
title: Duplicate Character Counter in C
layout: default
date: 2022-10-03
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2022-10-03

---

Welcome to the Duplicate [C](https://sampleprograms.io/languages/c)haracter [C](https://sampleprograms.io/languages/c)ounter in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include <stdio.h>
#include <string.h>
#include<stdlib.h>

// Function to handle errors
int handle_error()
{
    printf("Usage: please provide a string\n");
    exit(0);
}

int main(int argc, char *argv[])
{
    /*
        Condition to check for No String as Input
    */
    if (argc !=2 )
    {
        handle_error();
    }
    /*
        Condition to check for No String as Input
    */
    if(strlen(argv[1]) == 0){
        handle_error();
    }
    int counter[256]={0};
    int len = strlen(argv[1]);
    for(int i=0;i<len;i++){
        counter[argv[1][i]-1]++;
    }
    int flag = 1;
    for(int i=0;i<len;i++){
        char c = argv[1][i];
        if(counter[c-1]>1){
            flag = 0;
            printf("%c: %d\n",c,counter[c-1]);
            counter[c-1]=0;
        }
    }
    if(flag == 1){
        printf("No duplicate characters\n");
    }
    return 0;
}
```

{% endraw %}

Duplicate [C](https://sampleprograms.io/languages/c)haracter [C](https://sampleprograms.io/languages/c)ounter in [C](https://sampleprograms.io/languages/c) was written by:

- Vipin Yadav

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).