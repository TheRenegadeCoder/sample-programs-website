---
authors:
- rzuckerm
date: 2023-12-21
featured-image: fizz-buzz-in-every-language.png
last-modified: 2023-12-21
layout: default
tags:
- fizz-buzz
- verve
title: Fizz Buzz in Verve
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/verve/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/verve/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Verve](https://sampleprograms.io/languages/verve) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```verve
fn fizz_buzz_line(n: Int) -> String {
    match [n % 3, n % 5] {
        case [0, 0]: "FizzBuzz"
        case [0, _]: "Fizz"
        case [_, 0]: "Buzz"
        case _: to_string(n)
    }
}

fn fizz_buzz(start: Int, end: Int) {
    if not(start > end) {
        print(fizz_buzz_line(start))
        fizz_buzz(start + 1, end)
    }
}

fizz_buzz(1, 100)

```

{% endraw %}

Fizz Buzz in [Verve](https://sampleprograms.io/languages/verve) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).