---
authors:
- Softizo
date: 2019-10-09
featured-image: rot13-in-every-language.jpg
last-modified: 2019-10-09
layout: default
tags:
- c
- rot13
title: Rot13 in C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/c/how-to-implement-the-solution.md
- sources/programs/rot13/c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

void rot13(char *str) {
    for(int i = 0; str[i] != '\0'; i++) {
        char c = *(str + i);
        if(('a' <= c && 'n' > c) || ('A' <= c && 'N' > c)) {
            *(str + i) += 13;
        } else if(('n' <= c && 'z' >= c) || ('N' <= c && 'Z' >= c)) {
            *(str + i) -= 13;
        }
    }
}

int main(int argc, char *argv[]) {
    if(argc == 2 && strlen(argv[1]) != 0 && !isdigit(*argv[1])) {
        rot13(argv[1]);
        printf("%s\n", argv[1]);
    } else {
        printf("Usage: please provide a string to encrypt\n");
    }
    
    return 0;
}

```

{% endraw %}

Rot13 in [C](https://sampleprograms.io/languages/c) was written by:

- Softizo

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).