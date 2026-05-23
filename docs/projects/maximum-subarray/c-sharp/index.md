---
authors:
- Ștefan-Iulian Alecu
date: 2025-07-29
featured-image: maximum-subarray-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- maximum-subarray
title: Maximum Subarray in C#
title1: Maximum
title2: Subarray in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-subarray/c-sharp/how-to-implement-the-solution.md
- sources/programs/maximum-subarray/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Subarray](/projects/maximum-subarray) in [C#](/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
﻿if (
    args is not [var input]
    || string.IsNullOrWhiteSpace(input)
    || !TryParseList(input.AsSpan(), out var numbers)
)
    return ExitWithUsage();

Console.WriteLine(MaximumSubarraySum(numbers));
return 0;

static int MaximumSubarraySum(List<int> numbers)
{
    int current = numbers[0];
    int best = numbers[0];

    for (int i = 1; i < numbers.Count; i++)
    {
        int v = numbers[i];
        current = Math.Max(v, current + v);
        best = Math.Max(current, best);
    }

    return best;
}

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

static int ExitWithUsage()
{
    Console.Error.WriteLine(
        "Usage: Please provide a list of integers in the format: \"1, 2, 3, 4, 5\""
    );
    return 1;
}

```

{% endraw %}

Maximum Subarray in [C#](/languages/c-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).