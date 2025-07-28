---
authors:
- "\u0218tefan-Iulian Alecu"
date: 2025-07-29
featured-image: maximum-subarray-in-every-language.jpg
last-modified: 2025-07-29
layout: default
tags:
- c-sharp
- maximum-subarray
title: Maximum Subarray in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-subarray/c-sharp/how-to-implement-the-solution.md
- sources/programs/maximum-subarray/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

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
        Console.Error.WriteLine("Usage: Please provide a list of integers in the format: \"1, 2, 3, 4, 5\"");
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
                if (!int.TryParse(s, out var val))
                    ShowUsage();
                return val;
            })
            .ToList();

        if (list.Count == 0)
            ShowUsage();

        return list;
    }

    private static int MaximumSubarraySum(IReadOnlyList<int> numbers)
    {
        if (numbers.Count == 0)
            return 0;

        int currentSum = numbers[0];
        int maxSum = numbers[0];

        for (int i = 1; i < numbers.Count; i++)
        {
            int number = numbers[i];
            currentSum = Math.Max(number, currentSum + number);
            maxSum = Math.Max(maxSum, currentSum);
        }

        return maxSum;
    }

    public static int Main(string[] args)
    {
        if (args.Length != 1)
            ShowUsage();

        var inputList = ParseIntegerList(args[0]);

        Console.WriteLine(MaximumSubarraySum(inputList));

        return 0;
    }
}

```

{% endraw %}

Maximum Subarray in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Ștefan-Iulian Alecu

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).