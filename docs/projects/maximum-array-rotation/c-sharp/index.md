---
authors:
- Ștefan-Iulian Alecu
date: 2025-07-29
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- maximum-array-rotation
title: Maximum Array Rotation in C#
title1: Maximum Array
title2: Rotation in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-array-rotation/c-sharp/how-to-implement-the-solution.md
- sources/programs/maximum-array-rotation/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Array Rotation](/projects/maximum-array-rotation) in [C#](/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
﻿if (args is not [var input] || !TryParseList(input.AsSpan(), out var numbers))
    return ExitWithUsage();

Console.WriteLine(MaximumRotationSum(numbers));
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

    return numbers.Count > 0;
}

static int MaximumRotationSum(List<int> numbers)
{
    int n = numbers.Count;

    int totalSum = numbers[0];
    int rotationSum = 0;

    for (int i = 1; i < n; i++)
    {
        int v = numbers[i];
        totalSum += v;
        rotationSum += v * i;
    }

    int best = rotationSum;

    for (int i = 1, last = n - 1; i < n; i++, last--)
    {
        rotationSum += totalSum - n * numbers[last];
        best = Math.Max(best, rotationSum);
    }

    return best;
}

static int ExitWithUsage()
{
    Console.WriteLine(
        "Usage: please provide a list of integers (e.g. \"8, 3, 1, 2\")"
    );
    return 1;
}

```

{% endraw %}

Maximum Array Rotation in [C#](/languages/c-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).