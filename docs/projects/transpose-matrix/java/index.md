---
authors:
- Apurva Vats
date: 2025-10-31
featured-image: transpose-matrix-in-every-language.jpg
last-modified: 2025-10-31
layout: default
tags:
- java
- transpose-matrix
title: Transpose Matrix in Java
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/transpose-matrix/java/how-to-implement-the-solution.md
- sources/programs/transpose-matrix/java/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Transpose Matrix](https://sampleprograms.io/projects/transpose-matrix) in [Java](https://sampleprograms.io/languages/java) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```java
import java.util.*;

public class TransposeMatrix {
    private static final int MAX_MATRIX_SIZE = 100;
    private static final String USAGE_MSG = "Usage: please enter the dimension of the matrix and the serialized matrix";

    public static void transposeMatrix(int[] matrix, int rows, int cols, int[] transposed) {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                transposed[j * rows + i] = matrix[i * cols + j];
            }
        }
    }

    public static void main(String[] args) {
        if (args.length != 3) {
            System.out.println(USAGE_MSG);
            return;
        }

        int cols, rows;
        String input = args[2];

        try {
            cols = Integer.parseInt(args[0]);
            rows = Integer.parseInt(args[1]);
        } catch (Exception e) {
            System.out.println(USAGE_MSG);
            return;
        }

        if (cols <= 0 || rows <= 0 || input.isEmpty()) {
            System.out.println(USAGE_MSG);
            return;
        }

        int[] matrix = new int[MAX_MATRIX_SIZE];
        int[] transposed = new int[MAX_MATRIX_SIZE];
        int count = 0;

        String[] tokens = input.split(",");
        for (String token : tokens) {
            if (count >= rows * cols) break;

            token = token.trim();
            try {
                matrix[count++] = Integer.parseInt(token);
            } catch (Exception e) {
                System.out.println(USAGE_MSG);
                return;
            }
        }

        if (count != rows * cols) {
            System.out.println(USAGE_MSG);
            return;
        }

        transposeMatrix(matrix, rows, cols, transposed);

        for (int i = 0; i < cols * rows; i++) {
            System.out.print(transposed[i]);
            if (i < cols * rows - 1) {
                System.out.print(", ");
            }
        }
        System.out.println();
    }
}

```

{% endraw %}

Transpose Matrix in [Java](https://sampleprograms.io/languages/java) was written by:

- Apurva Vats

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).