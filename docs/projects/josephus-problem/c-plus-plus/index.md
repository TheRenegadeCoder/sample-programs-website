---
authors:
- Apurva Vats
date: 2025-10-26
featured-image: josephus-problem-in-every-language.jpg
last-modified: 2025-10-26
layout: default
tags:
- c-plus-plus
- josephus-problem
title: Josephus Problem in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/josephus-problem/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/josephus-problem/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Josephus Problem](https://sampleprograms.io/projects/josephus-problem) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <string>
#include <stdexcept>
using namespace std;

int josephus(int n, int k) {
    if (n == 1)
        return 1;
    else
        return (josephus(n - 1, k) + k - 1) % n + 1;
}

int main(int argc, char* argv[]) {
    const string usage_msg = "Usage: please input the total number of people and number of people to skip.\n";

    if (argc != 3) {
        cerr << usage_msg;
        return 1;
    }

    try {
        int n = stoi(argv[1]);
        int k = stoi(argv[2]);

        if (n <= 0 || k <= 0) {
            cerr << usage_msg;
            return 1;
        }

        int result = josephus(n, k);
        cout << result << endl;
        return 0;

    } catch (...) {
        cerr << usage_msg;
        return 1;
    }
}

```

{% endraw %}

Josephus Problem in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Apurva Vats

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).