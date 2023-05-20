---
title: Prime Number in Rust
layout: default
date: 2019-10-31
featured-image: prime-number-in-every-language.jpg
last-modified: 2019-10-31

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

    // Exit if 1st command-line argument not an positive integer
    let input_num: u128 = args
        .next()
        .and_then(|s| parse_int(&s).ok())
        .unwrap_or_else(|| usage());

    if input_num < 2 || (input_num != 2 && input_num % 2 == 0) {
        println!("Composite");
        exit(0);
    }

    let mut n = 3u128;
    while n * n <= input_num {
        if input_num % n == 0 {
            println!("Composite");
            exit(0);
        }
        n += 2;
    }
    println!("Prime");
}
```

{% endraw %}

[Prime Number](https://sampleprograms.io/projects/prime-number) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Mallikarjuna S J
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 08 2023 19:53:07. The solution was first committed on Oct 31 2019 18:11:28. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).