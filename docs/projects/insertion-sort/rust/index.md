---
title: Insertion Sort in Rust
layout: default
date: 2020-10-03
last-modified: 2020-10-03

---

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
use std::env::args;
use std::process::exit;
use std::num::ParseIntError;

fn usage() -> ! {
    println!("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"");
    exit(0);
}

fn parse_int(s: String) -> Result<i32, ParseIntError> {
    s.trim().parse::<i32>()
}

fn parse_int_list(s_list: String) -> Option<Vec<i32>> {
    let results: Vec<Result<i32, ParseIntError>> = s_list.split(",")
        .map(|s| parse_int(s.to_string()))
        .collect();
    match results.iter().any(|s| s.is_err()) {
        true => None,
        false => Some(
            results.iter()
            .map(|result| result.clone().unwrap())
            .collect()
        ),
    }
}

fn insertion_sort(arr: &mut Vec<i32>) {
    for i in 0..arr.len() {
        for j in (0..i).rev() {
            if arr[j] >= arr[j+1] {
                arr.swap(j, j+1);
            } else {
                break;
            }
        }
    }
}

fn main() {
    // Convert 1st command-line argument to list of integers
    let mut arr: Vec<i32> = parse_int_list(
        args().nth(1)
        .unwrap_or_else(|| usage())
    ).unwrap_or_else(|| usage());

    // Exit if list too small
    if arr.len() < 2 {
        usage();
    }

    insertion_sort(&mut arr);
    println!("{:?}", arr);
}
```

{% endraw %}

[Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Andrew Johnson
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Apr 07 2023 23:48:08. The solution was first committed on Oct 03 2020 19:39:06. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).