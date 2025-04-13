---
authors:
- Zia
date: 2025-03-29
featured-image: base64-encode-decode-in-every-language.png
last-modified: 2025-03-29
layout: default
tags:
- base64-encode-decode
- zig
title: Base64 Encode Decode in Zig
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/base64-encode-decode/zig/how-to-implement-the-solution.md
- sources/programs/base64-encode-decode/zig/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Base64 Encode Decode](https://sampleprograms.io/projects/base64-encode-decode) in [Zig](https://sampleprograms.io/languages/zig) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```zig
const std = @import("std");
const decoder = std.base64.standard.Decoder;
const encoder = std.base64.standard.Encoder;
const process = std.process;

const stdout = std.io.getStdOut().writer();

fn die() !void {
    try stdout.writeAll("Usage: please provide a mode and a string to encode/decode\n");
    process.exit(1);
}

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    var args = process.args();

    _ = args.next();
    const mode_opt = args.next();
    const src_opt = args.next();

    if (mode_opt == null or src_opt == null) {
        try die();
    }

    const mode = mode_opt.?;
    const src = src_opt.?;

    if (src.len == 0) {
        try die();
    }

    if (std.mem.eql(u8, mode, "encode")) {
        const buffer = try allocator.alloc(u8, encoder.calcSize(src.len));
        defer allocator.free(buffer);

        _ = encoder.encode(buffer, src);
        try stdout.writeAll(buffer);
        _ = try stdout.write("\n");
    } else if (std.mem.eql(u8, mode, "decode")) {
        errdefer {
            die() catch unreachable;
        }
        const buflen = try decoder.calcSizeForSlice(src);

        const buffer = try allocator.alloc(u8, buflen);
        defer allocator.free(buffer);

        decoder.decode(buffer, src) catch {
            try die();
        };

        try stdout.writeAll(buffer);
        _ = try stdout.write("\n");
    } else {
        try die();
    }
}

```

{% endraw %}

Base64 Encode Decode in [Zig](https://sampleprograms.io/languages/zig) was written by:

- Zia

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).