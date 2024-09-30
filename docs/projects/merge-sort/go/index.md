---
authors:
- Parker Johansen
date: 2019-03-17
featured-image: merge-sort-in-every-language.jpg
last-modified: 2019-03-25
layout: default
tags:
- go
- merge-sort
title: Merge Sort in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/merge-sort/go/how-to-implement-the-solution.md
- sources/programs/merge-sort/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Merge Sort](https://sampleprograms.io/projects/merge-sort) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

func mergeSort(list []int) []int {
	var doMergeSort func(lst [][]int) [][]int
	doMergeSort = func(lst [][]int) [][]int {
		if len(lst) <= 0 {
			return [][]int{}
		}
		if len(lst) == 1 {
			return lst
		}
		return doMergeSort(append([][]int{merge(lst[0], lst[1])}, doMergeSort(lst[2:])...))
	}
	return doMergeSort(split(list))[0]
}

func split(list []int) (splitList [][]int) {
	for _, i := range list {
		splitList = append(splitList, []int{i})
	}
	return
}

func merge(list1 []int, list2 []int) []int {
	if len(list1) <= 0 {
		return list2
	}
	if len(list2) <= 0 {
		return list1
	}
	if list1[0] < list2[0] {
		return append(list1[:1], merge(list1[1:], list2)...)
	}
	return append(list2[:1], merge(list1, list2[1:])...)
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
	nums = mergeSort(nums)
	fmt.Println(sliceIntToString(nums))
}

```

{% endraw %}

Merge Sort in [Go](https://sampleprograms.io/languages/go) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).