---
authors:
- Jeremy Grifski
- Parker Johansen
date: 2018-09-17
featured-image: baklava-in-every-language.jpg
last-modified: 2019-04-01
layout: default
tags:
- baklava
- go
title: Baklava in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/go/how-to-implement-the-solution.md
- sources/programs/baklava/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	for i := 0; i < 10; i++ {
		fmt.Println(strings.Repeat(" ", (10-i)) + strings.Repeat("*", (i*2+1)))
	}

	for i := 10; -1 < i; i-- {
		fmt.Println(strings.Repeat(" ", (10-i)) + strings.Repeat("*", (i*2+1)))
	}
}

```

{% endraw %}

Baklava in [Go](https://sampleprograms.io/languages/go) was written by:

- Jeremy Grifski
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).