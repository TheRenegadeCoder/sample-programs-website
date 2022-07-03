---

title: Factorial in Rust
layout: default
date: 2022-04-28
last-modified: 2022-07-03

---

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
//  Requirement     https://sample-programs.therenegadecoder.com/projects/factorial/
// Accept a number on command line and print it's factorial
// Works till factorial 34, which is 39 digits, ...
fn main() {
    //confirm integer is passed as commandline argument
    let mut input_value = std::env::args().nth(1).expect("please input a non-negative integer");
    // Trim the trailing newline
    input_value = input_value.trim_end().to_string();
    //String to Int

    let input_num: u128 = input_value
        .trim()
        .parse()
        .expect("please input a non-negative integer");
    let mut n = input_num as u128;
    let mut result = 1;
    while n > 0 {
        result = result * n;
        n = n - 1;
    }
    println!("{}", result );
}
```

{% endraw %}

[Factorial](https://sampleprograms.io/projects/factorial) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Mallikarjuna S J

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).