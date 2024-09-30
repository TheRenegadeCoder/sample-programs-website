---
authors:
- rzuckerm
date: 2023-04-06
featured-image: selection-sort-in-every-language.jpg
last-modified: 2023-05-08
layout: default
tags:
- rust
- selection-sort
title: Selection Sort in Rust
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/selection-sort/rust/how-to-implement-the-solution.md
- sources/programs/selection-sort/rust/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Selection Sort](https://sampleprograms.io/projects/selection-sort) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
use std::env::args;
use std::process::exit;
use std::str::FromStr;

fn usage() -> ! {
    println!("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"");
    exit(0);
}

fn parse_int<T: FromStr>(s: &str) -> Result<T, <T as FromStr>::Err> {
    s.trim().parse::<T>()
}

fn parse_int_list<T: FromStr>(s: &str) -> Result<Vec<T>, <T as FromStr>::Err> {
    s.split(',')
        .map(parse_int)
        .collect::<Result<Vec<T>, <T as FromStr>::Err>>()
}

fn selection_sort<T: PartialOrd>(arr: &mut Vec<T>) {
    // Source: https://en.wikipedia.org/wiki/Selection_sort#Implementations
    for i in 0..(arr.len() - 1) {
        let mut min_pos = i;
        for j in (i + 1)..arr.len() {
            if arr[j] < arr[min_pos] {
                min_pos = j;
            }
        }

        if min_pos != i {
            arr.swap(min_pos, i);
        }
    }
}

fn main() {
    let mut args = args().skip(1);

    // Convert 1st command-line argument to list of integers
    let mut arr: Vec<i32> = args
        .next()
        .and_then(|s| parse_int_list(&s).ok())
        .unwrap_or_else(|| usage());

    // Exit if list too small
    if arr.len() < 2 {
        usage();
    }

    selection_sort::<i32>(&mut arr);
    println!("{arr:?}");
}

```

{% endraw %}

Selection Sort in [Rust](https://sampleprograms.io/languages/rust) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).