---
authors:
- Meet Thakur
date: 2025-10-11
featured-image: transpose-matrix-in-every-language.jpg
last-modified: 2025-10-11
layout: default
tags:
- c-plus-plus
- transpose-matrix
title: Transpose Matrix in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/transpose-matrix/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/transpose-matrix/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Transpose Matrix](https://sampleprograms.io/projects/transpose-matrix) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <sstream>
#include <vector>
#include <string>

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
        std::cout << "Usage: please enter the dimension of the matrix and the serialized matrix" << std::endl;
        return 1;
    }

    int cols = std::atoi(argv[1]);
    int rows = std::atoi(argv[2]);
    std::string input = argv[3];

    if (cols <= 0 || rows <= 0 || input.empty()) {
        std::cout << "Usage: please enter the dimension of the matrix and the serialized matrix" << std::endl;
        return 1;
    }

    int matrix[MAX_MATRIX_SIZE];
    int transposed[MAX_MATRIX_SIZE];
    int count = 0;

    std::stringstream ss(input);
    std::string token;

    while (std::getline(ss, token, ',') && count < rows * cols) {
        // Trim leading spaces
        size_t start = token.find_first_not_of(" ");
        if (start != std::string::npos) {
            token = token.substr(start);
        }
        matrix[count++] = std::atoi(token.c_str());
    }

    if (count != rows * cols) {
        std::cout << "Usage: please enter the dimension of the matrix and the serialized matrix" << std::endl;
        return 1;
    }

    transpose_matrix(matrix, rows, cols, transposed);

    for (int i = 0; i < cols * rows; i++) {
        std::cout << transposed[i];
        if (i < cols * rows - 1) {
            std::cout << ", ";
        }
    }
    std::cout << std::endl;

    return 0;
}

```

{% endraw %}

Transpose Matrix in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Meet Thakur

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).