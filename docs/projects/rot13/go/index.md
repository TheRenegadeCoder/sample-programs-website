---
authors:
- Parker Johansen
date: 2019-03-17
featured-image: rot13-in-every-language.jpg
last-modified: 2019-04-06
layout: default
tags:
- go
- rot13
title: Rot13 in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/go/how-to-implement-the-solution.md
- sources/programs/rot13/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
	"fmt"
	"os"
	"strings"
)

func rot13(str string) string {
	return strings.Map(encryptRune, str)
}

func encryptRune(r rune) rune {
	if r >= 65 && r <= 90 {
		return (((r - 65) + 13) % 26) + 65
	} else if r >= 97 && r <= 122 {
		return (((r - 97) + 13) % 26) + 97
	} else {
		return r
	}
}

func exitWithError() {
	fmt.Println("Usage: please provide a string to encrypt")
	os.Exit(1)
}

func main() {
	if len(os.Args) != 2 {
		exitWithError()
	}

	if len(os.Args[1]) <= 0 {
	    exitWithError()
	}

	fmt.Println(rot13(os.Args[1]))
}

```

{% endraw %}

Rot13 in [Go](https://sampleprograms.io/languages/go) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).