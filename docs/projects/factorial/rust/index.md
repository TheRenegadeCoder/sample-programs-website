---
authors:
- Mallikarjuna S J
- rzuckerm
date: 2019-10-31
featured-image: factorial-in-every-language.jpg
last-modified: 2023-05-08
layout: default
tags:
- factorial
- rust
title: Factorial in Rust
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/rust/how-to-implement-the-solution.md
- sources/programs/factorial/rust/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
//  Requirement     https://sample-programs.therenegadecoder.com/projects/factorial/
// Accept a number on command line and print it's factorial
// Works till factorial 34, which is 39 digits, ...
use std::env::args;
use std::process::exit;
use std::str::FromStr;

fn usage() -> ! {
    println!("Usage: please input a non-negative integer");
    exit(0);
}

fn parse_int<T: FromStr>(s: &str) -> Result<T, <T as FromStr>::Err> {
    s.trim().parse::<T>()
}

fn main() {
    let mut args = args().skip(1);

    // confirm positive integer is passed as command-line argument
    let mut input_num: u32 = args
        .next()
        .and_then(|s| parse_int(&s).ok())
        .unwrap_or_else(|| usage());

    let mut n = input_num as u128;
    let mut result = 1;
    while n > 0 {
        result *= n;
        n -= 1;
    }
    println!("{result}");
}

```

{% endraw %}

Factorial in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Mallikarjuna S J
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).