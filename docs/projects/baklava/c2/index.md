---
authors:
- rzuckerm
date: 2025-01-14
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-14
layout: default
tags:
- baklava
- c2
title: Baklava in C2
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/c2/how-to-implement-the-solution.md
- sources/programs/baklava/c2/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [C2](https://sampleprograms.io/languages/c2) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c2
module hello_world;

import stdio as io;
import string;

public fn i32 main(i32 argc, char** argv) {
    char[22] line;
    for (u32 n = 0; n <= 20; n++) {
        u32 num_spaces = (n < 10) ? (10 - n) : (n - 10);
        u32 num_stars = 21 - 2 * num_spaces;

        // Fill line with num_spaces " "
        string.memset(line, ' ', num_spaces);

        // Append num_stars "*"
        string.memset(&line[num_spaces], '*', num_stars);

        // Null terminate line
        line[num_spaces + num_stars] = '\0';

        io.printf("%s\n", line);
    }

    return 0;
}

```

{% endraw %}

Baklava in [C2](https://sampleprograms.io/languages/c2) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).