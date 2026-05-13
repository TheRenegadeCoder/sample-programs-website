---
authors:
- Parker Johansen
- Ștefan-Iulian Alecu
date: 2018-12-28
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- bubble-sort
- c-sharp
title: Bubble Sort in C#
title1: Bubble
title2: Sort in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/bubble-sort/c-sharp/how-to-implement-the-solution.md
- sources/programs/bubble-sort/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System.Runtime.InteropServices;

if (args is not [var input] || !TryParseList(input.AsSpan(), out var numbers))
    return Usage();

BubbleSort(numbers);

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

static void BubbleSort(List<int> list)
{
    Span<int> span = CollectionsMarshal.AsSpan(list);
    int n = span.Length;

    for (int i = 0; i < n - 1; i++)
    {
        bool swapped = false;

        for (int j = 0; j < n - i - 1; j++)
        {
            if (span[j] <= span[j + 1])
                continue;

            (span[j], span[j + 1]) = (span[j + 1], span[j]);
            swapped = true;
        }

        if (!swapped)
            return;
    }
}


static int Usage()
{
    Console.Error.WriteLine("""
Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"
"""
    );
    return 1;
}
```

{% endraw %}

Bubble Sort in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Parker Johansen
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).