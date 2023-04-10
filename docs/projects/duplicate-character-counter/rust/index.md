---
title: Duplicate Character Counter in Rust
layout: default
date: 2022-04-28
last-modified: 2023-04-10
---

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

fn duplicate_character_counter(s: &String) -> HashMap<char, usize> {
    let mut counts: HashMap<char, usize> = HashMap::new();

    // Count number of occurances of each character
    for c in s.chars() {
        *counts.entry(c).or_insert(0) += 1;
    }

    counts
}

fn show_duplicate_character_counts(
    s: &String, counts: &HashMap<char, usize>
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
    // Get 1st command-line argument. Error if empty
    let s: String = args().nth(1)
        .unwrap_or_else(|| "".to_string());
    if s.len() < 1 {
        usage();
    }

    // Count duplicate characters and show results
    let counts: &HashMap<char, usize> = &duplicate_character_counter(&s);
    show_duplicate_character_counts(&s, counts);
}
```

{% endraw %}

[Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).