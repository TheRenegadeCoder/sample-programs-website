---
authors:
- Jeremy Grifski
- Sailok Chinta
date: 2019-10-21
featured-image: roman-numeral-in-every-language.jpg
last-modified: 2022-10-10
layout: default
tags:
- c-plus-plus
- roman-numeral
title: Roman Numeral in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/roman-numeral/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/roman-numeral/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Roman Numeral](https://sampleprograms.io/projects/roman-numeral) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

bool is_roman(char x)
{
    return !(x == 'I' || x == 'V' || x == 'X' || x == 'L' || x == 'C' || x == 'D' || x == 'M');
}

int main(int argc, char *argv[])
{
    if (argv[1] == NULL)
    {
        cerr << "Usage: please provide a string of roman numerals" << endl;
        exit(0);
    }

    string s;
    s = argv[1];

    for (char c : s)
    {
        if (is_roman(c))
        {
            cerr << "Error: invalid string of roman numerals" << endl;
            exit(0);
        }
    }

    map<char, int> value;
    value['I'] = 1;
    value['V'] = 5;
    value['X'] = 10;
    value['L'] = 50;
    value['C'] = 100;
    value['D'] = 500;
    value['M'] = 1000;

    int num = 0;

    for (int i = s.size() - 1; i >= 0; i--)
    {
        if (value[s[i]] > value[s[i - 1]] && i > 0)
        {
            num += value[s[i]] - value[s[i - 1]];
            i--;
        }
        else
        {
            num += value[s[i]];
        }
    }

    cout << num << endl;
}

```

{% endraw %}

Roman Numeral in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Grifski
- Sailok Chinta

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).