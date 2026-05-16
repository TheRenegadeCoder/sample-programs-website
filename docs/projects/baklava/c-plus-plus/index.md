---
authors:
- Behnam Ahmad khan beigi
- Ștefan-Iulian Alecu
date: 2019-10-09
featured-image: baklava-in-every-language.jpg
last-modified: 2026-05-05
layout: default
tags:
- baklava
- c-plus-plus
title: Baklava in C++
title1: Baklava
title2: in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/baklava/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <cmath>
#include <iostream>
#include <ranges>
#include <string>

int main() {
    constexpr int n = 21;
    constexpr int mid = n / 2;

    for (int i : std::views::iota(-mid, mid + 1)) {
        int stars = n - 2 * std::abs(i);
        int spaces = std::abs(i);

        std::cout << std::string(spaces, ' ') << std::string(stars, '*')
                  << '\n';
    }
}
```

{% endraw %}

Baklava in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Behnam Ahmad khan beigi
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).