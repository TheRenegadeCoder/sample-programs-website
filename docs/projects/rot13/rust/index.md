---
title: Rot13 in Rust
layout: default
date: 2019-07-15
featured-image: rot13-in-every-language.jpg
last-modified: 2019-07-15

---

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
use std::env;

fn rot13(input: String) -> String {
    let mut output = String::new();
    
    for character in input.chars() {
        let offset;

        if character.is_ascii_lowercase() {
            offset = 'a' as u8;
        }
        else if character.is_ascii_uppercase() {
            offset = 'A' as u8;
        }
        else {
            output.push(character);
            continue;
        }
    
        let mut rotated = character as u8;
        rotated -= offset;
        rotated += 13;
        rotated %= 26;
        rotated += offset;
        
        output.push(rotated as char);
    }
    
    return output;
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if (args.len() == 1) {
        println!("Usage: please provide a string to encrypt");
        return;
    }
    
    let input = args[1].to_string();
    if (input.is_empty()) {
        println!("Usage: please provide a string to encrypt");
        return;
    }
    
    let output = rot13(input);
    println!("{}", output);
}
```

{% endraw %}

[Rot13](https://sampleprograms.io/projects/rot13) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Jeremy Grifski
- Vincent Caron

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 16 2022 11:56:20. The solution was first committed on Jul 15 2019 10:49:39. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).