---
authors:
- Meet Thakur
- Ștefan-Iulian Alecu
date: 2025-10-11
featured-image: maximum-subarray-in-every-language.jpg
last-modified: 2026-05-05
layout: default
tags:
- c-plus-plus
- maximum-subarray
title: Maximum Subarray in C++
title1: Maximum
title2: Subarray in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-subarray/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/maximum-subarray/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <algorithm>
#include <charconv>
#include <cstdlib>
#include <iostream>
#include <optional>
#include <ranges>
#include <string_view>
#include <vector>

namespace ranges = std::ranges;
namespace views = std::views;

[[noreturn]] void usage() {
    std::cout << "Usage: Please provide a list of integers in the format: \"1, "
                 "2, 3, 4, 5\"\n";
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
    int value{};
    auto [ptr, ec] = std::from_chars(s.data(), s.data() + s.size(), value);
    return (ec == std::errc{} && ptr == s.data() + s.size())
               ? std::make_optional(value)
               : std::nullopt;
}

std::optional<std::vector<int>> parse_vec(std::string_view s) {
    auto pipe = s | views::split(',') | views::transform([](auto&& r) {
                    return std::string_view{
                        std::addressof(*ranges::begin(r)),
                        static_cast<std::size_t>(ranges::distance(r))};
                }) |
                views::transform(trim) | views::transform(to_int);

    std::vector<int> out;
    for (auto&& opt : pipe) {
        if (!opt) return std::nullopt;
        out.push_back(*opt);
    }
    return out.empty() ? std::nullopt : std::make_optional(out);
}

int max_subarray_sum(const std::vector<int>& arr) {
    int best = arr[0];
    int current = 0;

    for (int x : arr) {
        current = std::max(x, current + x);
        best = std::max(best, current);
    }

    return best;
}

int main(int argc, char* argv[]) {
    if (argc < 2) usage();

    if (auto vec = parse_vec(argv[1]); vec)
        std::cout << max_subarray_sum(*vec) << '\n';
    else
        usage();
}
```

{% endraw %}

Maximum Subarray in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Meet Thakur
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).