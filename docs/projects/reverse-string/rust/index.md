---
title: Reverse String in Rust
layout: default
date: 2018-07-04
featured-image: reverse-string-in-every-language.jpg
last-modified: 2018-07-04

---

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
use std::env;

fn main() {
    let mut strings: Vec<String> = env::args().collect();
    strings.remove(0); //Removes path to executable from argument vector.
    for string in &strings {
        println!("{}", string.chars().rev().collect::<String>());
    }
}
```

{% endraw %}

[Reverse String](https://sampleprograms.io/projects/reverse-string) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Sebastian Veitleder

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).