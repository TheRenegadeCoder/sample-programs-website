---

title: Fibonacci in Rust
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Fibonacci in Rust page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
const LIMIT: u64 = 93;

fn fibonacci(terms: u64) {
    if terms > LIMIT {
        println!("The number of terms you want to calculate is too big!");
        println!("The limit is {}.", LIMIT);
    } else {
        println!("\n");
        let mut i = 0u64;
        let mut a = 0u64;
        let mut b = 1u64;
        let mut c = 0u64;
        while i < terms {
            println!("{}", c);

            c = a + b;
            b = a;
            a = c;
            
            i += 1;
        }
    }
}

fn main() {
    let mut terms = String::new();
    let mut terms_n: u64 = 0;

    if std::io::stdin().read_line(&mut terms).is_err() {
        println!("Could not read from keyboard!");
    } else {
        terms.pop();
        terms_n = terms.parse().unwrap();
    }

    fibonacci(terms_n);
}
```

{% endraw %}

Fibonacci in Rust was written by:

- Noah Nichols

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 05 2018 10:31:35. The solution was first committed on Oct 05 2018 09:33:10. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).