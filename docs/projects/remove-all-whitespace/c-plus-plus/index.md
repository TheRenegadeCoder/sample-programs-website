---
authors:
- LauraV-702
- Ștefan-Iulian Alecu
date: 2024-11-07
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2026-05-05
layout: default
tags:
- c-plus-plus
- remove-all-whitespace
title: Remove All Whitespace in C++
title1: Remove All
title2: Whitespace in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <algorithm>
#include <cctype>
#include <iostream>
#include <ranges>
#include <string>
#include <string_view>

[[noreturn]] void usage() {
    std::cerr << "Usage: please provide a string\n";
    std::exit(1);
}

int main(int argc, char* argv[]) {
    if (argc < 2) usage();

    std::string_view input = argv[1];
    if (input.empty()) usage();

    auto is_not_space = [](unsigned char c) { return !std::isspace(c); };
    auto filtered = input | std::views::filter(is_not_space);

    std::string result;
    std::ranges::copy(filtered, std::back_inserter(result));

    std::cout << result << '\n';
}
```

{% endraw %}

Remove All Whitespace in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- LauraV-702
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).