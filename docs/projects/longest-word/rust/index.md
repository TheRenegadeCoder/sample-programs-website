---
title: Longest Word in Rust
layout: default
date: 2022-04-28
last-modified: 2023-04-15
---

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
use std::env::args;
use std::process::exit;

fn usage() -> ! {
    println!("Usage: please provide a string");
    exit(0);
}

fn get_longest_word_len(s: String) -> usize {
    s.trim()
        .split_whitespace()
        .map(|t| t.len())
        .max()
        .unwrap()
}

fn main() {
    // Exit if 1st command-line argument is empty
    let s: String = args()
        .nth(1)
        .unwrap_or_else(|| "".to_string());
    if s.len() < 1 {
        usage();
    }

    // Get longest word length and display it
    println!("{}", get_longest_word_len(s));
}
```

{% endraw %}

[Longest Word](https://sampleprograms.io/projects/longest-word) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).