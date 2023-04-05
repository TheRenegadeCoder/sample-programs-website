---

title: Merge Sort in Rust
layout: default
date: 2022-04-28
last-modified: 2023-04-05

---

Welcome to the [Merge Sort](https://sampleprograms.io/projects/merge-sort) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

fn parse_int_list(s_list: String) -> Vec<i32> {
    let results: Vec<Result<i32, ParseIntError>> = s_list.split(",")
        .map(|s| parse_int(s.to_string()))
        .collect();
    match results.iter().any(|s| s.is_err()) {
        true => vec![],
        false => results.iter()
            .map(|result| result.clone().unwrap())
            .collect()
    }
}

fn merge(lhs: &Vec<i32>, rhs: &Vec<i32>, merged_arr: &mut Vec<i32>) {
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

fn merge_sort(arr: &mut Vec<i32>) {
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
    // Convert 1st command-line argument to list of integers
    let mut arr: Vec<i32> = parse_int_list(
        args().nth(1)
        .unwrap_or_else(|| usage())
    );

    // Exit if list too small
    if arr.len() < 2 {
        usage();
    }

    merge_sort(&mut arr);
    println!("{:?}", arr);
}
```

{% endraw %}

[Merge Sort](https://sampleprograms.io/projects/merge-sort) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Andrew Johnson
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Apr 04 2023 17:31:25. The solution was first committed on Oct 03 2020 19:42:59. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).