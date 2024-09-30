---
authors:
- clarkimusmax
- Parker Johansen
date: 2018-10-25
featured-image: even-odd-in-every-language.jpg
last-modified: 2019-04-01
layout: default
tags:
- even-odd
- go
title: Even Odd in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/go/how-to-implement-the-solution.md
- sources/programs/even-odd/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
	"fmt"
	"os"
	"strconv"
)

func exitWithError() {
	fmt.Println("Usage: please input a number")
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

	if n%2 == 0 {
		fmt.Printf("Even\n")
	} else {
		fmt.Printf("Odd\n")
	}
}

```

{% endraw %}

Even Odd in [Go](https://sampleprograms.io/languages/go) was written by:

- clarkimusmax
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).