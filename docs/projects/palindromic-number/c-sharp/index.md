---
authors:
- maple-johnson
- Ștefan-Iulian Alecu
date: 2025-02-18
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- palindromic-number
title: Palindromic Number in C#
title1: Palindromic
title2: Number in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/c-sharp/how-to-implement-the-solution.md
- sources/programs/palindromic-number/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](/projects/palindromic-number) in [C#](/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
if (args is not [var raw] || !ulong.TryParse(raw.AsSpan(), out ulong number))
    return ExitWithUsage();

Console.WriteLine(IsPalindrome(number) ? "true" : "false");
return 0;

static bool IsPalindrome(ulong value)
{
    if (value < 10)
        return true;

    if (value % 10 == 0)
        return false;

    ulong reversedHalf = 0;

    while (value > reversedHalf)
    {
        reversedHalf = reversedHalf * 10 + value % 10;
        value /= 10;
    }

    return value == reversedHalf ||
           value == reversedHalf / 10;
}

static int ExitWithUsage()
{
    Console.WriteLine("Usage: please input a non-negative integer");
    return 1;
}
```

{% endraw %}

Palindromic Number in [C#](/languages/c-sharp) was written by:

- maple-johnson
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).