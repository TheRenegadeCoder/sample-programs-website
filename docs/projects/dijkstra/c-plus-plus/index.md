---
authors:
- Ajay Maheshwari
- Ștefan-Iulian Alecu
date: 2022-10-06
featured-image: dijkstra-in-every-language.jpg
last-modified: 2026-05-05
layout: default
tags:
- c-plus-plus
- dijkstra
title: Dijkstra in C++
title1: Dijkstra
title2: in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/dijkstra/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/dijkstra/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Dijkstra](https://sampleprograms.io/projects/dijkstra) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <algorithm>
#include <charconv>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <queue>
#include <ranges>
#include <string_view>
#include <vector>

namespace ranges = std::ranges;
namespace views = std::views;

using Node = std::uint32_t;
using Weight = std::int64_t;
using Matrix = std::vector<Weight>;

constexpr Weight INF = std::numeric_limits<Weight>::max() / 2;

struct State {
    Weight dist;
    Node u;

    auto operator<=>(const State& other) const noexcept {
        return dist <=> other.dist;
    }
};

[[noreturn]] void usage() {
    std::cerr
        << R"(Usage: please provide three inputs: a serialized matrix, a source node and a destination node)"
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

template <std::integral T>
std::optional<T> to_num(std::string_view s) {
    T value{};
    auto [ptr, ec] = std::from_chars(s.data(), s.data() + s.size(), value);
    return (ec == std::errc{} && ptr == s.data() + s.size())
               ? std::make_optional(value)
               : std::nullopt;
}

std::optional<Matrix> parse_weights(std::string_view s) {
    if (s.empty()) return std::nullopt;

    Matrix m;
    m.reserve(ranges::count(s, ',') + 1);

    auto weight_view = s | views::split(',') | views::transform([](auto&& r) {
                           return std::string_view{
                               std::addressof(*ranges::begin(r)),
                               static_cast<std::size_t>(ranges::distance(r))};
                       }) |
                       views::transform(trim) |
                       views::transform(to_num<Weight>);

    for (auto&& opt : weight_view) {
        if (!opt) return std::nullopt;
        m.push_back(*opt);
    }
    return m;
}

Weight dijkstra(const Matrix& matrix, std::size_t n, Node src, Node dest) {
    std::vector<Weight> dist(n, INF);
    dist[src] = 0;

    std::priority_queue<State, std::vector<State>, std::greater<>> pq;
    pq.push({0, src});

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();

        if (u == dest) return d;
        if (d > dist[u]) continue;

        auto row = matrix | views::drop(u * n) | views::take(n);

        for (std::size_t v = 0; v < n; ++v) {
            const Weight w = row[v];
            if (w <= 0) continue;

            if (Weight new_dist = d + w; new_dist < dist[v]) {
                dist[v] = new_dist;
                pq.push({new_dist, static_cast<Node>(v)});
            }
        }
    }

    return dist[dest];
}

int main(int argc, char* argv[]) {
    if (argc < 4) usage();

    auto matrix_opt = parse_weights(argv[1]);
    if (!matrix_opt) usage();

    const auto matrix = std::move(*matrix_opt);
    const std::size_t n = std::sqrt(matrix.size());

    if (n == 0 || n * n != matrix.size()) usage();
    if (ranges::any_of(matrix, [](Weight w) { return w < 0; })) usage();

    const auto source = to_num<Node>(argv[2]);
    const auto destination = to_num<Node>(argv[3]);

    if (!source || *source >= n) usage();
    if (!destination || *destination >= n) usage();

    const Weight result = dijkstra(matrix, n, *source, *destination);

    if (result >= INF) usage();
    std::cout << result << '\n';
}
```

{% endraw %}

Dijkstra in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Ajay Maheshwari
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).