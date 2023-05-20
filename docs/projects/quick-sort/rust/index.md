---
title: Quick Sort in Rust
layout: default
date: 2022-10-03
featured-image: quick-sort-in-every-language.jpg
last-modified: 2022-10-03

---

Welcome to the [Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
fn quicksort_recursive<T: std::cmp::PartialOrd + Clone>(mut vector: Vec<T>) -> Vec<T> {
    match vector.len() {
        0|1 => vector,
        _ => {
            let pivot = vector.pop().unwrap(); // len is always greater than 1 here, so this is safe
            let lesser: Vec<T> = vector.iter().cloned().filter(|i| i.lt(&pivot)).collect();
            let greater: Vec<T> = vector.into_iter().filter(|i| i.ge(&pivot)).collect();
            let mut lesser = quicksort_recursive(lesser);
            lesser.push(pivot);
            lesser.extend(quicksort_recursive(greater).into_iter());
            lesser
        },
    }
}


fn main() {
    let usage_msg = "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"";

    let mut args = std::env::args();
    args.next(); // first arg is command name, so ignore it

    let input_str = args.next().unwrap_or_else(|| {eprintln!("{usage_msg}"); std::process::exit(-1)});
    let input_vec: Vec<i32> = input_str.split(",") // parse comma separated input into a i32 vector
        .map(|x| x.trim()
            .parse()
            .unwrap_or_else(|_| {eprintln!("{usage_msg}"); std::process::exit(-1)}))
        .collect();

    if input_vec.len() < 2 {
        eprintln!("{usage_msg}");
        std::process::exit(-1);
    }

    println!("{:?}", quicksort_recursive(input_vec));
}
```

{% endraw %}

[Quick Sort](https://sampleprograms.io/projects/quick-sort) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Paolo Cretaro

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).