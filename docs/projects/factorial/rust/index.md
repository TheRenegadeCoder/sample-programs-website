---
title: Factorial in Rust
layout: default
date: 2022-04-28
last-modified: 2023-04-09
---

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
//  Requirement     https://sample-programs.therenegadecoder.com/projects/factorial/
// Accept a number on command line and print it's factorial
// Works till factorial 34, which is 39 digits, ...
use std::env::args;
use std::process::exit;
use std::num::ParseIntError;

fn usage() -> ! {
    println!("Usage: please input a non-negative integer");
    exit(0);
}

fn parse_int(s: String) -> Result<i32, ParseIntError> {
    s.trim().parse::<i32>()
}

fn main() {
    // confirm integer is passed as commandline argument
    let mut input_num: i32 = parse_int(
        args().nth(1).unwrap_or_else(|| usage())
    ).unwrap_or_else(|_| usage());

    // Make sure non-negative
    if input_num < 0 {
        usage()
    }

    let mut n = input_num as u128;
    let mut result = 1;
    while n > 0 {
        result = result * n;
        n = n - 1;
    }
    println!("{}", result );
}
```

{% endraw %}

[Factorial](https://sampleprograms.io/projects/factorial) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Mallikarjuna S J
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Apr 07 2023 23:48:08. The solution was first committed on Oct 31 2019 17:25:13. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).