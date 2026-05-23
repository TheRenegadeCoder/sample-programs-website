---
authors:
- Parker Johansen
- Ștefan-Iulian Alecu
date: 2018-12-30
featured-image: prime-number-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- prime-number
title: Prime Number in C#
title1: Prime Number
title2: in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/c-sharp/how-to-implement-the-solution.md
- sources/programs/prime-number/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](/projects/prime-number) in [C#](/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
if (args is not [var raw] || !ulong.TryParse(raw, out ulong number))
    return ExitWithUsage();

Console.WriteLine(IsPrime(number) ? "Prime" : "Composite");
return 0;

static bool IsPrime(ulong value)
{
    if (value < 2)
        return false;

    if (value == 2)
        return true;

    if (value % 2 == 0)
        return false;

    for (ulong divisor = 3; divisor * divisor <= value; divisor += 2)
    {
        if (value % divisor == 0)
            return false;
    }

    return true;
}

static int ExitWithUsage()
{
    Console.WriteLine("Usage: please input a non-negative integer");
    return 1;
}

```

{% endraw %}

Prime Number in [C#](/languages/c-sharp) was written by:

- Parker Johansen
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).