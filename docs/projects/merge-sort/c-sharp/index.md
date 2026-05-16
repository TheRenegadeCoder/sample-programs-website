---
authors:
- Parker Johansen
- Ștefan-Iulian Alecu
date: 2018-12-30
featured-image: merge-sort-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- merge-sort
title: Merge Sort in C#
title1: Merge Sort
title2: in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/merge-sort/c-sharp/how-to-implement-the-solution.md
- sources/programs/merge-sort/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Merge Sort](https://sampleprograms.io/projects/merge-sort) in [C#](https://sampleprograms.io/languages/c-sharp)! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System.Collections.Generic;
using System.Runtime.InteropServices;
using System.Buffers;

if (args is not [var input] || !TryParseList(input.AsSpan(), out var numbers))
    return ExitWithUsage();

Span<int> span = CollectionsMarshal.AsSpan(numbers);
MergeSort(span);

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

// Bottom-up merge sort
static void MergeSort(Span<int> span)
{
    int n = span.Length;
    if (n <= 1)
        return;

    int[] buffer = new int[n];

    Span<int> src = span;
    Span<int> dst = buffer;

    for (int width = 1; width < n; width *= 2)
    {
        for (int left = 0; left < n; left += width * 2)
        {
            int mid = Math.Min(left + width, n);
            int right = Math.Min(left + width * 2, n);

            Merge(
                src[left..mid],
                src[mid..right],
                dst[left..right]
            );
        }

        Span<int> temp = src;
        src = dst;
        dst = temp;
    }

    // if final data ended up in buffer, copy back
    if (!src.Overlaps(span))
        src.CopyTo(span);
}

static void Merge(
    ReadOnlySpan<int> left,
    ReadOnlySpan<int> right,
    Span<int> target)
{
    int li = 0;
    int ri = 0;
    int ti = 0;

    while (li < left.Length && ri < right.Length)
    {
        target[ti++] = left[li] <= right[ri]
            ? left[li++]
            : right[ri++];
    }

    left[li..].CopyTo(target[ti..]);
    right[ri..].CopyTo(target[ti..]);
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

Merge Sort in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Parker Johansen
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).