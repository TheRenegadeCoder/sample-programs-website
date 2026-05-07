---
authors:
- Ștefan-Iulian Alecu
date: 2026-05-07
featured-image: dijkstra-in-every-language.jpg
last-modified: 2026-05-07
layout: default
tags:
- dijkstra
- go
title: Dijkstra in Go
title1: Dijkstra
title2: in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/dijkstra/go/how-to-implement-the-solution.md
- sources/programs/dijkstra/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Dijkstra](https://sampleprograms.io/projects/dijkstra) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

const usage = `Usage: please provide three inputs: a serialized matrix, a source node and a destination node`

func main() {
	if len(os.Args) != 4 {
		printUsage()
	}

	matrix, errM := parseList(os.Args[1])
	source, errS := strconv.Atoi(os.Args[2])
	dest, errD := strconv.Atoi(os.Args[3])

	if errM != nil || errS != nil || errD != nil {
		printUsage()
	}

	nFloat := math.Sqrt(float64(len(matrix)))
	n := int(nFloat)
	if nFloat != float64(n) || n == 0 {
		printUsage()
	}

	if source < 0 || source >= n || dest < 0 || dest >= n {
		printUsage()
	}

	for _, w := range matrix {
		if w < 0 {
			printUsage()
		}
	}

	cost, reachable := dijkstra(matrix, n, source, dest)
	if !reachable {
		printUsage()
	}

	fmt.Println(cost)
}

func dijkstra(matrix []int, n, start, end int) (int, bool) {
	dist := make([]int, n)
	visited := make([]bool, n)

	for i := range dist {
		dist[i] = math.MaxInt32
	}
	dist[start] = 0

	for i := 0; i < n; i++ {
		u := -1
		minDist := math.MaxInt32

		for v := 0; v < n; v++ {
			if !visited[v] && dist[v] < minDist {
				u = v
				minDist = dist[v]
			}
		}

		if u == -1 {
			break
		}

		visited[u] = true
		if u == end {
			return dist[u], true
		}

		for v := 0; v < n; v++ {
			weight := matrix[u*n+v]
			if weight > 0 && !visited[v] {
				newDist := dist[u] + weight
				if newDist < dist[v] {
					dist[v] = newDist
				}
			}
		}
	}

	if dist[end] == math.MaxInt32 {
		return 0, false
	}
	return dist[end], true
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

Dijkstra in [Go](https://sampleprograms.io/languages/go) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).