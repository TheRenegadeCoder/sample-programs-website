---

title: Binary Search in Rust
layout: default
date: 2022-04-28
last-modified: 2023-02-19

---

Welcome to the [Binary Search](https://sampleprograms.io/projects/binary-search) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
#![feature(is_sorted)]

use std::env;

fn binary_search(search_arr: &Vec<i32>, target: &i32) -> Option<usize> {
  let mut low: i8 = 0;
  let mut high: i8 = search_arr.len() as i8 - 1;

  while low <= high {
    let mid = (((high - low) / 2) + low) as usize;
    let val = &search_arr[mid];

    if val == target {
        return Some(mid);
    }

    // If value is < target then search between mid + 1 and high
    if val < target {
        low = mid as i8 + 1;
    }

    // If value is > target then search between low and mid - 1
    if val > target {
        high = mid as i8 - 1;
    }
  }

  return None;
}

fn main() {
  let err_msg = "Usage: please provide a list of sorted integers \"1, 4, 5, 11, 12\" and the integer to find \"11\"";
  let args: Vec<String> = env::args().collect();

  if args.len() < 3 {
    panic!(err_msg);
  }

  let arr: Vec<i32> = args[1].clone()
    .split(",")
    .map(|s| s.trim().parse().expect(err_msg))
    .collect();

  if !arr.is_sorted() {
    panic!(err_msg);
  }
  
  let target = args[2].clone()
    .parse()
    .expect(err_msg);
  
  match binary_search(&arr, &target) {
    Some(_) => println!("true"),
    None => println!("false"),
  }
}
```

{% endraw %}

[Binary Search](https://sampleprograms.io/projects/binary-search) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Andrew Johnson

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 03 2020 18:37:05. The solution was first committed on Oct 03 2020 14:05:42. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).