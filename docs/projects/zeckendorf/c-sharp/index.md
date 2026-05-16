---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-11
featured-image: zeckendorf-in-every-language.png
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- zeckendorf
title: Zeckendorf in C#
title1: Zeckendorf
title2: in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/zeckendorf/c-sharp/how-to-implement-the-solution.md
- sources/programs/zeckendorf/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Zeckendorf](https://sampleprograms.io/projects/zeckendorf) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System;
using System.Collections.Generic;
using System.Globalization;

if (args is not [var raw] ||
    !long.TryParse(raw, out long n) ||
    n < 0)
{
    return ExitWithUsage();
}

if (n == 0)
    return 0;

ReadOnlySpan<long> fibs = GenerateFibs();
Span<long> buffer = stackalloc long[fibs.Length];

int count = Decompose(n, fibs, buffer);
Console.WriteLine(string.Join(", ", buffer[..count].ToArray()));

return 0;

static int Decompose(long n, ReadOnlySpan<long> fibs, Span<long> result)
{
    int count = 0;

    for (int i = fibs.Length - 1; i >= 0 && n > 0; i--)
    {
        long f = fibs[i];

        if (f <= n)
        {
            result[count++] = f;
            n -= f;
        }
    }

    return count;
}

static int ExitWithUsage()
{
    Console.WriteLine("Usage: please input a non-negative integer");
    return 1;
}

static long[] GenerateFibs()
{
    var list = new List<long> { 1, 2 };

    while (true)
    {
        long next = list[^1] + list[^2];
        if (next < 0 || next > long.MaxValue - list[^1])
            break;

        list.Add(next);
    }

    return list.ToArray();
}
```

{% endraw %}

Zeckendorf in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).