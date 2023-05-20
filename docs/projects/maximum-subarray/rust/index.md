---
title: Maximum Subarray in Rust
layout: default
date: 2023-04-09
featured-image: maximum-subarray-in-every-language.jpg
last-modified: 2023-04-09

---

Welcome to the [Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
use std::env::args;
use std::process::exit;
use std::str::FromStr;
use std::cmp::max;

fn usage() -> ! {
    println!("Usage: Please provide a list of integers in the format: \"1, 2, 3, 4, 5\"");
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

// Find maximum subarray using Kadane's algorithm.
// Source: https://en.wikipedia.org/wiki/Maximum_subarray_problem#No_empty_subarrays_admitted
fn maximum_subarray(arr: &Vec<i32>) -> i32 {
    let mut best_sum: i32 = i32::MIN;
    let mut current_sum: i32 = 0;
    for value in arr {
        current_sum = value + max(0, current_sum);
        best_sum = max(current_sum, best_sum);
    }

    best_sum
}

fn main() {
    let mut args = args().skip(1);

    // Convert 1st command-line argument to list of integers
    let mut arr: Vec<i32> = args
        .next()
        .and_then(|s| parse_int_list(&s).ok())
        .unwrap_or_else(|| usage());

    // Get maximum subarray and display
    println!("{}", maximum_subarray(&arr));
}
```

{% endraw %}

[Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 08 2023 19:53:07. The solution was first committed on Apr 09 2023 10:53:37. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).