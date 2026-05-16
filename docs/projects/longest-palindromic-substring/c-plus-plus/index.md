---
authors:
- Meet Thakur
- Ștefan-Iulian Alecu
date: 2025-10-11
featured-image: longest-palindromic-substring-in-every-language.jpg
last-modified: 2026-05-05
layout: default
tags:
- c-plus-plus
- longest-palindromic-substring
title: Longest Palindromic Substring in C++
title1: Longest Palindromic
title2: Substring in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-palindromic-substring/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/longest-palindromic-substring/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <algorithm>
#include <iostream>
#include <string>
#include <string_view>
#include <vector>

std::string_view find_longest_palindrome(std::string_view s) {
    if (s.empty()) return {};

    std::string t;
    t.reserve(s.size() * 2 + 3);
    t += '^';
    for (const char c : s) {
        t += '#';
        t += c;
    }
    t += "#$";

    const int n = static_cast<int>(t.size());
    std::vector<int> radii(n, 0);
    int center = 0;
    int right_boundary = 0;

    for (int i = 1; i < n - 1; ++i) {
        const int mirror = 2 * center - i;

        if (i < right_boundary) {
            radii[i] = std::min(right_boundary - i, radii[mirror]);
        }

        while (t[i + (1 + radii[i])] == t[i - (1 + radii[i])]) {
            ++radii[i];
        }

        if (i + radii[i] > right_boundary) {
            center = i;
            right_boundary = i + radii[i];
        }
    }

    const auto max_it = std::ranges::max_element(radii);
    const int max_radius = *max_it;
    const int center_idx =
        static_cast<int>(std::distance(radii.begin(), max_it));

    return s.substr((center_idx - max_radius - 1) / 2, max_radius);
}

[[noreturn]] void usage() {
    std::cerr << "Usage: please provide a string that contains at least one "
                 "palindrome\n";
    std::exit(1);
}

int main(int argc, char* argv[]) {
    if (argc != 2) usage();

    std::string_view input{argv[1]};
    if (input.empty()) usage();

    auto result = find_longest_palindrome(input);

    if (result.length() <= 1 && input.length() > 1) {
        usage();
    }

    std::cout << result << "\n";
    return 0;
}
```

{% endraw %}

Longest Palindromic Substring in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Meet Thakur
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).