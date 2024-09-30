---
authors:
- Angooj Kumar Singh
- Jeremy Grifski
date: 2019-10-09
featured-image: factorial-in-every-language.jpg
last-modified: 2022-10-10
layout: default
tags:
- c-plus-plus
- factorial
title: Factorial in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/factorial/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <cstdlib>
using namespace std;

int main(int argc, char *argv[])
{
    if (argc < 2 || std::string(argv[1]) == "")
    {
        cout << "Usage: please input a non-negative integer" << endl;
        return 1;
    }

    int n = atoi(argv[1]);
    if (n == 0 && std::string(argv[1]) != "0")
    {
        cout << "Usage: please input a non-negative integer" << endl;
        return 1;
    }
    if (n < 0)
    {
        cout << "Usage: please input a non-negative integer" << endl;
        return 1;
    }
    int i, fact = 1;
    for (i = 1; i <= n; i++)
    {
        fact = fact * i;
    }
    cout << fact << endl;
    return 0;
}

```

{% endraw %}

Factorial in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Angooj Kumar Singh
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).