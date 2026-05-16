---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: minimum-spanning-tree-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- go
- minimum-spanning-tree
title: Minimum Spanning Tree in Go
title1: Minimum Spanning
title2: Tree in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/minimum-spanning-tree/go/how-to-implement-the-solution.md
- sources/programs/minimum-spanning-tree/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Minimum Spanning Tree](https://sampleprograms.io/projects/minimum-spanning-tree) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

const usage = `Usage: please provide a comma-separated list of integers`

func main() {
	if len(os.Args) != 2 {
		printUsage()
	}

	matrix, errM := parseList(os.Args[1])

	if errM != nil {
		printUsage()
	}

	nFloat := math.Sqrt(float64(len(matrix)))
	n := int(nFloat)
	if nFloat != float64(n) || n == 0 {
		printUsage()
	}

	cost, ok := primMST(matrix, n)
	if !ok {
		printUsage()
	}

	fmt.Println(cost)
}

func primMST(matrix []int, n int) (int, bool) {
	if n == 0 {
		return 0, true
	}

	inMST := make([]bool, n)
	minWeights := make([]int, n)
	for i := range minWeights {
		minWeights[i] = math.MaxInt32
	}

	minWeights[0] = 0
	totalWeight := 0
	nodesInTree := 0

	for i := 0; i < n; i++ {
		u := -1
		minVal := math.MaxInt32

		for v := 0; v < n; v++ {
			if !inMST[v] && minWeights[v] < minVal {
				minVal = minWeights[v]
				u = v
			}
		}

		if u == -1 {
			break
		}

		inMST[u] = true
		totalWeight += minVal
		nodesInTree++

		for v := 0; v < n; v++ {
			weight := matrix[u*n+v]
			if weight > 0 && !inMST[v] && weight < minWeights[v] {
				minWeights[v] = weight
			}
		}
	}

	if nodesInTree != n {
		return 0, false
	}

	return totalWeight, true
}

func parseList(input string) ([]int, error) {
	if strings.TrimSpace(input) == "" {
		return nil, fmt.Errorf("empty input")
	}

	parts := strings.Split(input, ",")
	nums := make([]int, 0, len(parts))
	for _, p := range parts {
		val, err := strconv.Atoi(strings.TrimSpace(p))
		if err != nil {
			return nil, err
		}
		nums = append(nums, val)
	}
	return nums, nil
}

func printUsage() {
	fmt.Println(usage)
	os.Exit(1)
}
```

{% endraw %}

Minimum Spanning Tree in [Go](https://sampleprograms.io/languages/go) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).