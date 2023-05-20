---
title: Fibonacci in Rust
layout: default
date: 2018-10-05
featured-image: fibonacci-in-every-language.jpg
last-modified: 2018-10-05

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
use std::env::args;
use std::process::exit;
use std::str::FromStr;

const LIMIT: i32 = 93;

fn usage() -> ! {
    println!("Usage: please input the count of fibonacci numbers to output");
    exit(0);
}

fn parse_int<T: FromStr>(s: &str) -> Result<T, <T as FromStr>::Err> {
    s.trim().parse::<T>()
}

fn fibonacci(terms: i32) {
    if terms > LIMIT {
        println!("The number of terms you want to calculate is too big!");
        println!("The limit is {}.", LIMIT);
    } else {
        let mut a = 0u64;
        let mut b = 1u64;
        for i in 1..(terms + 1) {
            (a, b) = (b, a + b);
            println!("{i}: {a}");
        }
    }
}

fn main() {
    let mut args = args().skip(1);

    // Exit if 1st command-line argument not an integer
    let mut input_num: i32 = args
        .next()
        .and_then(|s| parse_int(&s).ok())
        .unwrap_or_else(|| usage());

    // Show request number of Fibonacci numbers
    fibonacci(input_num);
}
```

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Noah Nichols
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 08 2023 19:53:07. The solution was first committed on Oct 05 2018 09:33:10. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).