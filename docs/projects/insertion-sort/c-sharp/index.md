---
authors:
- Parker Johansen
- Ștefan-Iulian Alecu
date: 2018-12-28
featured-image: insertion-sort-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- insertion-sort
title: Insertion Sort in C#
title1: Insertion
title2: Sort in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/insertion-sort/c-sharp/how-to-implement-the-solution.md
- sources/programs/insertion-sort/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [C#](https://sampleprograms.io/languages/c-sharp)! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System.Runtime.InteropServices;

if (args is not [var input] || !TryParseList(input.AsSpan(), out var numbers))
    return Usage();

InsertionSort(CollectionsMarshal.AsSpan(numbers));

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

static void InsertionSort(Span<int> xs)
{
    for (int i = 1; i < xs.Length; i++)
    {
        int x = xs[i];
        if (x >= xs[i - 1])
            continue;

        int lo = 0,
            hi = i;

        while (lo < hi)
        {
            int mid = (lo + hi) >> 1;

            if (x >= xs[mid])
                lo = mid + 1;
            else
                hi = mid;
        }

        xs[lo..i].CopyTo(xs[(lo + 1)..]);
        xs[lo] = x;
    }
}

static int Usage()
{
    Console.Error.WriteLine(
        """
Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"
"""
    );
    return 1;
}

```

{% endraw %}

Insertion Sort in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Parker Johansen
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).