---

---

Welcome to the Factorial in Rust page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Rust
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.