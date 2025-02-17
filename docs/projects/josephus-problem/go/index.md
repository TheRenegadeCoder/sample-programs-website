---
authors:
- Zia
date: 2025-02-17
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2025-02-17
layout: default
tags:
- go
- josephus-problem
title: Josephus Problem in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/josephus-problem/go/how-to-implement-the-solution.md
- sources/programs/josephus-problem/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
	"os"
	"strconv"
)

func die() {
	println("Usage: please input the total number of people and number of people to skip.")
	os.Exit(1)
}

func josephus(n, k int) int {
	if n == 1 {
		return 1
	}

	return (josephus(n-1, k)+k-1)%n + 1
}

func main() {
	if len(os.Args) != 3 {
		die()
	}

	n, err := strconv.Atoi(os.Args[1])
	if err != nil {
		die()
	}

	k, err := strconv.Atoi(os.Args[2])
	if err != nil {
		die()
	}

	println(josephus(n, k))
}

```

{% endraw %}

Josephus Problem in [Go](https://sampleprograms.io/languages/go) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).