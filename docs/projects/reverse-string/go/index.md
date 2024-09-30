---
authors:
- Parker Johansen
- Riddhi K
date: 2018-10-15
featured-image: reverse-string-in-every-language.jpg
last-modified: 2019-04-01
layout: default
tags:
- go
- reverse-string
title: Reverse String in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/go/how-to-implement-the-solution.md
- sources/programs/reverse-string/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import "fmt"
import "os"

//Function to reverse a string
func reverse_string(str string) string {
	chars := []rune(str)
	for i, j := 0, len(chars)-1; i < j; i, j = i+1, j-1 {
		chars[i], chars[j] = chars[j], chars[i]
	}
	return string(chars)
}

func main() {
	// Check the command line args length
	var argslen = len(os.Args)

	// If the length is 2, one command line arg exist
	if argslen == 2 {
		input := os.Args[1]
		fmt.Printf("%v\n", reverse_string(input))
	}
}

```

{% endraw %}

Reverse String in [Go](https://sampleprograms.io/languages/go) was written by:

- Parker Johansen
- Riddhi K

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).