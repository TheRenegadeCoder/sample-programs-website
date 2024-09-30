---
authors:
- rzuckerm
date: 2023-04-06
featured-image: baklava-in-every-language.jpg
last-modified: 2023-04-06
layout: default
tags:
- baklava
- rust
title: Baklava in Rust
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/rust/how-to-implement-the-solution.md
- sources/programs/baklava/rust/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
fn main() {
    for i in -10i32..11i32 {
        let num_spaces: usize = i.abs() as usize;
        println!("{}{}", " ".repeat(num_spaces), "*".repeat(21 - 2 * num_spaces));
    }
}

```

{% endraw %}

Baklava in [Rust](https://sampleprograms.io/languages/rust) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).