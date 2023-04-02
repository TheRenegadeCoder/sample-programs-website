---

title: Merge Sort in C++
layout: default
date: 2022-04-28
last-modified: 2023-04-02

---

Welcome to the [Merge Sort](https://sampleprograms.io/projects/merge-sort) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

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

void merge(int low, int mid, int high, vector<int> &v)
{
    int n1 = mid - low + 1;
    int n2 = high - mid;

    vector<int> v1(n1), v2(n2);

    for (int i = 0; i < n1; i++)
    {
        v1[i] = v[i + low];
    }

    for (int i = 0; i < n2; i++)
    {
        v2[i] = v[i + mid + 1];
    }

    int j = 0, k = 0;
    int l = low;

    while (j < n1 && k < n2)
    {
        if (v1[j] < v2[k])
        {
            v[l] = v1[j];
            j++;
        }
        else
        {
            v[l] = v2[k];
            k++;
        }
        l++;
    }

    while (j < n1)
    {
        v[l] = v1[j];
        j++;
        l++;
    }

    while (k < n2)
    {
        v[l] = v2[k];
        k++;
        l++;
    }
}

void mergesort(int low, int high, vector<int> &v)
{

    if (low < high)
    {
        int mid = (low + high) / 2;
        mergesort(low, mid, v);
        mergesort(mid + 1, high, v);
        merge(low, mid, high, v);
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

    mergesort(0, n - 1, v);

    for (int i = 0; i < n - 1; i++)
    {
        cout << v[i] << ", ";
    }
    cout << v[n - 1];
}
```

{% endraw %}

[Merge Sort](https://sampleprograms.io/projects/merge-sort) in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Jeremy Grifski
- Sailok Chinta

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 16:05:09. The solution was first committed on Oct 26 2019 08:19:51. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).