---
authors:
- Parker Johansen
date: 2019-02-24
featured-image: fibonacci-in-every-language.jpg
last-modified: 2019-04-07
layout: default
tags:
- fibonacci
- go
title: Fibonacci in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/go/how-to-implement-the-solution.md
- sources/programs/fibonacci/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
	"fmt"
	"os"
	"strconv"
)

func fibonacci(n int, c chan int) {
	x, y := 1, 1
	for i := 0; i < n; i++ {
		c <- x
		x, y = y, x+y
	}
	close(c)
}

func exitWithError() {
	fmt.Println("Usage: please input the count of fibonacci numbers to output")
	os.Exit(1)
}

func main() {
	if len(os.Args) != 2 {
		exitWithError()
	}

	n, err := strconv.Atoi(os.Args[1])
	if err != nil {
		exitWithError()
	}

	c := make(chan int, n)

	go fibonacci(cap(c), c)
	i := 1
	for v := range c {
		fmt.Printf("%d: %d\n", i, v)
		i++
	}
}

```

{% endraw %}

Fibonacci in [Go](https://sampleprograms.io/languages/go) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).