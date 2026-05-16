---
authors:
- Jeremy Grifski
- Ștefan-Iulian Alecu
date: 2024-10-29
featured-image: linear-search-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- linear-search
title: Linear Search in C#
title1: Linear
title2: Search in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/c-sharp/how-to-implement-the-solution.md
- sources/programs/linear-search/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [C#](https://sampleprograms.io/languages/c-sharp)! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
if (
    args is not [var input, var targetRaw]
    || !int.TryParse(targetRaw, out int target)
    || !TryParseList(input.AsSpan(), out var numbers)
)
    return Usage();

Console.WriteLine(numbers.Contains(target));
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

static int Usage()
{
    Console.WriteLine(
        """Usage: please provide a list of integers ("1, 4, 5, 11, 12") and the integer to find ("11")"""
    );
    return 1;
}

```

{% endraw %}

Linear Search in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Jeremy Grifski
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).