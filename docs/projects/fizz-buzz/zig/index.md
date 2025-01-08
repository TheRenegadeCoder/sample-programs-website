---
authors:
- Zia
date: 2025-01-08
featured-image: fizz-buzz-in-every-language.png
last-modified: 2025-01-08
layout: default
tags:
- fizz-buzz
- zig
title: Fizz Buzz in Zig
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fizz-buzz/zig/how-to-implement-the-solution.md
- sources/programs/fizz-buzz/zig/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fizz Buzz](https://sampleprograms.io/projects/fizz-buzz) in [Zig](https://sampleprograms.io/languages/zig) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```zig
const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    var i: usize = 1;
    while (i <= 100) : (i += 1) {
        if (i % 15 == 0) {
            try stdout.writeAll("FizzBuzz\n");
        } else if (i % 3 == 0) {
            try stdout.writeAll("Fizz\n");
        } else if (i % 5 == 0) {
            try stdout.writeAll("Buzz\n");
        } else {
            try stdout.print("{d}\n", .{i});
        }
    }
}

```

{% endraw %}

Fizz Buzz in [Zig](https://sampleprograms.io/languages/zig) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).