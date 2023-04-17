---
title: Prime Number in Rust
layout: default
date: 2022-04-28
last-modified: 2023-04-17
---

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
//  Requirement     https://sample-programs.therenegadecoder.com/projects/prime-number/
// Accept a number on command line and print if it is Composite or Prime 
// Works till  39 digits, ...

use std::env::args;
use std::process::exit;
use std::num::ParseIntError;

fn usage() -> ! {
    println!("Usage: please input a non-negative integer");
    exit(0);
}

fn parse_int(s: String) -> Result<i128, ParseIntError> {
    s.trim().parse::<i128>()
}

fn main() {
    // Exit if 1st command-line argument not an integer
    let mut input_num: i128 = parse_int(
        args().nth(1).unwrap_or_else(|| usage())
    ).unwrap_or_else(|_| usage());

    // Exit if negative integer
    if input_num < 0 {
        usage();
    }

    let mut n = 3 as u128;
    let value = input_num as u128;

    if value < 2 || (value != 2 && value % 2 == 0) {
        println!("Composite");
        exit(0);
    }
    while n * n <= value {
        if value % n == 0 {
            println!("Composite");
            exit(0);
        }
        n = n + 2;
    }
    println!("Prime");
}
```

{% endraw %}

[Prime Number](https://sampleprograms.io/projects/prime-number) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Mallikarjuna S J
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Apr 07 2023 23:48:08. The solution was first committed on Oct 31 2019 18:11:28. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).