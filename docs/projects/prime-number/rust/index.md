---

title: Prime Number in Rust
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Prime Number in Rust page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```Rust
//  Requirement     https://sample-programs.therenegadecoder.com/projects/prime-number/
// Accept a number on command line and print if it is Composite or Prime 
// Works till  39 digits, ...

use std::process;
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

    let mut n = 3 as u128;
    let divisor = input_num /2 as u128;

    if input_num % 2 == 0 {
        println!("Composite");
        process::exit(1);
    }    
    while n < divisor {  
        if input_num % n == 0 {
        println!("Composite");
        process::exit(1);        
        }
        n = n + 2;
    }
    if n >= divisor {
    println!("Prime");
    }
}
```

{% endraw %}

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).