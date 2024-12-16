---
authors:
- Zia
date: 2024-12-16
featured-image: factorial-in-every-language.jpg
last-modified: 2024-12-16
layout: default
tags:
- factorial
- v
title: Factorial in V
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/v/how-to-implement-the-solution.md
- sources/programs/factorial/v/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [V](https://sampleprograms.io/languages/v) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```v
module main

import os
import strconv

fn factorial(n u64) u64 {
	return match true {
		n <= 1 { 1 }
		else { n * factorial(n-1) }
	}
}

fn usage() {
	println("Usage: please input a non-negative integer")
	exit(1)
}

fn main() {
	if os.args.len != 2 {
		usage()
	}

	n := strconv.atoi(os.args[1]) or {
		usage()
		exit(1)
	}
	if n < 0 {
		usage()
	}
	println(factorial(u64(n)))
}

```

{% endraw %}

Factorial in [V](https://sampleprograms.io/languages/v) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).