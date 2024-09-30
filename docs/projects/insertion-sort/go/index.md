---
authors:
- Parker Johansen
date: 2019-03-15
featured-image: insertion-sort-in-every-language.jpg
last-modified: 2019-03-25
layout: default
tags:
- go
- insertion-sort
title: Insertion Sort in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/insertion-sort/go/how-to-implement-the-solution.md
- sources/programs/insertion-sort/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
	"encoding/json"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func insertionSort(unsorted []int, sorted ...int) []int {
	if len(unsorted) <= 0 {
		return sorted
	}
	return insertionSort(unsorted[1:], insert(unsorted[0], sorted)...)
}

func insert(n int, list []int) []int {
	if len(list) <= 0 || n < list[0] {
		return append([]int{n}, list...)
	}
	return append([]int{list[0]}, insert(n, list[1:])...)
}

func strToSliceInt(strList string) []int {
	list := regexp.MustCompile(", ?").Split(strList, -1)
	if len(list) < 2 {
		exitWithError()
	}
	var nums []int
	for _, num := range list {
		n, err := strconv.Atoi(num)
		if err != nil {
			exitWithError()
		}
		nums = append(nums, n)
	}
	return nums
}

func sliceIntToString(list []int) (out string) {
	bytes, _ := json.Marshal(list)
	out = strings.Replace(string(bytes), ",", ", ", -1)
	out = strings.Trim(out, "[]")
	return
}

func exitWithError() {
	fmt.Println("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"")
	os.Exit(1)
}

func main() {
	if len(os.Args) != 2 {
		exitWithError()
	}

	nums := strToSliceInt(os.Args[1])
	nums = insertionSort(nums)
	fmt.Println(sliceIntToString(nums))
}

```

{% endraw %}

Insertion Sort in [Go](https://sampleprograms.io/languages/go) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).