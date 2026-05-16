---
authors:
- Jeremy Grifski
- Marius
- Parker Johansen
- Ștefan-Iulian Alecu
date: 2018-10-06
featured-image: fibonacci-in-every-language.jpg
last-modified: 2026-05-05
layout: default
tags:
- c-plus-plus
- fibonacci
title: Fibonacci in C++
title1: Fibonacci
title2: in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/fibonacci/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <charconv>
#include <format>
#include <iostream>
#include <optional>
#include <ranges>
#include <string_view>

namespace views = std::views;

[[noreturn]] void usage() {
    std::cerr
        << "Usage: please input the count of fibonacci numbers to output\n";
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

auto fibonacci_sequence() {
    return views::iota(0) | views::transform([a = 1LL, b = 1LL](auto) mutable {
               auto out = a;
               auto next = a + b;
               a = b;
               b = next;
               return out;
           });
}

int main(int argc, char* argv[]) {
    if (argc < 2) usage();

    if (auto n_opt = to_int(argv[1]); !n_opt || *n_opt < 0) {
        usage();
    } else {
        const int n = *n_opt;

        int index = 1;
        for (const auto value : fibonacci_sequence() | views::take(n)) {
            std::cout << std::format("{}: {}\n", index++, value);
        }
    }
}

```

{% endraw %}

Fibonacci in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Grifski
- Marius
- Parker Johansen
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).