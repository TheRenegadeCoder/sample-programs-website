---
authors:
- Ford Smith
- Ștefan-Iulian Alecu
date: 2019-10-09
featured-image: capitalize-in-every-language.jpg
last-modified: 2026-05-05
layout: default
tags:
- c-plus-plus
- capitalize
title: Capitalize in C++
title1: Capitalize
title2: in C++
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
#include <cctype>
#include <format>
#include <iostream>
#include <string_view>

[[noreturn]] void usage() {
    std::cerr << "Usage: please provide a string\n";
    std::exit(1);
}

int main(int argc, char* argv[]) {
    if (argc < 2) usage();

    std::string_view input{argv[1]};
    if (input.empty()) usage();

    char head = static_cast<char>(
        std::toupper(static_cast<unsigned char>(input.front())));

    std::string_view tail = input.substr(1);

    std::cout << std::format("{}{}\n", head, tail);
    return 0;
}
```

{% endraw %}

Capitalize in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Ford Smith
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).