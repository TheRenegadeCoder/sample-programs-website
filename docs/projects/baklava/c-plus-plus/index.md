---
authors:
- Behnam Ahmad khan beigi
- Jeremy Grifski
- yottanami
date: 2019-10-09
featured-image: baklava-in-every-language.jpg
last-modified: 2022-10-10
layout: default
tags:
- baklava
- c-plus-plus
title: Baklava in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/baklava/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/baklava/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Baklava](https://sampleprograms.io/projects/baklava) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    int i, j, k, n;
    n = 21;
    for (i = 1; i <= (n + 1) / 2;)
    {
        for (k = 1; (n + 1) / 2 - i >= k; k++)
            cout << " ";
        for (j = 1; j < 2 * i; j++)
            cout << "*";
        cout << "\n";
        i++;
    }
    if (2 * i - 1 >= n)
    {
        for (i = (n + 1) / 2 - 1; i >= 1; i--)
        {
            for (k = 1; (n + 1) / 2 - i >= k; k++)
                cout << " ";
            for (j = 1; j < 2 * i; j++)
                cout << "*";
            cout << "\n";
        }
    }
    return (0);
}

```

{% endraw %}

Baklava in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Behnam Ahmad khan beigi
- Jeremy Grifski
- yottanami

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).