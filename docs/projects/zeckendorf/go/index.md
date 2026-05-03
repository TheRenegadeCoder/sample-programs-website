---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-24
featured-image: zeckendorf-in-every-language.png
last-modified: 2026-04-24
layout: default
tags:
- go
- zeckendorf
title: Zeckendorf in Go
title1: Zeckendorf
title2: in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/zeckendorf/go/how-to-implement-the-solution.md
- sources/programs/zeckendorf/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Zeckendorf](https://sampleprograms.io/projects/zeckendorf) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: please input a non-negative integer")
		return
	}

	n, err := strconv.Atoi(os.Args[1])
	if err != nil || n < 0 {
		fmt.Println("Usage: please input a non-negative integer")
		return
	}

	if n == 0 {
		fmt.Println("")
		return
	}

	var result []string

	for n > 0 {
		a, b := 1, 2
		prev := 1

		for b <= n {
			prev = b
			a, b = b, a+b
		}

		result = append(result, strconv.Itoa(prev))
		n -= prev
	}

	fmt.Println(strings.Join(result, ", "))
}
```

{% endraw %}

Zeckendorf in [Go](https://sampleprograms.io/languages/go) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).