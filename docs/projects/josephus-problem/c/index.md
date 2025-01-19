---
authors:
- Maximillian Naza
date: 2025-01-19
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2025-01-19
layout: default
tags:
- c
- josephus-problem
title: Josephus Problem in C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/josephus-problem/c/how-to-implement-the-solution.md
- sources/programs/josephus-problem/c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include <stdio.h>
#include <stdlib.h>

int josephus(int n, int k) {
    if (n == 1)
        return 1;
    else
        return (josephus(n - 1, k) + k - 1) % n + 1;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: please input the total number of people and number of people to skip.\n");
        return 1;
    }

    char *endptr;
    int n = strtol(argv[1], &endptr, 10);
    if (*endptr != '\0' || n <= 0) {
        printf("Usage: please input the total number of people and number of people to skip.\n");
        return 1;
    }

    int k = strtol(argv[2], &endptr, 10);
    if (*endptr != '\0' || k <= 0) {
        printf("Usage: please input the total number of people and number of people to skip.\n");
        return 1;
    }

    int result = josephus(n, k);
    printf("%d\n", result);

    return 0;
}

```

{% endraw %}

Josephus Problem in [C](https://sampleprograms.io/languages/c) was written by:

- Maximillian Naza

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).