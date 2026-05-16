---
authors:
- Jeremy Grifski
- killbotxd
- Ștefan-Iulian Alecu
date: 2019-10-09
featured-image: even-odd-in-every-language.jpg
last-modified: 2026-05-05
layout: default
tags:
- c-plus-plus
- even-odd
title: Even Odd in C++
title1: Even Odd
title2: in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/even-odd/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <charconv>
#include <iostream>
#include <optional>
#include <string_view>

[[noreturn]] void usage() {
    std::cout << "Usage: please input a number\n";
    std::exit(1);
}

static constexpr std::string_view ws = " \t\n\r\f\v";
constexpr std::string_view trim(std::string_view s) {
    const auto start = s.find_first_not_of(ws);
    if (start == std::string_view::npos) return "";
    s.remove_prefix(start);

    const auto end = s.find_last_not_of(ws);
    s.remove_suffix(s.size() - 1 - end);
    return s;
}

std::optional<int> to_int(std::string_view s) {
    s = trim(s);
    int value{};
    auto [ptr, ec] = std::from_chars(s.data(), s.data() + s.size(), value);
    return (ec == std::errc{} && ptr == s.data() + s.size())
               ? std::make_optional(value)
               : std::nullopt;
}

int main(int argc, char* argv[]) {
    if (argc != 2) usage();

    const auto input_opt = to_int(argv[1]);
    if (!input_opt) usage();

    const int input = *input_opt;

    std::cout << ((input % 2 == 0) ? "Even" : "Odd") << '\n';
}
```

{% endraw %}

Even Odd in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Grifski
- killbotxd
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).