---
authors:
- Zia
date: 2025-01-19
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-01-19
layout: default
tags:
- ballerina
- fizz-buzz
title: Fizz Buzz in Ballerina
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/ballerina/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/ballerina/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Ballerina](https://sampleprograms.io/languages/ballerina) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```ballerina
import ballerina/io;

public function main() {
	foreach int i in int:range(1, 101, 1) {
		if i % 15 == 0 {
			io:println("FizzBuzz");
		} else if i % 5 == 0 {
			io:println("Buzz");
		} else if i % 3 == 0 {
			io:println("Fizz");
		} else {
			io:println(i);
		}
	}
}

```

{% endraw %}

Fizz Buzz in [Ballerina](https://sampleprograms.io/languages/ballerina) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).