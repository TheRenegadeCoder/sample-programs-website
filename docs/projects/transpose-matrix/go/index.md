---
authors:
- Meet Thakur
date: 2024-10-11
featured-image: transpose-matrix-in-every-language.jpg
last-modified: 2024-10-11
layout: default
tags:
- go
- transpose-matrix
title: Transpose Matrix in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/transpose-matrix/go/how-to-implement-the-solution.md
- sources/programs/transpose-matrix/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Transpose Matrix](https://sampleprograms.io/projects/transpose-matrix) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	if len(os.Args) < 4 {
		fmt.Println("Usage: please enter the dimension of the matrix and the serialized matrix")
		return
	}

	cols, err1 := strconv.Atoi(os.Args[1])
	rows, err2 := strconv.Atoi(os.Args[2])
	matrixStr := os.Args[3]

	if err1 != nil || err2 != nil || cols <= 0 || rows <= 0 || matrixStr == "" {
		fmt.Println("Usage: please enter the dimension of the matrix and the serialized matrix")
		return
	}

	matrixStr = strings.ReplaceAll(matrixStr, " ", "")
	matrixElements := strings.Split(matrixStr, ",")
	if len(matrixElements) != cols*rows {
		fmt.Println("Usage: please enter the dimension of the matrix and the serialized matrix")
		return
	}

	matrix := make([][]int, rows)
	for i := range matrix {
		matrix[i] = make([]int, cols)
	}

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			num, err := strconv.Atoi(matrixElements[i*cols+j])
			if err != nil {
				fmt.Println("Usage: please enter the dimension of the matrix and the serialized matrix")
				return
			}
			matrix[i][j] = num
		}
	}

	transposed := transpose(matrix)
	printMatrix(transposed)
}

func transpose(matrix [][]int) [][]int {
	if len(matrix) == 0 {
		return [][]int{}
	}

	transposed := make([][]int, len(matrix[0]))
	for i := range transposed {
		transposed[i] = make([]int, len(matrix))
	}

	for i := range matrix {
		for j := range matrix[i] {
			transposed[j][i] = matrix[i][j]
		}
	}

	return transposed
}

func printMatrix(matrix [][]int) {
	var result []string
	for _, row := range matrix {
		for _, val := range row {
			result = append(result, strconv.Itoa(val))
		}
	}
	fmt.Println(strings.Join(result, ", "))
}
```

{% endraw %}

Transpose Matrix in [Go](https://sampleprograms.io/languages/go) was written by:

- Meet Thakur

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).