---
authors:
- Zia
date: 2025-01-19
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-01-19
layout: default
tags:
- fizz-buzz
- gravity
title: Fizz Buzz in Gravity
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/gravity/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/gravity/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Gravity](https://sampleprograms.io/languages/gravity) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```gravity
func main() {
	for (var i in 1...100) {
		if (i % 15 == 0) {
			System.print("FizzBuzz")
		} else if (i % 5 == 0) {
			System.print("Buzz")
		} else if (i % 3 == 0) {
			System.print("Fizz")
		} else {
			System.print(i)
		}
	}
}

```

{% endraw %}

Fizz Buzz in [Gravity](https://sampleprograms.io/languages/gravity) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).