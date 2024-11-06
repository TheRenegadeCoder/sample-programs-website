---
authors:
- qopci
date: 2024-11-06
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2024-11-06
layout: default
tags:
- c
- remove-all-whitespace
title: Remove All Whitespace in C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/c/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, char *argv[]) {
    // check whether the passed argument is a string or empty
    if (argc < 2 || argv[1][0] == '\0') {
        printf("Usage: please provide a string\n");
        return 1; 
    }

    char *input = argv[1]; 
    char output[1000];  
    int j = 0; 

    for (int i = 0; input[i] != '\0'; i++) {
        // check if current character is not a whitespace character
        if (!isspace(input[i])) {
            output[j++] = input[i];
        }
    }

    // null terminator to mark the end of a string
    output[j] = '\0';

    // print the output string with no spaces
    printf("%s\n", output);

    return 0;
}

```

{% endraw %}

Remove All Whitespace in [C](https://sampleprograms.io/languages/c) was written by:

- qopci

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).