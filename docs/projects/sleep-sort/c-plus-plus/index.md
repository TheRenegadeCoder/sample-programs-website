---
authors:
- Apurva Vats
date: 2025-10-30
featured-image: sleep-sort-in-every-language.jpg
last-modified: 2025-10-30
layout: default
tags:
- c-plus-plus
- sleep-sort
title: Sleep Sort in C++
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
#include <iostream>
#include <vector>
#include <string>
#include <thread>
#include <mutex>
#include <sstream>
#include <chrono>

std::mutex mtx;
std::vector<int> sorted_numbers;

void sortNumber(int number) {
    std::this_thread::sleep_for(std::chrono::seconds(number));
    std::lock_guard<std::mutex> lock(mtx);
    sorted_numbers.push_back(number);
}

std::vector<int> parseInput(const std::string &input) {
    std::vector<int> numbers;
    std::stringstream ss(input);
    std::string token;

    while (std::getline(ss, token, ',')) {
        try {
            int num = std::stoi(token);
            numbers.push_back(num);
        } catch (...) {
            throw std::invalid_argument("Invalid input");
        }
    }

    return numbers;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"\n";
        return 1;
    }

    std::string input = argv[1];
    if (input.empty() || input[0] == ' ') {
        std::cerr << "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"\n";
        return 1;
    }

    std::vector<int> numbers;
    try {
        numbers = parseInput(input);
    } catch (...) {
        std::cerr << "Usage: please provide a valid list of integers in the format \"1, 2, 3, 4, 5\"\n";
        return 1;
    }

    if (numbers.size() < 2) {
        std::cerr << "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"\n";
        return 1;
    }

    std::vector<std::thread> threads;
    for (int num : numbers) {
        threads.emplace_back(sortNumber, num);
    }

    for (auto &t : threads) {
        t.join();
    }

    for (size_t i = 0; i < sorted_numbers.size(); ++i) {
        std::cout << sorted_numbers[i];
        if (i < sorted_numbers.size() - 1) std::cout << ", ";
    }
    std::cout << std::endl;

    return 0;
}

```

{% endraw %}

Sleep Sort in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Apurva Vats

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).