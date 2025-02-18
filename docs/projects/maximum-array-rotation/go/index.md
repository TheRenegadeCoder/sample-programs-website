---
authors:
- dangrabo
date: 2025-02-18
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2025-02-18
layout: default
tags:
- go
- maximum-array-rotation
title: Maximum Array Rotation in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-array-rotation/go/how-to-implement-the-solution.md
- sources/programs/maximum-array-rotation/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
	"fmt"
	"os"
	"unicode"
)

func main() {
	if len(os.Args) != 2 {
		printError()
	} else {
		if len(createSlice()) == 0 {
			printError()
		} else {
			fmt.Println(getMaxWeightedSum(createSlice()))
		}
	}
}

func createSlice() (slice []int) {
	stringSlice := os.Args[1]
	for _, char := range stringSlice {
		if unicode.IsDigit(char) {
			slice = append(slice, int(char)-'0')
		}
	}
	return
}

func getWeightedSum(slice []int) (sum int) {
	for i, num := range slice {
		sum += i * num
	}
	return
}

func getMaxWeightedSum(slice []int) (max int) {
	max = 0
	for i := 0; i < len(slice); i++ {
		if getWeightedSum(slice) > max {
			max = getWeightedSum(slice)
		}
		slice = rotateSlice(slice)
	}
	return
}

func rotateSlice(slice []int) (rotatedSlice []int) {
	first := slice[0]
	slice = slice[1:]
	slice = append(slice, first)
	rotatedSlice = slice
	return
}

func printError() {
	fmt.Println("Usage: please provide a list of integers (e.g. \"8, 3, 1, 2\")")
}

```

{% endraw %}

Maximum Array Rotation in [Go](https://sampleprograms.io/languages/go) was written by:

- dangrabo

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).