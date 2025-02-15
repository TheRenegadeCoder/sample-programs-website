---
authors:
- Mallikarjuna S J
- rzuckerm
date: 2019-10-26
featured-image: capitalize-in-every-language.jpg
last-modified: 2023-04-04
layout: default
tags:
- capitalize
- rust
title: Capitalize in Rust
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/rust/how-to-implement-the-solution.md
- sources/programs/capitalize/rust/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
// Accept a string in command line from User and Capitalize the first letter of that string
// Rust is built to support not just ASCII, but Unicode by-default.
// Do note, each character in string is multi-byte UTF-8 supported, which needs upto 3 bytes (to accommodate Japanese letters)
// Best part of Rust compiler issues warning to remove unused variables, functions, ...
fn main() {
    //confirm string is passed as commandline argument
    let mut input_value = std::env::args().nth(1).unwrap_or_else(|| "".to_string());
    if input_value.len() < 1 {
        println!("Usage: please provide a string");
        std::process::exit(0);
    }

    // Trim the trailing newline
    input_value = input_value.trim_end().to_string();
    // convert to vector
    let mut buff: Vec<char> = input_value.chars().collect();
    // Change the 1'st letter to capital case
    buff[0] = buff[0].to_uppercase().nth(0).unwrap();
    // convert to string for printing
    let buff_hold: String = buff.into_iter().collect();
    // {} will print string without double quotes {:?} will print string with double quotes
    println!("{}", buff_hold);
}

```

{% endraw %}

Capitalize in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Mallikarjuna S J
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).