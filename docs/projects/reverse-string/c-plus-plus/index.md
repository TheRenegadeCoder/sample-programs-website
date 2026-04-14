---
authors:
- Jeremy Grifski
- Noah
- "\u0218tefan-Iulian Alecu"
date: 2018-09-14
featured-image: reverse-string-in-every-language.jpg
last-modified: 2026-04-15
layout: default
tags:
- c-plus-plus
- reverse-string
title: Reverse String in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/reverse-string/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/reverse-string/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Reverse String](https://sampleprograms.io/projects/reverse-string) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <algorithm>
#include <iostream>
#include <string>

int main(int argc, char *argv[])
{
    if (argc < 2)
        return 0;

    std::string s = argv[1];
    std::reverse(s.begin(), s.end());

    std::cout << s << "\n";
}
```

{% endraw %}

Reverse String in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Grifski
- Noah
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).