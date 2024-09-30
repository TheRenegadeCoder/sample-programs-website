---
authors:
- nallovint
date: 2024-07-10
featured-image: prime-number-in-every-language.jpg
last-modified: 2024-07-10
layout: default
tags:
- odin
- prime-number
title: Prime Number in Odin
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/odin/how-to-implement-the-solution.md
- sources/programs/prime-number/odin/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Odin](https://sampleprograms.io/languages/odin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```odin
package main


import "core:fmt"
import "core:math"
import "core:os"
import "core:strconv"

is_prime :: proc(n: i64) -> bool {
	if n <= 1 {
		return false
	}
	if n == 2 {
		return true
	}
	for i in 2..=i64(math.sqrt(f32(n)) + 1) {
		if n % i == 0 {
			return false
		}
	}
	return true
}

usage :: proc() {
	fmt.eprintln("Usage: please input a non-negative integer")
}

prime_numbers :: proc(args : []string) {
    n: i64
    ok: bool
	// Get command line argument as string
	args := os.args
	if len(args) < 2 {
		usage()
		return
	}
    if n, ok = strconv.parse_i64(args[1]) ; !ok {
        usage()
		return
    }
	if n < 0  || n % 1 != 0 {
		usage()
		return
	}
	
	if is_prime(n) {
		fmt.println("prime")
	} else {
		fmt.println("composite")
	}
}

main :: proc() {
    prime_numbers(os.args)
}

```

{% endraw %}

Prime Number in [Odin](https://sampleprograms.io/languages/odin) was written by:

- nallovint

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).