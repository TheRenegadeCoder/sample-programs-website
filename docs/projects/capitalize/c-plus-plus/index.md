---
authors:
- Ford Smith
- Jeremy Grifski
date: 2019-10-09
featured-image: capitalize-in-every-language.jpg
last-modified: 2022-10-10
layout: default
tags:
- c-plus-plus
- capitalize
title: Capitalize in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/capitalize/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <cstring>

int main(int argc, const char *argv[])
{
    if (argc < 2 || argv[1][0] == '\0')
    {
        std::cout << "Usage: please provide a string";
        return 1;
    }

    for (int j = 0; j < (int)std::strlen(argv[1]); j++)
    {
        if (j == 0)
            std::cout << (char)toupper(argv[1][j]);
        else
            std::cout << *(argv[1] + sizeof(char) * j);
    }
}

```

{% endraw %}

Capitalize in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Ford Smith
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).