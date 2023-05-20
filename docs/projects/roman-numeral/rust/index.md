---
title: Roman Numeral in Rust
layout: default
date: 2018-10-12
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2018-10-12

---

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        println!("Usage: please provide a string of roman numerals");
    } else {
        let value: i64 = convert_roman_numeral(&args[1]);
        if value < 0 {
            println!("Error: invalid string of roman numerals");
        } else {
            println!("{value}");
        }
    }
}

fn convert_char(c: char) -> i64 {
    if c == 'I' {
        return 1;
    } else if c == 'V' {
        return 5;
    } else if c == 'X' {
        return 10;
    } else if c == 'L' {
        return 50;
    } else if c == 'C' {
        return 100;
    } else if c == 'D' {
        return 500;
    } else if c == 'M' {
        return 1000;
    } else {
        return -1;
    }
}

fn convert_roman_numeral(s: &String) -> i64 {
    let mut number: i64 = 0;
    let mut prev_value: i64 = 0;
    for c in s.as_bytes() {
        let value = convert_char(*c as char);
        if value < 0 {
            number = value;
            break;
        }
        number += value;
        if prev_value > 0 && value > prev_value {
            number -= 2*prev_value;
            prev_value = 0;
        } else {
            prev_value = value;
        }
    }

    number
}
```

{% endraw %}

[Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Noah Nichols
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Apr 04 2023 17:31:25. The solution was first committed on Oct 12 2018 18:00:40. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).