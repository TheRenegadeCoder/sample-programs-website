---
title: Maximum Array Rotation in Rust
layout: default
date: 2023-04-09
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2023-04-09

---

Welcome to the [Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
use std::env::args;
use std::process::exit;
use std::str::FromStr;
use std::cmp::max;

fn usage() -> ! {
    println!("Usage: please provide a list of integers (e.g. \"8, 3, 1, 2\")");
    exit(0);
}

fn parse_int<T: FromStr>(s: &str) -> Result<T, <T as FromStr>::Err> {
    s.trim().parse::<T>()
}

fn parse_int_list<T: FromStr>(s: &str) -> Result<Vec<T>, <T as FromStr>::Err> {
    s.split(',')
        .map(parse_int)
        .collect::<Result<Vec<T>, <T as FromStr>::Err>>()
}

// Find maximum array rotation, max{W(k), k=0..N-1}, where:
//
//     W(k) = sum{i*a[i+k mod N], i=0..N-1}
//
// The value of W(k) can be calculated from W(k-1) as follows:
//
//     W(k) = W(k-1) - S + N*a[k-1]
//
// where:
//
//     S = sum{a[i], i=0..N-1} = sum{a[i+x mod N], i=0..N-1}
//
// where: x is any arbitary value
//
// Proof:
//
// - Set up initial assumption for W(k):
//
//     W(k-1) - S + N*a[k-1] = sum{i*a[i+k-1 mod N], i=0..N-1} - sum{a[i+k-1 mod N}, i=0..N-1} + N*a[k-1]
//
// - Combine the two sums:
//
//     = sum{(i-1)*a[i+k-1 mod N], i=0..N-1} + N*a[k-1]
//
// - Pull out the i=0 term:
//     = -a[k-1] + sum{(i-1)*a[i+k-1 mod N], i=1..N-1} + N*a[k-1]
//
// - Combine the a[k-1] terms:
//
//     = sum{(i-1}*a[i+k-1 mod N], i=1..N-1) + (N-1)*a[k-1]
//
// - Change indexing from i=1..N-1 to 0..N-2:
//
//     = sum{i*a[i+k mod N], i=0..N-2} + (N-1)*a[k-1]
//
// - Bring the i=N-1 term back into the sum since N-1+k mod N equals k-1:
//
//     = sum{i*a[i+k mod N], i=0..N-1}
//
// - The above equals W(k)
fn maximum_array_rotation(arr: &Vec<i32>) -> i32 {
    // Calculate sum and initial array rotation
    let s: i32 = arr.iter()
        .sum::<i32>();
    let n: usize = arr.len();
    let mut w: i32 = (0..n)
        .map(|i| (i as i32) * arr[i])
        .sum::<i32>();

    // Initialize maximum array rotation
    let mut wmax: i32 = w;

    // Adjust array rotation and update maximum
    for value in arr.iter().take(n - 1) {
        w += (n as i32) * value - s;
        wmax = max(w, wmax);
    }

    wmax
}

fn main() {
    let mut args = args().skip(1);

    // Convert 1st command-line argument to list of integers
    let arr: Vec<i32> = args
        .next()
        .and_then(|s| parse_int_list(&s).ok())
        .unwrap_or_else(|| usage());

    // Get maximum array rotation and display it
    println!("{}", maximum_array_rotation(&arr));
}
```

{% endraw %}

[Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 08 2023 19:53:07. The solution was first committed on Apr 09 2023 11:04:19. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).