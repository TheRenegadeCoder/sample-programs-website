---

title: Even Odd in Rust
layout: default
date: 2022-04-28
last-modified: 2022-04-30

---

Welcome to the Even Odd in Rust page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```rust
// Requirement is in https://sample-programs.therenegadecoder.com/projects/even-odd/
// Program to accept an integer on the command line and outputs if the integer is Even or Odd.

fn main() {
    //confirm integer is passed as commandline argument
    let mut input_value = std::env::args().nth(1).expect("Kindly pass an integer as Command line Argument");
    // Trim the trailing newline
    input_value = input_value.trim_end().to_string();
    //Convert String to Int
    let input_num: i32 = input_value
        .trim()
        .parse()
        .expect("Kindly enter an integer");
    // Even numbers are divisible by 2
    if input_num % 2 == 0 {
        println!("Even");
    }
    // Odd numbers are not divisible by 2
    else {
    	println!("Odd");
    }    
}
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).