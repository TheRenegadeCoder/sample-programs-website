---
authors:
- Jessica Hebert
date: 2025-10-31
featured-image: maximum-subarray-in-every-language.jpg
last-modified: 2025-10-31
layout: default
tags:
- go
- maximum-subarray
title: Maximum Subarray in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-subarray/go/how-to-implement-the-solution.md
- sources/programs/maximum-subarray/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	if len(os.Args) < 2 || strings.TrimSpace(os.Args[1]) == "" {
		fmt.Println(`Usage: Please provide a list of integers in the format: "1, 2, 3, 4, 5"`)
		return
	}
	input := strings.Join(os.Args[1:], "")
	parts := strings.Split(input, ",")
	nums := make([]int, len(parts))

	for i, p := range parts {
		p = strings.TrimSpace(p)
		n, _ := strconv.Atoi(p)
		nums[i] = n

	}

	maxSum := nums[0]
	blockSum := nums[0]

	for i := 1; i < len(nums); i++ {
		blockSum = max(nums[i], blockSum+nums[i])
		if maxSum < blockSum {
			maxSum = blockSum

		}

	}
	fmt.Println(maxSum)

}

```

{% endraw %}

Maximum Subarray in [Go](https://sampleprograms.io/languages/go) was written by:

- Jessica Hebert

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).