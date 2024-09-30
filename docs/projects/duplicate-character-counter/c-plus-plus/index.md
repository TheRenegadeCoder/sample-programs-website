---
authors:
- Jeremy Grifski
- Vipin Yadav
date: 2022-10-03
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2022-10-10
layout: default
tags:
- c-plus-plus
- duplicate-character-counter
title: Duplicate Character Counter in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

int handle_error()
{
    cout << "Usage: please provide a string\n";
    exit(0);
}
int main(int argc, char *argv[])
{

    if (argc != 2)
    {
        handle_error();
    }
    string inputStr(argv[1]);

    if (inputStr.size() == 0)
    {
        handle_error();
    }

    unordered_map<char, int> m1;

    for (auto x : inputStr)
    {
        if (m1.find(x) == m1.end())
        {
            m1.insert({x, 1});
        }
        else
        {
            m1[x]++;
        }
    }
    int flag = 1;
    for (int i = 0; i < inputStr.length(); i++)
    {
        if (m1[inputStr[i]] > 1)
        {
            flag = 0;
            cout << inputStr[i] << ": " << m1[inputStr[i]] << "\n";
            m1[inputStr[i]] = 0;
        }
    }
    if (flag == 1)
        cout << "No duplicate characters\n";
    return 0;
}
```

{% endraw %}

Duplicate Character Counter in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Grifski
- Vipin Yadav

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).