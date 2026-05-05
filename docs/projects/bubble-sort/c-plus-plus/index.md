---
authors:
- Jayden Thrasher
- Jeremy Grifski
- Ștefan-Iulian Alecu
date: 2019-10-02
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2026-05-05
layout: default
tags:
- bubble-sort
- c-plus-plus
title: Bubble Sort in C++
title1: Bubble Sort
title2: in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/bubble-sort/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/bubble-sort/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <algorithm>
#include <charconv>
#include <iostream>
#include <optional>
#include <ranges>
#include <string_view>
#include <utility>
#include <vector>

namespace ranges = std::ranges;
namespace views = std::views;

[[noreturn]] void usage() {
    std::cerr
        << R"(Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5")"
        << '\n';
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

template <ranges::forward_range R>
    requires std::sortable<ranges::iterator_t<R>>
void bubble_sort(R&& r) {
    auto end_it = ranges::end(r);
    if (ranges::begin(r) == end_it) return;

    while (ranges::begin(r) != end_it) {
        auto last_swapped = ranges::begin(r);
        auto current = ranges::begin(r);
        auto next = std::next(current);

        while (next != end_it) {
            if (*next < *current) {
                ranges::iter_swap(current, next);
                last_swapped = next;
            }
            current = next++;
        }
        if (last_swapped == ranges::begin(r)) break;
        end_it = last_swapped;
    }
}

int main(int argc, char* argv[]) {
    if (argc != 2) usage();

    const std::string_view input{argv[1]};
    auto ints_view = input | views::split(',') |
                     views::transform([](auto&& rng) {
                         return std::string_view(rng.begin(), rng.end());
                     }) |
                     views::transform(to_int) |
                     views::filter([](auto&& opt) { return opt.has_value(); }) |
                     views::transform([](auto&& opt) { return *opt; });

    std::vector<int> numbers;
    ranges::copy(ints_view, std::back_inserter(numbers));

    if (numbers.size() < 2) usage();

    bubble_sort(numbers);

    for (const char* sep = ""; int val : numbers) {
        std::cout << std::exchange(sep, ", ") << val;
    }
    std::cout << "\n";

    return 0;
}
```

{% endraw %}

Bubble Sort in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jayden Thrasher
- Jeremy Grifski
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).