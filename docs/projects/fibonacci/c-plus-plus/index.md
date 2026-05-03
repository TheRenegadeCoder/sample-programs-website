---
authors:
- Jeremy Grifski
- Marius
- Parker Johansen
- Ștefan-Iulian Alecu
date: 2018-10-06
featured-image: fibonacci-in-every-language.jpg
last-modified: 2026-04-15
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
#include <cstdlib>
#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    if (argc < 2 || std::string(argv[1]) == "")
    {
        cout
            << "Usage: please input the count of fibonacci numbers to output"
            << endl;
        return 1;
    }

    int n = atoi(argv[1]);
    if (n == 0 && std::string(argv[1]) != "0")
    {
        cout
            << "Usage: please input the count of fibonacci numbers to output"
            << endl;
        return 1;
    }
    int first = 0;
    int second = 1;
    int result = 0;

    for (int i = 1; i <= n; ++i)
    {
        result = first + second;
        first = second;
        second = result;
        cout << i << ": " << first << endl;
    }
    return 0;
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