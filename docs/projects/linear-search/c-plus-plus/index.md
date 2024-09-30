---
authors:
- Jeremy Grifski
- rzuckerm
- Vipin Yadav
date: 2022-10-03
featured-image: linear-search-in-every-language.jpg
last-modified: 2023-01-29
layout: default
tags:
- c-plus-plus
- linear-search
title: Linear Search in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/linear-search/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <vector>
#include <string>
#include <cstring>
using namespace std;

int main(int argc, char *argv[])
{
    string error = "Usage: please provide a list of integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")";

    if (argc != 3)
    {
        cout << error << endl;
        return 1;
    }
    int numberLength = strlen(argv[1]);
    int keyLength = strlen(argv[1]);

    if (numberLength == 0 || keyLength == 0)
    {
        cout << error << endl;
        return 1;
    }
    vector<int> arr;
    string temp = "";
    for (int i = 0; i < numberLength; i++)
    {
        if (argv[1][i] == ',')
        {
            arr.push_back(stoi(temp));
            temp = "";
        }
        else
        {
            temp = temp + argv[1][i];
        }
    }
    arr.push_back(stoi(temp));
    int key = stoi(argv[2]);
    bool found = false;
    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[i] == key)
        {
            found = true;
        }
    }
    if (found)
    {
        cout << "true";
    }
    else
    {
        cout << "false";
    }
}
```

{% endraw %}

Linear Search in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Grifski
- rzuckerm
- Vipin Yadav

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).