---
authors:
- Vipin Yadav
date: 2024-10-08
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2024-10-08
layout: default
tags:
- go
- remove-all-whitespace
title: Remove All Whitespace in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/go/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	errorMessage := "Usage: please provide a string"

	if len(os.Args) < 2 || os.Args[1] == "" {
		fmt.Println(errorMessage)
		os.Exit(1)
	}

	inputString := os.Args[1]
	outputString := strings.Join(strings.Fields(inputString), "")
	fmt.Println(outputString)
}

```

{% endraw %}

Remove All Whitespace in [Go](https://sampleprograms.io/languages/go) was written by:

- Vipin Yadav

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).