---
authors:
- Parker Johansen
date: 2019-03-05
featured-image: file-input-output-in-every-language.jpg
last-modified: 2019-03-05
layout: default
tags:
- file-input-output
- go
title: File Input Output in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/go/how-to-implement-the-solution.md
- sources/programs/file-input-output/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import (
	"fmt"
	"io/ioutil"
	"log"
)

func read() (string, error) {
	contents, err := ioutil.ReadFile("output.txt")
	return string(contents), err
}

func write(contents string) error {
	return ioutil.WriteFile("output.txt", []byte(contents), 0644)
}

func main() {
	err := write("file contents")
	if err != nil {
		log.Fatal(err)
	}
	contents, err := read()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(contents)
}

```

{% endraw %}

File Input Output in [Go](https://sampleprograms.io/languages/go) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).