---
authors:
- Parker Johansen
- Ștefan-Iulian Alecu
date: 2018-10-28
featured-image: longest-common-subsequence-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- longest-common-subsequence
title: Longest Common Subsequence in C#
title1: Longest Common
title2: Subsequence in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-common-subsequence/c-sharp/how-to-implement-the-solution.md
- sources/programs/longest-common-subsequence/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Common Subsequence](/projects/longest-common-subsequence) in [C#](/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System.Collections.Generic;

if (
    args is not [var raw1, var raw2]
    || !TryParseList(raw1.AsSpan(), out var a)
    || !TryParseList(raw2.AsSpan(), out var b)
)
{
    Console.WriteLine(
        """
Usage: please provide two lists in the format "1, 2, 3, 4, 5"
"""
    );
    return;
}

Console.WriteLine(string.Join(", ", LCS(a, b)));

static bool TryParseList(ReadOnlySpan<char> span, out List<int> numbers)
{
    numbers = new(span.Count(',') + 1);

    while (!span.IsEmpty)
    {
        int comma = span.IndexOf(',');
        var token = comma >= 0 ? span[..comma] : span;

        span = comma >= 0 ? span[(comma + 1)..] : [];

        if (!int.TryParse(token, out int n))
            return false;

        numbers.Add(n);
    }

    return true;
}

static List<int> LCS(List<int> a, List<int> b)
{
    int n = a.Count, m = b.Count;
    if (n == 0 || m == 0) return [];

    int[,] dp = new int[n + 1, m + 1];

    for (int i = 1; i <= n; i++)
    for (int j = 1; j <= m; j++)
        dp[i, j] = a[i - 1] == b[j - 1]
            ? dp[i - 1, j - 1] + 1
            : Math.Max(dp[i - 1, j], dp[i, j - 1]);

    var result = new List<int>(dp[n, m]);

    int i2 = n, j2 = m;

    while (i2 > 0 && j2 > 0)
    {
        if (a[i2 - 1] == b[j2 - 1])
        {
            result.Add(a[i2 - 1]);
            i2--;
            j2--;
        }
        else if (dp[i2 - 1, j2] >= dp[i2, j2 - 1])
        {
            i2--;
        }
        else
        {
            j2--;
        }
    }

    result.Reverse();
    return result;
}

```

{% endraw %}

Longest Common Subsequence in [C#](/languages/c-sharp) was written by:

- Parker Johansen
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).