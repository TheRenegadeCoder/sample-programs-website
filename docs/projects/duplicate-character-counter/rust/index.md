---
authors:
- rzuckerm
date: 2023-04-09
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2023-05-08
layout: default
tags:
- duplicate-character-counter
- rust
title: Duplicate Character Counter in Rust
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/rust/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/rust/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
use std::env::args;
use std::process::exit;
use std::collections::{HashMap, HashSet};

fn usage() -> ! {
    println!("Usage: please provide a string");
    exit(0);
}

fn duplicate_character_counter(s: &str) -> HashMap<char, usize> {
    let mut counts: HashMap<char, usize> = HashMap::new();

    // Count number of occurances of each character
    for c in s.chars() {
        *counts.entry(c).or_insert(0) += 1;
    }

    counts
}

fn show_duplicate_character_counts(
    s: &str, counts: &HashMap<char, usize>
) {
    // Show characters that have duplicates and keep track of
    // which duplicate characters are found
    let mut visited: HashSet<char> = HashSet::new();
    for c in s.chars() {
        let count: usize = *counts.get(&c).unwrap();
        if count > 1 && !visited.contains(&c) {
            println!("{c}: {count}");
            visited.insert(c);
        }
    }

    // Indicate if no duplicates found
    if visited.len() < 1 {
        println!("No duplicate characters");
    }
}

fn main() {
    let mut args = args().skip(1);

    // Get 1st command-line argument. Error if empty
    let s: &str = &args
        .next()
        .unwrap_or_else(|| usage());
    if s.len() < 1 {
        usage();
    }

    // Count duplicate characters and show results
    let counts: HashMap<char, usize> = duplicate_character_counter(&s);
    show_duplicate_character_counts(&s, &counts);
}

```

{% endraw %}

Duplicate Character Counter in [Rust](https://sampleprograms.io/languages/rust) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).