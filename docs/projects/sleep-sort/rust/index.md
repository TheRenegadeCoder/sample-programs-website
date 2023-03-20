---

title: Sleep Sort in Rust
layout: default
date: 2022-04-28
last-modified: 2023-03-20

---

Welcome to the [Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
extern mod std;
use std::timer::sleep;
use std::uv::global_loop;
fn main() {
    for os::args().tail().each |&arg| {
        do task::spawn {
            let n = uint::from_str(arg).get();
            sleep(global_loop::get(), n);
            io::println(arg);
        }
    }
}
```

{% endraw %}

[Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Nishant Giri

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).