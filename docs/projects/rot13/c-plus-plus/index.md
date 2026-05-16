---
authors:
- Himanshu Raheja
- Ștefan-Iulian Alecu
date: 2023-10-19
featured-image: rot13-in-every-language.jpg
last-modified: 2026-05-05
layout: default
tags:
- c-plus-plus
- rot13
title: Rot13 in C++
title1: Rot13
title2: in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/rot13/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <algorithm>
#include <cctype>
#include <iostream>
#include <string_view>

[[noreturn]] void usage() {
    std::cerr << "Usage: please provide a string to encrypt\n";
    std::exit(1);
}

constexpr char rot13_char(char c) {
    if (c >= 'a' && c <= 'z') {
        return static_cast<char>('a' + (c - 'a' + 13) % 26);
    }
    if (c >= 'A' && c <= 'Z') {
        return static_cast<char>('A' + (c - 'A' + 13) % 26);
    }
    return c;
}

int main(int argc, char* argv[]) {
    if (argc != 2 || std::string_view(argv[1]).empty()) usage();

    std::string s = argv[1];
    std::ranges::transform(s, s.begin(), rot13_char);
    std::cout << s << '\n';
}
```

{% endraw %}

Rot13 in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Himanshu Raheja
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).