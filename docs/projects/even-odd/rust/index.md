---
title: Even Odd in Rust
layout: default
date: 2022-04-28
last-modified: 2023-04-07
---

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
// Requirement is in https://sample-programs.therenegadecoder.com/projects/even-odd/
// Program to accept an integer on the command line and outputs if the integer is Even or Odd.

use std::env::args;
use std::process::exit;
use std::num::ParseIntError;

fn usage() -> ! {
    println!("Usage: please input a number");
    exit(0);
}

fn parse_int(s: String) -> Result<i32, ParseIntError> {
    s.trim().parse::<i32>()
}

fn main() {
    // Exit if 1st command-line argument not an integer
    let mut input_value: Result<i32, ParseIntError> = parse_int(
        args().nth(1).unwrap_or_else(|| usage())
    );
    if input_value.is_err() {
        usage();
    }

    let input_num: i32 = input_value.unwrap();

    // Even numbers are divisible by 2
    if input_num % 2 == 0 {
        println!("Even");
    }
    // Odd numbers are not divisible by 2
    else {
        println!("Odd");
    }
}
```

{% endraw %}

[Even Odd](https://sampleprograms.io/projects/even-odd) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Mallikarjuna S J
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Apr 04 2023 17:31:25. The solution was first committed on Oct 31 2019 16:49:58. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).