---
authors:
- Zia
date: 2024-12-15
featured-image: even-odd-in-every-language.jpg
last-modified: 2024-12-15
layout: default
tags:
- even-odd
- v
title: Even Odd in V
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/v/how-to-implement-the-solution.md
- sources/programs/even-odd/v/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [V](https://sampleprograms.io/languages/v) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```v
module main

import os
import strconv

fn main() {
	if os.args.len < 2 {
		println('Usage: please input a number')
		exit(1)
	}

	num := strconv.atoi(os.args[1]) or {
		println('Usage: please input a number')
		exit(1)
	}

	print(match num % 2 {
		0 { 'Even' }
		1, -1 { 'Odd' }
		else { 'Usage: please input a number' }
	})
}

```

{% endraw %}

Even Odd in [V](https://sampleprograms.io/languages/v) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).