---
authors:
- Parker Johansen
- Ștefan-Iulian Alecu
date: 2018-12-28
featured-image: factorial-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- factorial
title: Factorial in C#
title1: Factorial
title2: in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/c-sharp/how-to-implement-the-solution.md
- sources/programs/factorial/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System.Numerics;

if (args is not [var input] || !BigInteger.TryParse(input, out var n) || n < 0)
{
    Console.Error.WriteLine("Usage: please input a non-negative integer");
    return;
}

Console.WriteLine(Factorial(n));

static BigInteger Factorial(BigInteger n) => n < 2 ? BigInteger.One : MultiplyRange(2, n);

static BigInteger MultiplyRange(BigInteger lo, BigInteger hi)
{
    if (lo > hi)
        return BigInteger.One;
    if (lo == hi)
        return lo;
    if (hi - lo == 1)
        return lo * hi;

    BigInteger mid = (lo + hi) / 2;
    return MultiplyRange(lo, mid) * MultiplyRange(mid + 1, hi);
}

```

{% endraw %}

Factorial in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Parker Johansen
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).