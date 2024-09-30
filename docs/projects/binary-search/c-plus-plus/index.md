---
authors:
- Jeremy Grifski
- Sailok Chinta
date: 2019-10-27
featured-image: binary-search-in-every-language.jpg
last-modified: 2022-10-10
layout: default
tags:
- binary-search
- c-plus-plus
title: Binary Search in C++
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/binary-search/c-plus-plus/how-to-implement-the-solution.md
- sources/programs/binary-search/c-plus-plus/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Binary Search](https://sampleprograms.io/projects/binary-search) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void handle_error()
{
    cout << "Usage: please provide a list of sorted integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")" << endl;
    exit(0);
}

int check(string s)
{
    int x1 = 0, x2 = s.size() - 1;

    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] != ' ')
        {
            x1 = i;
            break;
        }
    }

    for (int i = s.size() - 1; i >= x1; i--)
    {
        if (s[i] != ' ')
        {
            x2 = i;
            break;
        }
    }

    for (int i = x1; i <= x2; i++)
    {
        if (s[i] == ' ')
        {
            handle_error();
        }
    }

    return stoi(s);
}

vector<int> convert(string s)
{
    if (s.size() == 0)
    {
        handle_error();
    }
    vector<int> v;
    string num = "";
    for (int i = 0; i < s.size(); i++)
    {
        if ((int)s[i] >= 48 && (int)s[i] <= 57 || s[i] == ' ')
        {
            num += s[i];
        }
        else if (s[i] == ',')
        {
            v.push_back(check(num));
            num = "";
        }
        else
        {
            handle_error();
        }
    }

    if (num.size() > 0)
    {
        v.push_back(check(num));
    }

    return v;
}

int main(int argc, char *argv[])
{
    if (argc < 3)
    {
        handle_error();
    }

    vector<int> v = convert(argv[1]);
    int num = check(argv[2]);

    for (int i = 0; i < v.size() - 1; i++)
    {
        if (v[i] > v[i + 1])
        {
            handle_error();
        }
    }

    int start = 0, end = v.size();
    string ans = "false";
    while (start < end)
    {
        int mid = (start + end) / 2;

        if (num < v[mid])
        {
            end = mid;
        }
        else if (v[mid] < num)
        {
            start = mid + 1;
        }
        else if (v[mid] == num)
        {
            ans = "true";
            break;
        }
    }

    if (start > end)
    {
        ans = "false";
    }

    cout << ans << endl;
}

```

{% endraw %}

Binary Search in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Grifski
- Sailok Chinta

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).