---
authors:
- rzuckerm
date: 2024-09-23
featured-image: baklava-in-every-language.jpg
last-modified: 2024-09-23
layout: default
tags:
- baklava
- zig
title: Baklava in Zig
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/zig/how-to-implement-the-solution.md
- sources/programs/baklava/zig/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Zig](https://sampleprograms.io/languages/zig) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```zig
const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    const spaces = " " ** 10;
    const stars = "*" ** 21;
    var i: i32 = -10;
    while (i <= 10): (i += 1) {
        const numSpaces: usize = @intCast(@abs(i));
        const numStars: usize = 21 - numSpaces * 2;
        try stdout.print("{s}{s}\n", .{spaces[0..numSpaces], stars[0..numStars]});
    }
}

```

{% endraw %}

Baklava in [Zig](https://sampleprograms.io/languages/zig) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).