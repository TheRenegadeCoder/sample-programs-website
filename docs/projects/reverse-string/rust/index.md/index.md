# Reverse String in Rust

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Rust
use std::env;

fn main() {
    let mut strings: Vec<String> = env::args().collect();
    strings.remove(0); //Removes path to executable from argument vector.
    for string in &strings {
        println!("{}", string.chars().rev().collect::<String>());
    }
}

```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.