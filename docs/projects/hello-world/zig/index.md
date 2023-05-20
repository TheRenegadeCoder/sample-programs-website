---
title: Hello World in Zig
layout: default
date: 2020-10-09
featured-image: hello-world-in-every-language.jpg
last-modified: 2020-10-09

---

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Zig](https://sampleprograms.io/languages/zig) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```zig
const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    try stdout.print("Hello, {}!\n", .{"world"});
}
```

{% endraw %}

[Hello World](https://sampleprograms.io/projects/hello-world) in [Zig](https://sampleprograms.io/languages/zig) was written by:

- Palash Dubey

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).