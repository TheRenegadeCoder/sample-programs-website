---
authors:
- Jeremy Grifski
- sachchu007
date: 2022-10-02
featured-image: longest-word-in-every-language.jpg
last-modified: 2022-10-10
layout: default
tags:
- c-plus-plus
- longest-word
title: Longest Word in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/longest-word/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <string>
#include <cstring>
#include <sstream>

using namespace std;

int handle_error()
{
    printf("Usage: please provide a string");
    exit(0);
}

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        handle_error();
    }
    string inputStr(argv[1]);

    if (inputStr.size() == 0)
    {
        handle_error();
    }
    int max = -1;

    stringstream ss(inputStr);
    string word;
    while (ss >> word)
    {

        int size = word.size();
        if (size > max)
        {
            max = size;
        }
    }
    cout << max;

    return 0;
}
```

{% endraw %}

Longest Word in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Grifski
- sachchu007

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).