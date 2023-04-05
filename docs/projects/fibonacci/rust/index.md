---

title: Fibonacci in Rust
layout: default
date: 2022-04-28
last-modified: 2023-04-05

---

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
use std::env::args;
use std::process::exit;
use std::num::ParseIntError;

const LIMIT: i32 = 93;

fn usage() -> ! {
    println!("Usage: please input the count of fibonacci numbers to output");
    exit(0);
}

fn parse_int(s: String) -> Result<i32, ParseIntError> {
    s.trim().parse::<i32>()
}

fn fibonacci(terms: i32) {
    if terms > LIMIT {
        println!("The number of terms you want to calculate is too big!");
        println!("The limit is {}.", LIMIT);
    } else {
        let mut a = 0u64;
        let mut b = 1u64;
        let mut c = 0u64;
        for i in 1..(terms + 1) {
            c = a + b;
            b = a;
            a = c;

            println!("{i}: {c}");
        }
    }
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

    // Show request number of Fibonacci numbers
    fibonacci(input_num);
}
```

{% endraw %}

[Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Noah Nichols
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Apr 04 2023 17:31:25. The solution was first committed on Oct 05 2018 09:33:10. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).