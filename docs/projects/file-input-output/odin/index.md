---
authors:
- nallovint
date: 2024-07-11
featured-image: file-input-output-in-every-language.jpg
last-modified: 2024-07-11
layout: default
tags:
- file-input-output
- odin
title: File Input Output in Odin
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/file-input-output/odin/how-to-implement-the-solution.md
- sources/programs/file-input-output/odin/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [File Input Output](https://sampleprograms.io/projects/file-input-output) in [Odin](https://sampleprograms.io/languages/odin) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```odin
package main

import "core:os"
import "core:fmt"
import "core:strings"

read_file :: proc(filepath: string) {
    data, ok := os.read_entire_file(filepath, context.allocator) // context.allocator will track the memory held by this data
    if !ok {
        fmt.println("Error reading file")
    }
    defer delete(data, context.allocator) // we're using the allocator to delete the memory. defer means 'execute this code when the function returns'
    it := string(data)
    for line in strings.split_lines_iterator(&it) { // run through all the lines
        fmt.println(line)
    }
}

write_file :: proc(filepath: string) {
    data_as_string := "Odin is great!"
    data_as_bytes := transmute([]byte)(data_as_string) // 'transmute' casts our string to a byte array
    ok := os.write_entire_file(filepath, data_as_bytes)
    if !ok {
        fmt.println("Error writing file")
    }
}

main :: proc() {
    
    write_file("output.txt")
    read_file("output.txt")
}
```

{% endraw %}

File Input Output in [Odin](https://sampleprograms.io/languages/odin) was written by:

- nallovint

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).