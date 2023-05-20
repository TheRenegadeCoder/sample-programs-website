---
title: File Input Output in Rust
layout: default
date: 2018-09-13
featured-image: file-input-output-in-every-language.jpg
last-modified: 2018-09-13

---

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Rust](https://sampleprograms.io/languages/rust) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```rust
use std::fs::File;
use std::io::prelude::*;
use std::io::Result;

fn write_file() -> Result<()> {
    let mut out = File::create("output.txt")?;

    let bytes_written = out.write(b"A line of text written to this file in Rust!\n").unwrap_or(0);
    let bytes_written2 = out.write(b"Another line also written by a Rust program!\n").unwrap_or(0);

    if bytes_written == 0 || bytes_written2 == 0 {
        ()
    }

    out.flush()?;

    Ok(())
}

fn read_file() -> Result<()> {
    let mut in_file = File::open("output.txt")?;

    let mut line = String::new();
    match in_file.read_to_string(&mut line) {
        Ok(_)   =>  println!("{}", line),
        Err(_)  =>  panic!("Could not read contents into string!")
    }

    Ok(())
}

fn main() -> Result<()> {
    write_file()?;
    Ok(read_file()?)
}
```

{% endraw %}

[File Input Output](https://sampleprograms.io/projects/file-input-output) in [Rust](https://sampleprograms.io/languages/rust) was written by:

- Noah

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).