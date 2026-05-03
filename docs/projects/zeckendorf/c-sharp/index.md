---
authors:
- Ștefan-Iulian Alecu
date: 2026-04-11
featured-image: zeckendorf-in-every-language.png
last-modified: 2026-04-11
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
using System.Globalization;

public static class Zeckendorf
{
    private static readonly long[] Fibs = GenerateFibs();

    private static long[] GenerateFibs()
    {
        var fs = new List<long> { 1, 2 };
        while (long.MaxValue - fs[^1] >= fs[^2])
        {
            fs.Add(fs[^1] + fs[^2]);
        }
        return [.. fs];
    }

    public static void Main(string[] args)
    {
        if (args.Length == 0 || !long.TryParse(args[0], NumberStyles.None, CultureInfo.InvariantCulture, out var n) || n < 0)
        {
            Console.WriteLine("Usage: please input a non-negative integer");
            return;
        }

        if (n == 0) return;

        Span<long> terms = stackalloc long[Fibs.Length];
        int count = Decompose(n, terms);

        PrintResults(terms[..count]);
    }

    private static int Decompose(long n, Span<long> terms)
    {
        int count = 0;
        int i = Array.BinarySearch(Fibs, n);
        if (i < 0) i = ~i - 1;

        for (; i >= 0 && n > 0; i--)
        {
            if (Fibs[i] <= n)
            {
                terms[count++] = Fibs[i];
                n -= Fibs[i];
            }
        }
        return count;
    }

    private static void PrintResults(ReadOnlySpan<long> terms) =>
        Console.WriteLine(string.Join(", ", terms.ToArray()));
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