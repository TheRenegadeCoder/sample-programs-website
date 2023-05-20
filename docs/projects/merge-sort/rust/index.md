---
title: Merge Sort in Rust
layout: default
date: 2020-10-03
featured-image: merge-sort-in-every-language.jpg
last-modified: 2020-10-03

---

Welcome to the [Merge Sort](https://sampleprograms.io/projects/merge-sort) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

fn merge<T: PartialOrd + Copy>(lhs: &Vec<T>, rhs: &Vec<T>, merged_arr: &mut Vec<T>) {
    let mut lhs_idx = 0;
    let mut rhs_idx = 0;
    let mut merged_idx = 0;

    while lhs_idx < lhs.len() && rhs_idx < rhs.len() {
        if lhs[lhs_idx] < rhs[rhs_idx] {
            merged_arr[merged_idx] = lhs[lhs_idx];
            lhs_idx += 1;
        } else {
            merged_arr[merged_idx] = rhs[rhs_idx];
            rhs_idx += 1;
        }

        merged_idx += 1;
    }

    if lhs_idx < lhs.len() {
        merged_arr[merged_idx..].copy_from_slice(&lhs[lhs_idx..]);
    }
    else if rhs_idx < rhs.len() {
        merged_arr[merged_idx..].copy_from_slice(&rhs[rhs_idx..]);
    }
}

fn merge_sort<T: PartialOrd + Copy>(arr: &mut Vec<T>) {
    if arr.len() <= 1 {
        return;
    }

    let mid = arr.len() / 2;
    let mut lhs = arr[..mid].to_vec();
    let mut rhs = arr[mid..].to_vec();

    merge_sort(&mut lhs);
    merge_sort(&mut rhs);

    merge(&lhs, &rhs, arr);
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

    merge_sort::<i32>(&mut arr);
    println!("{arr:?}");
}
```

{% endraw %}

[Merge Sort](https://sampleprograms.io/projects/merge-sort) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Andrew Johnson
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 08 2023 19:53:07. The solution was first committed on Oct 03 2020 19:42:59. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).