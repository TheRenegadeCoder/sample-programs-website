---
authors:
- Maximillian Naza
date: 2025-01-21
featured-image: transpose-matrix-in-every-language.jpg
last-modified: 2025-01-21
layout: default
tags:
- c
- transpose-matrix
title: Transpose Matrix in C
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/transpose-matrix/c/how-to-implement-the-solution.md
- sources/programs/transpose-matrix/c/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Transpose Matrix](https://sampleprograms.io/projects/transpose-matrix) in [C](https://sampleprograms.io/languages/c) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_MATRIX_SIZE 100

void transpose_matrix(int *matrix, int rows, int cols, int *transposed) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            transposed[j * rows + i] = matrix[i * cols + j];
        }
    }
}

int main(int argc, char *argv[]) {
    if (argc != 4) {
        printf("Usage: please enter the dimension of the matrix and the serialized matrix\n");
        return 1;
    }

    int cols = atoi(argv[1]);
    int rows = atoi(argv[2]);
    char *input = argv[3];

    if (cols <= 0 || rows <= 0 || strlen(input) == 0) {
        printf("Usage: please enter the dimension of the matrix and the serialized matrix\n");
        return 1;
    }

    int matrix[MAX_MATRIX_SIZE];
    int transposed[MAX_MATRIX_SIZE];
    int count = 0;
    char *token = strtok(input, ", ");

    while (token != NULL && count < rows * cols) {
        matrix[count++] = atoi(token);
        token = strtok(NULL, ", ");
    }

    if (count != rows * cols) {
        printf("Usage: please enter the dimension of the matrix and the serialized matrix\n");
        return 1;
    }

    transpose_matrix(matrix, rows, cols, transposed);

    for (int i = 0; i < cols * rows; i++) {
        printf("%d", transposed[i]);
        if (i < cols * rows - 1) {
            printf(", ");
        }
    }
    printf("\n");

    return 0;
}

```

{% endraw %}

Transpose Matrix in [C](https://sampleprograms.io/languages/c) was written by:

- Maximillian Naza

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).