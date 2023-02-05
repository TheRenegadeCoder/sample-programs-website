---

title: Insertion Sort in Rust
layout: default
date: 2022-04-28
last-modified: 2023-02-05

---

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
use std::env;

fn insertion_sort(arr: &mut Vec<i32>) {
  for i in 0..arr.len() {
    for j in (0..i).rev() {
      if arr[j] >= arr[j+1] {
        arr.swap(j, j+1);
      } else {
        break;
      }
    }
  }
}

fn main() {
  let err_msg = "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"";
  let args: Vec<String> = env::args().collect();

  if args.len() < 2 {
    panic!(err_msg);
  }

  let mut arr: Vec<i32> = args[1].clone()
    .split(",")
    .map(|s| s.trim().parse().expect(err_msg))
    .collect();

  if arr.len() < 2 {
    panic!(err_msg);
  }
  
  insertion_sort(&mut arr);
  println!("{:?}", arr);
}
```

{% endraw %}

[Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Andrew Johnson

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).