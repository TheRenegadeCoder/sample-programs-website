---
authors:
- rzuckerm
date: 2023-04-09
featured-image: longest-word-in-every-language.jpg
last-modified: 2023-05-08
layout: default
tags:
- longest-word
- rust
title: Longest Word in Rust
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/rust/how-to-implement-the-solution.md
- sources/programs/longest-word/rust/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

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

fn get_longest_word_len(s: &str) -> usize {
    s.trim()
        .split_whitespace()
        .map(|t| t.len())
        .max()
        .unwrap()
}

fn main() {
    let mut args = args().skip(1);

    // Exit if 1st command-line argument is empty
    let s: &str = &args
        .next()
        .unwrap_or_else(|| usage());
    if s.len() < 1 {
        usage();
    }

    // Get longest word length and display it
    println!("{}", get_longest_word_len(s));
}

```

{% endraw %}

Longest Word in [Rust](https://sampleprograms.io/languages/rust) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).