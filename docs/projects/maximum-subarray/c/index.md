---
authors:
- Maximillian Naza
date: 2025-01-19
featured-image: maximum-subarray-in-every-language.jpg
last-modified: 2025-01-19
layout: default
tags:
- c
- maximum-subarray
title: Maximum Subarray in C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-subarray/c/how-to-implement-the-solution.md
- sources/programs/maximum-subarray/c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

void print_usage() {
    printf("Usage: Please provide a list of integers in the format: \"1, 2, 3, 4, 5\"\n");
}

int max_subarray_sum(int* arr, int n) {
    int max_so_far = INT_MIN;
    int max_ending_here = 0;

    for (int i = 0; i < n; i++) {
        max_ending_here += arr[i];

        if (max_so_far < max_ending_here) {
            max_so_far = max_ending_here;
        }

        if (max_ending_here < 0) {
            max_ending_here = 0;
        }
    }

    return max_so_far;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        print_usage();
        return 1;
    }

    // Check if input is empty
    if (strlen(argv[1]) == 0) {
        print_usage();
        return 1;
    }

    // Parse input string
    char* token;
    int arr[100]; // Assuming a maximum of 100 integers
    int count = 0;

    token = strtok(argv[1], ",");
    while (token != NULL) {
        arr[count++] = atoi(token);
        token = strtok(NULL, ",");
    }

    // If less than two integers were provided
    if (count == 1) {
        printf("%d\n", arr[0]);
        return 0;
    } else if (count < 2) {
        print_usage();
        return 1;
    }

    // Calculate maximum subarray sum
    int result = max_subarray_sum(arr, count);

    printf("%d\n", result);

    return 0;
}

```

{% endraw %}

Maximum Subarray in [C](https://sampleprograms.io/languages/c) was written by:

- Maximillian Naza

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).