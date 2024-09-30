---
authors:
- rzuckerm
date: 2023-04-09
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2023-05-08
layout: default
tags:
- remove-all-whitespace
- rust
title: Remove All Whitespace in Rust
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/rust/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/rust/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
use std::env::args;
use std::process::exit;

fn usage() -> ! {
    println!("Usage: please provide a string");
    exit(0);
}
fn remove_all_whitespaces(s: String) -> String {
    s.chars().filter(|c| !c.is_whitespace()).collect()
}

fn main() {
    let mut args = args().skip(1);

    // Get first command-line argument
    let s: String = args
        .next()
        .unwrap_or_else(|| usage());

    // Make sure not empty
    if s.len() < 1 {
        usage();
    }

    // Remove all whitespace and show results
    let t: String = remove_all_whitespaces(s);
    println!("{t}");
}

```

{% endraw %}

Remove All Whitespace in [Rust](https://sampleprograms.io/languages/rust) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).