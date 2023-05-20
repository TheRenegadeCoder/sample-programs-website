---
title: Longest Palindromic Substring in Rust
layout: default
date: 2023-04-17
featured-image: longest-palindromic-substring-in-every-language.jpg
last-modified: 2023-04-17

---

Welcome to the [Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
use std::env::args;
use std::process::exit;

fn usage() -> ! {
    println!("Usage: please provide a string that contains at least one palindrome");
    exit(0);
}

type Matrix<T> = Vec<Vec<T>>;

// Find longest palindromic string using matching array
// Source: https://www.geeksforgeeks.org/longest-palindromic-substring-using-dynamic-programming/
fn longest_palindromic_substring(s: &str) -> String {
    // Initialize array indicating whether there is a character match
    // between two characters to indicate that nothing matches
    let n = s.len();
    let mut matches: Matrix<bool> = vec![vec![false; n]; n];

    // Indicate all length 1 strings match
    for i in 0..n {
        matches[i][i] = true;
    }

    // Convert string to a lowercase vector of characters
    let chars: Vec<char> = s
        .to_lowercase()
        .chars()
        .collect();

    // Find all length 2 matches
    let mut start = 0;
    let mut max_len = 1;
    for i in 0..(n - 1) {
        if chars[i] == chars[i + 1] {
            matches[i][i + 1] = true;
            start = i;
            max_len = 2;
        }
    }

    // Find all length 3 or higher matches
    for len in 3..=n {
        // Loop through each starting character
        for i in 0..(n - len + 1) {
            // If match for one character in from start and end characters
            // and start and end characters match, set match for start and
            // end characters, and update max length
            let j = i + len - 1;
            if matches[i + 1][j - 1] && chars[i] == chars[j] {
                matches[i][j] = true;
                if len > max_len {
                    start = i;
                    max_len = len;
                }
            }
        }
    }

    chars[start..start + max_len]
        .iter()
        .collect()
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

    // Get longest palindromic substring. Error if none found
    let longest = longest_palindromic_substring(s);
    if longest.len() < 2 {
        usage();
    }

    // Show longest palindromic substring
    println!("{longest}");
}
```

{% endraw %}

[Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 08 2023 19:53:07. The solution was first committed on Apr 17 2023 20:17:59. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).