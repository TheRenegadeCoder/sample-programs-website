---
authors:
- Apurva Vats
- Ștefan-Iulian Alecu
date: 2025-10-30
featured-image: sleep-sort-in-every-language.jpg
last-modified: 2026-05-05
layout: default
tags:
- c-plus-plus
- sleep-sort
title: Sleep Sort in C++
title1: Sleep Sort
title2: in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/sleep-sort/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/sleep-sort/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <chrono>
#include <iostream>
#include <mutex>
#include <optional>
#include <ranges>
#include <string_view>
#include <thread>
#include <utility>
#include <vector>

namespace ranges = std::ranges;
namespace views = std::views;

[[noreturn]] void usage() {
    std::cerr
        << "Usage: please provide a list of at least two integers to sort "
           "in the format \"1, 2, 3, 4, 5\"\n";
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
    return out.size() < 2 ? std::nullopt : std::make_optional(out);
}

void sleep_sort_worker(int value, std::vector<int>& output, std::mutex& mtx) {
    std::this_thread::sleep_for(std::chrono::seconds(value));

    {
        std::lock_guard lock(mtx);
        output.push_back(value);
    }
}

int main(int argc, char* argv[]) {
    if (argc != 2) usage();

    std::string_view input = argv[1];
    auto numbers = parse_vec(input);
    if (!numbers) usage();

    std::vector<int> sorted;
    sorted.reserve(numbers->size());

    std::mutex mtx;
    std::vector<std::thread> threads;
    threads.reserve(numbers->size());

    for (int n : *numbers) {
        threads.emplace_back(sleep_sort_worker, n, std::ref(sorted),
                             std::ref(mtx));
    }

    for (auto& t : threads) t.join();

    for (const char* sep = ""; int val : sorted) {
        std::cout << std::exchange(sep, ", ") << val;
    }
    std::cout << "\n";
}
```

{% endraw %}

Sleep Sort in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Apurva Vats
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).