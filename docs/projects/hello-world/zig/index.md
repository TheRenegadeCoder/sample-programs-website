---
authors:
- Palash Dubey
- rzuckerm
date: 2020-10-09
featured-image: hello-world-in-every-language.jpg
last-modified: 2023-08-22
layout: default
tags:
- hello-world
- zig
title: Hello World in Zig
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/hello-world/zig/how-to-implement-the-solution.md
- sources/programs/hello-world/zig/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Hello World](https://sampleprograms.io/projects/hello-world) in [Zig](https://sampleprograms.io/languages/zig) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```zig
const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    try stdout.writeAll("Hello, World!\n");
}

```

{% endraw %}

Hello World in [Zig](https://sampleprograms.io/languages/zig) was written by:

- Palash Dubey
- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).