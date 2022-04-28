---

title: Fizz Buzz in Rust
layout: default
last-modified: 2021-12-11
featured-image: fizz-buzz.png
tags: [rust, fizz-buzz]
authors:
  - niftycode

---

Welcome to the Fizz Buzz in Rust page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Rust
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

## How to Implement the Solution

Let�s start by looking at the complete Fizz Buzz algorithm in Rust:

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

Before we dig into the code too much, let�s take a look at the rules:

* If a number is divisible by 3, print the word 'Fizz' instead of the number.
* If the number is divisible by 5, print the word 'Buzz' instead of the number.
* Finally, if the number is divisible by both 3 and 5, print 'FizzBuzz' instead of the number.
* Otherwise, just print the number.

You can test for divisibility using the modulo operator `%`. The modulo operator divides two numbers and yields the remainder, so `i` modulo `j` is `0` if `i` is divisible by `j`. In Rust, this is written as `i % j`. Then, it�s a simple matter of checking whether `i % 3 == 0` or `i % 5 == 0`.

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
