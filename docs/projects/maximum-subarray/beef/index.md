---
authors:
- rzuckerm
date: 2024-02-15
featured-image: maximum-subarray-in-every-language.jpg
last-modified: 2024-02-15
layout: default
tags:
- beef
- maximum-subarray
title: Maximum Subarray in Beef
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/maximum-subarray/beef/how-to-implement-the-solution.md
- sources/programs/maximum-subarray/beef/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Maximum Subarray](https://sampleprograms.io/projects/maximum-subarray) in [Beef](https://sampleprograms.io/languages/beef) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```beef
using System;
using System.Collections;

namespace MaximumSubarray;

class Program
{
    public static void Usage()
    {
        Console.WriteLine(
            """
            Usage: Please provide a list of integers in the format: "1, 2, 3, 4, 5"
            """
        );
        Environment.Exit(0);
    }

    public static Result<T> ParseInt<T>(StringView str)
    where T : IParseable<T>
    {
        StringView trimmedStr = scope String(str);
        trimmedStr.Trim();

        // T.Parse ignores single quotes since they are treat as digit separators -- e.g. 1'000
        if (trimmedStr.Contains('\''))
        {
            return .Err;
        }

        return T.Parse(trimmedStr);
    }

    public static Result<void> ParseIntList<T>(StringView str, List<T> arr)
    where T: IParseable<T>
    {
        arr.Clear();
        for (StringView item in str.Split(','))
        {
            switch (ParseInt<T>(item))
            {
                case .Ok(let val):
                    arr.Add(val);

                case .Err:
                    return .Err;
            }
        }

        return .Ok;
    }

    // Find maximum subarray using Kadane's algorithm.
    // Source: https://en.wikipedia.org/wiki/Maximum_subarray_problem#No_empty_subarrays_admitted
    public static T MaximumSubarray<T>(List<T> arr)
    where T : operator explicit int, operator T + T, IMinMaxValue<T>
    where int : operator T <=> T
    {
        T bestSum = T.MinValue;
        T currentSum = default(T);
        for (T val in arr)
        {
            currentSum = val + Math.Max<T>(default(T), currentSum);
            bestSum = Math.Max<T>(currentSum, bestSum);
        }

        return bestSum;
    }

    public static int Main(String[] args)
    {
        if (args.Count < 1)
        {
            Usage();
        }

        List<int32> arr = scope .();
        if (ParseIntList<int32>(args[0], arr) case .Err)
        {
            Usage();
        }

        int32 result = MaximumSubarray<int32>(arr);
        Console.WriteLine(result);

        return 0;
    }
}

```

{% endraw %}

Maximum Subarray in [Beef](https://sampleprograms.io/languages/beef) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).