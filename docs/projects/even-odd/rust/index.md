---
authors:
- Mallikarjuna S J
- rzuckerm
date: 2019-10-31
featured-image: even-odd-in-every-language.jpg
last-modified: 2023-05-08
layout: default
tags:
- even-odd
- rust
title: Even Odd in Rust
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/rust/how-to-implement-the-solution.md
- sources/programs/even-odd/rust/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
// Requirement is in https://sample-programs.therenegadecoder.com/projects/even-odd/
// Program to accept an integer on the command line and outputs if the integer is Even or Odd.

use std::env::args;
use std::process::exit;
use std::str::FromStr;

fn usage() -> ! {
    println!("Usage: please input a number");
    exit(0);
}

fn parse_int<T: FromStr>(s: &str) -> Result<T, <T as FromStr>::Err> {
    s.trim().parse::<T>()
}

fn main() {
    let mut args = args().skip(1);

    // Exit if 1st command-line argument not an integer
    let mut input_num: i32 = args
        .next()
        .and_then(|s| parse_int(&s).ok())
        .unwrap_or_else(|| usage());

    // Even if divisible by 2, Odd otherwise
    match input_num % 2 == 0 {
        true => println!("Even"),
        false => println!("Odd"),
    }
}

```

{% endraw %}

Even Odd in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Mallikarjuna S J
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).