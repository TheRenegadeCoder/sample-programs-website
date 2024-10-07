---
authors:
- Vipin Yadav
date: 2024-10-08
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2024-10-08
layout: default
tags:
- duplicate-character-counter
- go
title: Duplicate Character Counter in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/go/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
	"fmt"
	"os"
)

func errorMessage() {
	fmt.Println("Usage: please provide a string")
}

func main() {
	if len(os.Args) <= 1 {
		errorMessage()
		return
	}

	inputStr := os.Args[1]

	if len(inputStr) == 0 {
		errorMessage()
		return
	}
	charCount := make(map[rune]int)
	for _, c := range inputStr {
		charCount[c]++
	}
	duplicateFound := false
	for _, c := range inputStr {
		if count, exists := charCount[c]; exists && count > 1 {
			if !duplicateFound {
				duplicateFound = true
			}
			fmt.Printf("%c: %d\n", c, count)
			charCount[c] = 0
		}
	}

	if !duplicateFound {
		fmt.Println("No duplicate characters")
	}
}

```

{% endraw %}

Duplicate Character Counter in [Go](https://sampleprograms.io/languages/go) was written by:

- Vipin Yadav

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).