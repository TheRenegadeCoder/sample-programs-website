---

title: Reverse String in Rust

---

Welcome to the Reverse String in Rust page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

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

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.