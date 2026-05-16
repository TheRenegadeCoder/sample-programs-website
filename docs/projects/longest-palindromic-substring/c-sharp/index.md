---
authors:
- Maxwell Maslov
- Ștefan-Iulian Alecu
date: 2024-11-08
featured-image: longest-palindromic-substring-in-every-language.jpg
last-modified: 2026-05-13
layout: default
tags:
- c-sharp
- longest-palindromic-substring
title: Longest Palindromic Substring in C#
title1: Longest Palindromic
title2: Substring in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-palindromic-substring/c-sharp/how-to-implement-the-solution.md
- sources/programs/longest-palindromic-substring/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Palindromic Substring](https://sampleprograms.io/projects/longest-palindromic-substring) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
if (args is not { Length: > 0 })
    return Usage();

string result = LongestPalindrome(string.Join(' ', args));

if (result.Length < 2)
    return Usage();

Console.WriteLine(result);
return 0;

static string LongestPalindrome(string input)
{
    int length = input.Length;
    if (length < 2)
        return "";

    char[] transformed = new char[2 * length + 3];
    int[] radius = new int[transformed.Length];

    int index = 0;
    transformed[index++] = '^';

    ReadOnlySpan<char> source = input;

    foreach (char c in source)
    {
        transformed[index++] = '#';
        transformed[index++] = c;
    }

    transformed[index++] = '#';
    transformed[index++] = '$';

    int center = 0;
    int rightBoundary = 0;

    int bestCenter = 0;
    int bestRadius = 0;

    for (int i = 1; i < index - 1; i++)
    {
        int mirror = 2 * center - i;
        int R = radius[i];

        if (i < rightBoundary)
            R = Math.Min(rightBoundary - i, radius[mirror]);

        while (transformed[i + R + 1] == transformed[i - R - 1])
            R++;

        radius[i] = R;
        int expandedRight = i + R;

        center = expandedRight > rightBoundary ? i : center;
        rightBoundary = Math.Max(expandedRight, rightBoundary);

        bool isBest = R > bestRadius;
        bestRadius = isBest ? R : bestRadius;
        bestCenter = isBest ? i : bestCenter;
    }

    if (bestRadius < 2)
        return "";

    int startIndex = (bestCenter - bestRadius) / 2;
    return input.AsSpan(startIndex, bestRadius).ToString();
}

static int Usage()
{
    Console.Error.WriteLine("Usage: please provide a string that contains at least one palindrome");
    return 1;
}

```

{% endraw %}

Longest Palindromic Substring in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Maxwell Maslov
- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).