---
authors:
- Daffa Daraz
- Jeremy Grifski
- Ștefan-Iulian Alecu
date: 2019-10-14
featured-image: prime-number-in-every-language.jpg
last-modified: 2026-05-05
layout: default
tags:
- c-plus-plus
- prime-number
title: Prime Number in C++
title1: Prime Number
title2: in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/prime-number/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <charconv>
#include <iostream>
#include <optional>
#include <string_view>

[[noreturn]] void usage() {
    std::cerr << "Usage: please input a non-negative integer\n";
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

std::optional<int> to_nonnegative_int(std::string_view s) {
    s = trim(s);
    int value{};
    auto [ptr, ec] = std::from_chars(s.data(), s.data() + s.size(), value);
    return (ec == std::errc{} && ptr == s.data() + s.size() && value >= 0)
               ? std::make_optional(value)
               : std::nullopt;
}

bool is_prime(int n) {
    if (n < 2) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;

    for (int i = 5; i <= n / i; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }

    return true;
}

int main(int argc, char* argv[]) {
    if (argc != 2) usage();

    const auto n = to_nonnegative_int(argv[1]);
    if (!n) usage();

    std::cout << (is_prime(*n) ? "Prime" : "Composite") << '\n';
}

```

{% endraw %}

Prime Number in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Daffa Daraz
- Jeremy Grifski
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).