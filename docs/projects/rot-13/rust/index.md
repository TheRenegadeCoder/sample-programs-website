---

title: Rot 13 in Rust
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Rot 13 in Rust page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Rust
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.