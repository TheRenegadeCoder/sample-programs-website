---
authors:
- Zia
date: 2024-12-15
featured-image: fizz-buzz-in-every-language.png
last-modified: 2024-12-15
layout: default
tags:
- fizz-buzz
- v
title: Fizz Buzz in V
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/v/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/v/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [V](https://sampleprograms.io/languages/v) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```v
module main

fn main() {
	for i in 1..101 {
		println(match true {
			i % 15 == 0 { "FizzBuzz" }
			i % 5 == 0 { "Buzz" }
			i % 3 == 0 { "Fizz" }
			else { i.str() }
		})
	}
}

```

{% endraw %}

Fizz Buzz in [V](https://sampleprograms.io/languages/v) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).