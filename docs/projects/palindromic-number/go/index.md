---
authors:
- Vipin Yadav
date: 2024-10-08
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2024-10-08
layout: default
tags:
- go
- palindromic-number
title: Palindromic Number in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/go/how-to-implement-the-solution.md
- sources/programs/palindromic-number/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
	"fmt"
	"os"
	"strconv"
)

func palindromicNumber(x int) {
	if x >= 0 {
		reversedNumber := 0
		noOfDigits := 0
		temp := x

		for temp > 0 {
			noOfDigits++
			reversedNumber = (reversedNumber * 10) + (temp % 10)
			temp /= 10
		}

		if x == reversedNumber {
			fmt.Println("true")
		} else {
			fmt.Println("false")
		}
	} else {
		fmt.Println("Usage: please input a non-negative integer")
	}
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: please input a non-negative integer")
		os.Exit(1)
	}

	x, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Println("Usage: please input a non-negative integer")
		os.Exit(1)
	}

	palindromicNumber(x)
}

```

{% endraw %}

Palindromic Number in [Go](https://sampleprograms.io/languages/go) was written by:

- Vipin Yadav

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).