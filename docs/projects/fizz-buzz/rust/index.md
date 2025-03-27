---
authors:
- "Bodo Sch\xF6nfeld"
- Jeremy Grifski
- Noah Nichols
- Vincent Caron
date: 2018-09-24
featured-image: fizz-buzz-in-every-language.png
last-modified: 2022-04-28
layout: default
tags:
- fizz-buzz
- rust
title: Fizz Buzz in Rust
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/rust/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/rust/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
fn main() {
    for number in 1..101 {
        if number % 3 == 0 && number % 5 == 0 {
            println!("FizzBuzz");
        } else if number % 3 == 0 {
            println!("Fizz");
        } else if number % 5 == 0 {
            println!("Buzz");
        } else {
            println!("{}", number);
        }
    }
}

```

{% endraw %}

Fizz Buzz in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Noah Nichols
- Vincent Caron

This article was written by:

- Bodo Schönfeld
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

Before we dig into the code too much, let's take a look at the rules:

* If a number is divisible by 3, print the word 'Fizz' instead of the number.
* If the number is divisible by 5, print the word 'Buzz' instead of the number.
* Finally, if the number is divisible by both 3 and 5, print 'FizzBuzz' instead of the number.
* Otherwise, just print the number.

You can test for divisibility using the modulo operator `%`. The modulo operator divides two numbers and yields the remainder, so `i` modulo `j` is `0` if `i` is divisible by `j`. In Rust, this is written as `i % j`. Then, it's a simple matter of checking whether `i % 3 == 0` or `i % 5 == 0`.

### The Loop

In the very first line, we'll notice a `for`-loop:

```rust
for number in 1..101
```

Here, we loop through all the numbers from 1 to 100.

### Control Flow

From there, we begin our testing using an if statement:

```rust
if number % 3 == 0 && number % 5 == 0 {
    println!("FizzBuzz");
} else if number % 3 == 0 {
    println!("Fizz");
} else if number % 5 == 0 {
    println!("Buzz");
} else {
    println!("{}", number);
}
```

* If the number is divisible by 3 and 5, we print the word 'FizzBuzz'.
* If the number is divisible by 3, we print the word 'Fizz'.
* If the number is divisible by 5, we print the word 'Buzz'.
* In all other cases, we print the number itself.


## How to Run the Solution

To run FizzBuzz in Rust, install the latest version of Rust. After that, create a project structure using `cargo`:

```console
cargo new fizz-buzz
```

Copy the code from Github into 'main.rs'. Compile and run the code from the command line using

```console
cargo run main.rs
```

This will create a new 'target' directory containing the executable binary file.
