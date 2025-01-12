---
authors:
- Zia
date: 2025-01-12
featured-image: fraction-math-in-every-language.jpg
last-modified: 2025-01-12
layout: default
tags:
- fraction-math
- go
title: Fraction Math in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fraction-math/go/how-to-implement-the-solution.md
- sources/programs/fraction-math/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fraction Math](https://sampleprograms.io/projects/fraction-math) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
	"os"
	"math/big"
	"strings"
	"strconv"
)

func die(msg string) {
	println(msg)
	os.Exit(1)
}

func main() {
	if len(os.Args) != 4 {
		die("Usage: ./fraction-math operand1 operator operand2")
	}

	o1str := strings.Split(os.Args[1], "/")
	if len(o1str) != 2 {
		die("Invalid operand: " + os.Args[1])
	}

	o2str := strings.Split(os.Args[3], "/")
	if len(o2str) != 2 {
		die("Invalid operand: " + os.Args[3])
	}

	operator := os.Args[2]

	a, err := strconv.Atoi(o1str[0])
	if err != nil {
		die("Invalid operand: " + os.Args[1])
	}
	b, err := strconv.Atoi(o1str[1])
	if err != nil {
		die("Invalid operand: " + os.Args[1])
	}

	o1 := big.NewRat(int64(a), int64(b))

	a, err = strconv.Atoi(o2str[0])
	if err != nil {
		die("Invalid operand: " + os.Args[1])
	}
	b, err = strconv.Atoi(o2str[1])
	if err != nil {
		die("Invalid operand: " + os.Args[1])
	}

	o2 := big.NewRat(int64(a), int64(b))

	switch operator {
	case "+":
		println(o1.Add(o1, o2).RatString())
	case "-":
		println(o1.Sub(o1, o2).RatString())
	case "*":
		println(o1.Mul(o1, o2).RatString())
	case "/":
		println(o1.Mul(o1, o2.Inv(o2)).RatString())
	case ">":
		if o1.Cmp(o2) == -1 || o1.Cmp(o2) == 0 {
			println(0)
		} else if o1.Cmp(o2) == 1 {
			println(1)
		}
	case "<":
		if o1.Cmp(o2) == 1 {
			println(0)
		} else if o1.Cmp(o2) == -1 || o1.Cmp(o2) == 0 {
			println(1)
		}
	case "==":
		if o1.Cmp(o2) == 0 {
			println(1)
		} else {
			println(0)
		}
	case "!=":
		if o1.Cmp(o2) == 0 {
			println(0)
		} else {
			println(1)
		}
	case ">=":
		if o1.Cmp(o2) == 1 || o1.Cmp(o2) == 0 {
			println(1)
		} else {
			println(0)
		}
	case "<=":
		if o1.Cmp(o2) == -1 || o1.Cmp(o2) == 0 {
			println(1)
		} else {
			println(0)
		}
	}
}

```

{% endraw %}

Fraction Math in [Go](https://sampleprograms.io/languages/go) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).