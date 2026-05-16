---
authors:
- Jeremy Grifski
- Sailok Chinta
- Ștefan-Iulian Alecu
date: 2019-10-21
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2026-05-05
layout: default
tags:
- c-plus-plus
- roman-numeral
title: Roman Numeral in C++
title1: Roman Numeral
title2: in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/roman-numeral/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/roman-numeral/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <algorithm>
#include <iostream>
#include <ranges>
#include <string_view>

[[noreturn]] void usage() {
    std::cerr << "Usage: please provide a string of roman numerals\n";
    std::exit(1);
}

[[noreturn]] void error() {
    std::cerr << "Error: invalid string of roman numerals\n";
    std::exit(1);
}

constexpr int value(char c) {
    switch (c) {
        case 'I':
            return 1;
        case 'V':
            return 5;
        case 'X':
            return 10;
        case 'L':
            return 50;
        case 'C':
            return 100;
        case 'D':
            return 500;
        case 'M':
            return 1000;
        default:
            return -1;
    }
}

constexpr bool is_valid(char c) { return value(c) != -1; }

int main(int argc, char* argv[]) {
    if (argc < 2) usage();

    std::string_view s = argv[1];

    if (s.empty()) {
        std::cout << 0 << '\n';
        return 0;
    }

    if (!std::ranges::all_of(s, is_valid)) error();

    int result = 0;

    for (std::size_t i = 0; i < s.size(); ++i) {
        int curr = value(s[i]);

        if (i + 1 < s.size()) {
            int next = value(s[i + 1]);

            if (curr < next) {
                result += next - curr;
                ++i;
                continue;
            }
        }

        result += curr;
    }

    std::cout << result << '\n';
}
```

{% endraw %}

Roman Numeral in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Grifski
- Sailok Chinta
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).