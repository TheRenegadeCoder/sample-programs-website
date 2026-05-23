---
authors:
- Parker Johansen
- Ștefan-Iulian Alecu
date: 2018-12-30
featured-image: quick-sort-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- quick-sort
title: Quick Sort in C#
title1: Quick Sort
title2: in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/quick-sort/c-sharp/how-to-implement-the-solution.md
- sources/programs/quick-sort/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Quick Sort](/projects/quick-sort) in [C#](/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System.Collections.Generic;
using System.Runtime.InteropServices;
using System.Buffers;

if (args is not [var input] || !TryParseList(input.AsSpan(), out var numbers))
    return ExitWithUsage();

Span<int> span = CollectionsMarshal.AsSpan(numbers);
QuickSort(span);

Console.WriteLine(string.Join(", ", numbers));
return 0;

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

    return numbers.Count > 1;
}

static void QuickSort(Span<int> span)
{
    if (span.Length <= 1)
        return;

    int lo = 0;
    int hi = span.Length - 1;

    Sort(span, lo, hi);

    static void Sort(Span<int> s, int lo, int hi)
    {
        while (lo < hi)
        {
            int p = Partition(s, lo, hi);

            // Tail recursion elimination: sort smaller side first
            if (p - lo < hi - p)
            {
                Sort(s, lo, p - 1);
                lo = p + 1;
            }
            else
            {
                Sort(s, p + 1, hi);
                hi = p - 1;
            }
        }
    }

    static int Partition(Span<int> s, int lo, int hi)
    {
        int pivot = s[hi];
        int i = lo;

        for (int j = lo; j < hi; j++)
        {
            if (s[j] <= pivot)
            {
                (s[i], s[j]) = (s[j], s[i]);
                i++;
            }
        }

        (s[i], s[hi]) = (s[hi], s[i]);
        return i;
    }
}

static int ExitWithUsage()
{
    Console.WriteLine(
        "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\""
    );
    return 1;
}

```

{% endraw %}

Quick Sort in [C#](/languages/c-sharp) was written by:

- Parker Johansen
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).