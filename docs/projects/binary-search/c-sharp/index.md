---
authors:
- Jeremy Grifski
- Ștefan-Iulian Alecu
date: 2024-10-29
featured-image: binary-search-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- binary-search
- c-sharp
title: Binary Search in C#
title1: Binary
title2: Search in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/binary-search/c-sharp/how-to-implement-the-solution.md
- sources/programs/binary-search/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Binary Search](https://sampleprograms.io/projects/binary-search) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System.Collections.Generic;

if (args is not [var input, var targetRaw]
    || !int.TryParse(targetRaw, out int target)
    || !TryParseSorted(input.AsSpan(), out var numbers))
{
    return Usage();
}

Console.WriteLine(numbers.BinarySearch(target) >= 0);
return 0;

static bool TryParseSorted(ReadOnlySpan<char> span, out List<int> numbers)
{
    numbers = new(span.Count(',') + 1);

    int last = int.MinValue;

    while (!span.IsEmpty)
    {
        int comma = span.IndexOf(',');
        var token = comma >= 0 ? span[..comma] : span;

        span = comma >= 0 ? span[(comma + 1)..] : [];

        if (!int.TryParse(token, out int n) || n < last)
            return false;

        numbers.Add(n);
        last = n;
    }

    return numbers.Count > 0;
}

static int Usage()
{
    Console.Error.WriteLine(
        """Usage: please provide a list of sorted integers ("1, 4, 5, 11, 12") and the integer to find ("11")"""
    );

    return 1;
}
```

{% endraw %}

Binary Search in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Jeremy Grifski
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).