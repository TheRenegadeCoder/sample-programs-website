---
authors:
- Parker Johansen
date: 2019-03-17
featured-image: quine-in-every-language.jpg
last-modified: 2019-03-17
layout: default
tags:
- go
- quine
title: Quine in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quine/go/how-to-implement-the-solution.md
- sources/programs/quine/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quine](https://sampleprograms.io/projects/quine) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import "fmt"

func main() {
	a := "package main\n\nimport \"fmt\"\n\nfunc main() {\n\ta := %q\n\tfmt.Printf(a, a)\n}\n"
	fmt.Printf(a, a)
}

```

{% endraw %}

Quine in [Go](https://sampleprograms.io/languages/go) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).