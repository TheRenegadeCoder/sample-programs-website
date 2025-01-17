---
authors:
- rzuckerm
date: 2025-01-17
featured-image: baklava-in-every-language.jpg
last-modified: 2025-01-17
layout: default
tags:
- baklava
- cyclone
title: Baklava in Cyclone
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/cyclone/how-to-implement-the-solution.md
- sources/programs/baklava/cyclone/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [Cyclone](https://sampleprograms.io/languages/cyclone) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```cyclone
#include <stdio.h>
#include <string.h>

int main() {
    char line[22];

    // Tell compiler that pointer math is going to be done, and the result
    // may not be null terminated
    char *@fat @nozeroterm line_ptr = line;

    for (int n = -10; n <= 10; n++) {
        int num_spaces = (n >= 0) ? n : -n;
        int num_stars = 21 - 2 * num_spaces;

        // Write num_spaces " " to line
        memset(line_ptr, ' ', num_spaces);

        // Append num_stars "*" to line
        memset(&line_ptr[num_spaces], '*', num_stars);

        // Null terminate line
        line_ptr[num_spaces + num_stars] = '\0';

        printf("%s\n", line);
    }

    return 0;
}

```

{% endraw %}

Baklava in [Cyclone](https://sampleprograms.io/languages/cyclone) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).