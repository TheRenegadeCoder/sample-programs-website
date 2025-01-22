---
authors:
- Maximillian Naza
date: 2025-01-21
featured-image: linear-search-in-every-language.jpg
last-modified: 2025-01-21
layout: default
tags:
- c
- linear-search
title: Linear Search in C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/c/how-to-implement-the-solution.md
- sources/programs/linear-search/c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool linear_search(int* arr, int size, int target) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) {
            return true;
        }
    }
    return false;
}

int* parse_array(char* input, int* size) {
    int* arr = NULL;
    *size = 0;
    char* token = strtok(input, ", ");
    while (token != NULL) {
        arr = realloc(arr, (*size + 1) * sizeof(int));
        arr[*size] = atoi(token);
        (*size)++;
        token = strtok(NULL, ", ");
    }
    return arr;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        printf("Usage: please provide a list of integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")\n");
        return 1;
    }

    int size;
    int* arr = parse_array(argv[1], &size);
    int target = atoi(argv[2]);

    if (size == 0) {
        printf("Usage: please provide a list of integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")\n");
        free(arr);
        return 1;
    }

    bool result = linear_search(arr, size, target);
    printf("%s\n", result ? "true" : "false");

    free(arr);
    return 0;
}

```

{% endraw %}

Linear Search in [C](https://sampleprograms.io/languages/c) was written by:

- Maximillian Naza

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).