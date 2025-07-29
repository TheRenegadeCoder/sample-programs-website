---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-07-29
featured-image: maximum-array-rotation-in-every-language.jpg
last-modified: 2025-07-29
layout: default
tags:
- c-sharp
- maximum-array-rotation
title: Maximum Array Rotation in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-array-rotation/c-sharp/how-to-implement-the-solution.md
- sources/programs/maximum-array-rotation/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Array Rotation](https://sampleprograms.io/projects/maximum-array-rotation) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
﻿using System;
using System.Collections.Generic;
using System.Linq;

public static class Program
{
    private static void ShowUsage()
    {
        Console.Error.WriteLine("Usage: please provide a list of integers (e.g. \"8, 3, 1, 2\")");
        Environment.Exit(1);
    }

    private static List<int> ParseIntegerList(string input)
    {
        if (string.IsNullOrWhiteSpace(input))
            ShowUsage();

        var list = input
            .Split(',', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
            .Select(s =>
            {
                if (!int.TryParse(s, out var val) || val < 0)
                    ShowUsage();
                return val;
            })
            .ToList();

        if (list.Count == 0)
            ShowUsage();

        return list;
    }

    private static int MaximumRotationSum(IList<int> numbers)
    {
        int n = numbers.Count;
        if (n == 0)
            ShowUsage();

        int totalSum = 0;
        int currentWeightedSum = 0;

        for (int i = 0; i < n; i++)
        {
            totalSum += numbers[i];
            currentWeightedSum += numbers[i] * i;
        }

        int maxWeightedSum = currentWeightedSum;

        for (int i = 1; i < n; i++)
        {
            currentWeightedSum = currentWeightedSum + totalSum - n * numbers[n - i];
            if (currentWeightedSum > maxWeightedSum)
                maxWeightedSum = currentWeightedSum;
        }

        return maxWeightedSum;
    }

    public static int Main(string[] args)
    {
        if (args.Length != 1)
            ShowUsage();

        var inputList = ParseIntegerList(args[0]);

        Console.WriteLine(MaximumRotationSum(inputList));

        return 0;
    }
}

```

{% endraw %}

Maximum Array Rotation in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).