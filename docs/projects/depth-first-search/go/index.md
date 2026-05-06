---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: depth-first-search-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- depth-first-search
- go
title: Depth First Search in Go
title1: Depth First
title2: Search in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/depth-first-search/go/how-to-implement-the-solution.md
- sources/programs/depth-first-search/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Depth First Search](https://sampleprograms.io/projects/depth-first-search) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

const usage = `Usage: please provide a tree in an adjacency matrix form ("0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0") together with a list of vertex values ("1, 3, 5, 2, 4") and the integer to find ("4")`

type Graph struct {
	matrix []int
	values []int
	size   int
}

func main() {
	if len(os.Args) != 4 {
		printUsage()
	}

	matrix, errM := parseList(os.Args[1])
	values, errV := parseList(os.Args[2])
	target, errT := strconv.Atoi(os.Args[3])

	if errM != nil || errV != nil || errT != nil {
		printUsage()
	}

	n := len(values)
	if len(matrix) != n*n || n == 0 {
		printUsage()
	}

	g := &Graph{
		matrix: matrix,
		values: values,
		size:   n,
	}

	visited := make([]bool, n)
	if g.DFS(0, target, visited) {
		fmt.Println("true")
	} else {
		fmt.Println("false")
	}
}

func (g *Graph) DFS(curr, target int, visited []bool) bool {
	if g.values[curr] == target {
		return true
	}

	visited[curr] = true

	for neighbor := 0; neighbor < g.size; neighbor++ {
		edgeExists := g.matrix[curr*g.size+neighbor] == 1
		if edgeExists && !visited[neighbor] {
			if g.DFS(neighbor, target, visited) {
				return true
			}
		}
	}

	return false
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

Depth First Search in [Go](https://sampleprograms.io/languages/go) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).