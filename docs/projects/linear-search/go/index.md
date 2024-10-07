---
authors:
- Vipin Yadav
date: 2024-10-08
featured-image: linear-search-in-every-language.jpg
last-modified: 2024-10-08
layout: default
tags:
- go
- linear-search
title: Linear Search in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/go/how-to-implement-the-solution.md
- sources/programs/linear-search/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

func linearSearch(list []int, keyToSearch int) bool {
	for _, number := range list {
		if number == keyToSearch {
			return true
		}
	}
	return false
}

func main() {
	if len(os.Args) < 3 {
		fmt.Println("Usage: please provide a list of integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")")
		return
	}

	numberString := os.Args[1]
	keyToSearchStr := os.Args[2]
	keyToSearch, err := strconv.Atoi(keyToSearchStr)
	if err != nil {
		fmt.Println("Usage: please provide a valid integer to find.")
		return
	}
	numberArray := strings.Split(numberString, ",")
	var listOfNumbers []int

	for _, numStr := range numberArray {
		numStr = strings.TrimSpace(numStr)
		number, err := strconv.Atoi(numStr)
		if err == nil {
			listOfNumbers = append(listOfNumbers, number)
		}
	}
	if len(listOfNumbers) > 0 {
		searched := linearSearch(listOfNumbers, keyToSearch)
		fmt.Println(searched)
	} else {
		fmt.Println("Usage: please provide a list of integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")")
	}
}

```

{% endraw %}

Linear Search in [Go](https://sampleprograms.io/languages/go) was written by:

- Vipin Yadav

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).