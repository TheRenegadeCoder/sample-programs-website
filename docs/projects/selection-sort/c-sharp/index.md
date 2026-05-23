---
authors:
- Parker Johansen
- Ștefan-Iulian Alecu
date: 2018-12-30
featured-image: selection-sort-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- selection-sort
title: Selection Sort in C#
title1: Selection
title2: Sort in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/selection-sort/c-sharp/how-to-implement-the-solution.md
- sources/programs/selection-sort/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Selection Sort](/projects/selection-sort) in [C#](/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System.Collections.Generic;
using System.Runtime.InteropServices;

if (args is not [var input] || !TryParseList(input.AsSpan(), out var numbers))
    return ExitWithUsage();

SelectionSort(numbers);

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

static void SelectionSort(List<int> list)
{
    if (list.Count < 2)
        return;

    Span<int> span = CollectionsMarshal.AsSpan(list);

    int n = span.Length;

    for (int i = 0; i < n - 1; i++)
    {
        int minIndex = i;

        for (int j = i + 1; j < n; j++)
        {
            if (span[j] < span[minIndex])
                minIndex = j;
        }

        if (minIndex != i)
            (span[i], span[minIndex]) = (span[minIndex], span[i]);
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

Selection Sort in [C#](/languages/c-sharp) was written by:

- Parker Johansen
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).