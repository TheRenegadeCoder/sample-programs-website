---
authors:
- Azeb-S
date: 2025-10-30
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2025-10-30
layout: default
tags:
- duplicate-character-counter
- v
title: Duplicate Character Counter in V
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/v/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/v/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [V](https://sampleprograms.io/languages/v) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```v
import os

fn show_error() {
	println('Usage: please provide a string')
}

fn main() {
	args := os.args[1..] // skip program name
	if args.len == 0 {
		show_error()
		return
	}
	input_str := args[0]
	if input_str.len == 0 {
		show_error()
		return
	}

	mut counts := map[rune]int{}
	for c in input_str.runes() {
		counts[c]++
	}

	mut found := false
	for c in input_str.runes() {
		if counts[c] > 1 {
			println('${c.str()}: ${counts[c]}')
			counts[c] = 0 // prevent duplicate printing
			found = true
		}
	}

	if !found {
		println('No duplicate characters')
	}
}

```

{% endraw %}

Duplicate Character Counter in [V](https://sampleprograms.io/languages/v) was written by:

- Azeb-S

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).