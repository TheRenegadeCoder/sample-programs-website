---
authors:
- Jeremy Grifski
- Nathaniel Niosco
date: 2019-10-09
featured-image: capitalize-in-every-language.jpg
last-modified: 2019-10-26
layout: default
tags:
- capitalize
- go
title: Capitalize in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/go/how-to-implement-the-solution.md
- sources/programs/capitalize/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
	"fmt"
	"os"
	"strings"
)

func exitWithError() {
	fmt.Println("Usage: please provide a string")
	os.Exit(1)
}

func uppercaseFirst(str string) string {
	s := string(str[0])
	u := strings.ToUpper(s)
	up := u + str[1:]
	return up
}

func main() {
	if len(os.Args) != 2 || len(os.Args[1]) == 0 {
		exitWithError()
	}

	s := os.Args[1]
	up := uppercaseFirst(s)

	fmt.Println(up)
}

```

{% endraw %}

Capitalize in [Go](https://sampleprograms.io/languages/go) was written by:

- Jeremy Grifski
- Nathaniel Niosco

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).