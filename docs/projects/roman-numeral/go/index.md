---
authors:
- clarkimusmax
- Parker Johansen
date: 2018-10-25
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2019-04-01
layout: default
tags:
- go
- roman-numeral
title: Roman Numeral in Go
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/roman-numeral/go/how-to-implement-the-solution.md
- sources/programs/roman-numeral/go/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Go](https://sampleprograms.io/languages/go) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```go
package main

import "fmt"
import "os"

func exitWithError(msg string) {
	fmt.Println(msg)
	os.Exit(1)
}

func toRoman(input string) (total int) {
	var i = 0
	var temp1 int
	var temp2 int

	var numerals = map[string]int{
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}

	//While i is within bounds of input
	for i < len(input) {
		//Get the current value
		temp1 = numerals[string(input[i])]
		if temp1 == 0 {
			exitWithError("Error: invalid string of roman numerals")
		}

		//If we still have input left to compare, check if we need to
		//	subtract from the next value
		if len(input) > i+1 {
			//Get the next value
			temp2 = numerals[string(input[i+1])]
			if temp2 == 0 {
				exitWithError("Error: invalid string of roman numerals")
			}

			//If the current value is >= next, use it's mapped value
			if temp1 >= temp2 {
				total += temp1
				i++
				//Otherwise, adjust for the subtraction and skip next
			} else {
				total += temp2 - temp1
				i += 2
			}
			//Otherwise, just add the current value to the total
		} else {
			total += temp1
			i++
		}
	}
	return
}

func main() {
	//Args or die
	if len(os.Args) != 2 {
		exitWithError("Usage: please provide a string of roman numerals")
	}

	roman := toRoman(os.Args[1])
	fmt.Printf("%d\n", roman)
}

```

{% endraw %}

Roman Numeral in [Go](https://sampleprograms.io/languages/go) was written by:

- clarkimusmax
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).