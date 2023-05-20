---
title: Quick Sort in C++
layout: default
date: 2019-11-01
featured-image: quick-sort-in-every-language.jpg
last-modified: 2019-11-01

---

Welcome to the [Quick Sort](https://sampleprograms.io/projects/quick-sort) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void handle_error()
{
    cout << "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"" << endl;
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

int partition1(vector<int> &a, int l, int u)
{
    int v, i, j, temp;
    v = a[l];
    i = l;
    j = u + 1;
    do
    {
        do
            i++;
        while (a[i] < v && i <= u);
        do
            j--;
        while (v < a[j]);
        if (i < j)
        {
            temp = a[i];
            a[i] = a[j];
            a[j] = temp;
        }
    } while (i < j);
    a[l] = a[j];
    a[j] = v;
    return (j);
}

void quick_sort(vector<int> &a, int l, int u)
{
    int j;
    if (l < u)
    {
        j = partition1(a, l, u);
        quick_sort(a, l, j - 1);
        quick_sort(a, j + 1, u);
    }
}

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        handle_error();
    }
    vector<int> v = convert(argv[1]);
    if (v.size() < 2)
    {
        cout << "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"" << endl;
        exit(0);
    }
    int n = v.size();
    int min_idx;
    quick_sort(v, 0, n - 1);
    for (int i = 0; i < n - 1; i++)
    {
        cout << v[i] << ", ";
    }
    cout << v[n - 1];
}
```

{% endraw %}

[Quick Sort](https://sampleprograms.io/projects/quick-sort) in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Grifski
- Sumathi Varadharajan

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 16:05:09. The solution was first committed on Nov 01 2019 02:04:42. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).