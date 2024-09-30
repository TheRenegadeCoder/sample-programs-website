---
authors:
- Jeremy Grifski
- killbotxd
date: 2019-10-09
featured-image: even-odd-in-every-language.jpg
last-modified: 2022-10-10
layout: default
tags:
- c-plus-plus
- even-odd
title: Even Odd in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/even-odd/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/even-odd/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Even Odd](https://sampleprograms.io/projects/even-odd) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <stdlib.h>
#include <string.h>

using namespace std;

int main(int argc, char **argv)
{
    if (argc == 1 || argv[1][0] == '\0' || (atoi(argv[1]) == 0 && strcmp(argv[1], "0") != 0))
    {
        cout << "Usage: please input a number\n";
    }
    else
    {
        int input = atoi(argv[1]);
        if (input % 2 == 0)
        {
            cout << "Even\n";
        }
        else
        {
            cout << "Odd\n";
        }
    }

    return 0;
}

```

{% endraw %}

Even Odd in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Grifski
- killbotxd

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).