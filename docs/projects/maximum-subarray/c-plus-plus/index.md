---
authors:
- Meet Thakur
date: 2025-10-11
featured-image: maximum-subarray-in-every-language.jpg
last-modified: 2025-10-11
layout: default
tags:
- c-plus-plus
- maximum-subarray
title: Maximum Subarray in C++
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
#include <iostream>
#include <sstream>
#include <vector>
#include <limits>
#include <string>

void print_usage()
{
    std::cout << "Usage: Please provide a list of integers in the format: \"1, 2, 3, 4, 5\"\n";
}

int max_subarray_sum(const std::vector<int> &arr)
{
    int max_so_far = std::numeric_limits<int>::min();
    int max_ending_here = 0;

    for (int num : arr)
    {
        max_ending_here += num;

        if (max_so_far < max_ending_here)
        {
            max_so_far = max_ending_here;
        }

        if (max_ending_here < 0)
        {
            max_ending_here = 0;
        }
    }

    return max_so_far;
}

int main(int argc, char *argv[])
{
    if (argc < 2 || std::string(argv[1]).empty())
    {
        print_usage();
        return 1;
    }

    // Parse input string
    std::vector<int> arr;
    std::string input = argv[1];
    std::stringstream ss(input);
    std::string token;

    while (std::getline(ss, token, ','))
    {
        arr.push_back(std::stoi(token));
    }

    // If less than two integers were provided
    if (arr.size() == 1)
    {
        std::cout << arr[0] << "\n";
        return 0;
    }
    else if (arr.empty())
    {
        print_usage();
        return 1;
    }

    // Calculate maximum subarray sum
    int result = max_subarray_sum(arr);

    std::cout << result << "\n";

    return 0;
}

```

{% endraw %}

Maximum Subarray in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Meet Thakur

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).