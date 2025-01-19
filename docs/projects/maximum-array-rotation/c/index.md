---
authors:
- Maximillian Naza
date: 2025-01-19
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2025-01-19
layout: default
tags:
- c
- maximum-array-rotation
title: Maximum Array Rotation in C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-array-rotation/c/how-to-implement-the-solution.md
- sources/programs/maximum-array-rotation/c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void calculate_maximum_rotation(char *input) {
    // Parse the input string into an array of integers
    int arr[100], n = 0;
    char *token = strtok(input, ",");

    while (token != NULL) {
        arr[n++] = atoi(token);
        token = strtok(NULL, ",");
    }

    // Edge case: No input or empty input
    if (n == 0) {
        printf("Usage: please provide a list of integers (e.g. \"8, 3, 1, 2\")\n");
        return;
    }

    // Calculate initial weighted sum
    int total_sum = 0, weighted_sum = 0;

    for (int i = 0; i < n; i++) {
        weighted_sum += i * arr[i];
        total_sum += arr[i];
    }

    int max_weighted_sum = weighted_sum;

    // Calculate maximum weighted sum after rotations
    for (int i = 1; i < n; i++) {
        weighted_sum = weighted_sum + total_sum - n * arr[n - i];
        if (weighted_sum > max_weighted_sum) {
            max_weighted_sum = weighted_sum;
        }
    }

    printf("%d\n", max_weighted_sum);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: please provide a list of integers (e.g. \"8, 3, 1, 2\")\n");
        return 1;
    }

    calculate_maximum_rotation(argv[1]);
    return 0;
}

```

{% endraw %}

Maximum Array Rotation in [C](https://sampleprograms.io/languages/c) was written by:

- Maximillian Naza

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).