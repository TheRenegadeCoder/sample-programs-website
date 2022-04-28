---

---

Welcome to the Fibonacci in Rust page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```Rust
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.