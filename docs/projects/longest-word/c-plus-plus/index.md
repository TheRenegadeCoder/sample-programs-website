---
authors:
- Jeremy Grifski
- sachchu007
- Ștefan-Iulian Alecu
date: 2022-10-02
featured-image: longest-word-in-every-language.jpg
last-modified: 2026-05-05
layout: default
tags:
- c-plus-plus
- longest-word
title: Longest Word in C++
title1: Longest
title2: Word in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/longest-word/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <algorithm>
#include <cctype>
#include <iostream>
#include <string_view>

[[noreturn]] void usage() {
    std::cerr << "Usage: please provide a string\n";
    std::exit(1);
}

int main(int argc, char* argv[]) {
    if (argc != 2) usage();

    std::string_view input = argv[1];
    if (input.empty()) usage();

    auto is_space = [](unsigned char c) { return std::isspace(c) != 0; };

    size_t best = 0;
    size_t cur = 0;

    for (unsigned char c : input) {
        if (is_space(c)) {
            best = std::max(best, cur);
            cur = 0;
        } else {
            ++cur;
        }
    }

    std::cout << std::max(best, cur) << '\n';
}
```

{% endraw %}

Longest Word in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Grifski
- sachchu007
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).