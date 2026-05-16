---
authors:
- Jeremy Grifski
- Vipin Yadav
- Ștefan-Iulian Alecu
date: 2022-10-03
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2026-05-05
layout: default
tags:
- c-plus-plus
- duplicate-character-counter
title: Duplicate Character Counter in C++
title1: Duplicate Character
title2: Counter in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <array>
#include <format>
#include <iostream>
#include <string_view>

[[noreturn]] void usage() {
    std::cout << "Usage: please provide a string\n";
    std::exit(1);
}

int main(int argc, char* argv[]) {
    if (argc != 2) usage();

    std::string_view input{argv[1]};
    if (input.empty()) usage();

    std::array<std::size_t, 256> counts{};

    for (const auto c : input) {
        counts[c]++;
    }

    bool any_duplicates = false;

    for (const auto c : input) {
        if (counts[c] > 1) {
            std::cout << std::format("{}: {}\n", c, counts[c]);
            counts[c] = 0;
            any_duplicates = true;
        }
    }

    if (!any_duplicates) {
        std::cout << "No duplicate characters\n";
    }
}
```

{% endraw %}

Duplicate Character Counter in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Grifski
- Vipin Yadav
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).