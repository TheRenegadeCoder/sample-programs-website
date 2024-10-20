---
authors:
- rzuckerm
date: 2024-02-04
featured-image: selection-sort-in-every-language.jpg
last-modified: 2024-02-04
layout: default
tags:
- beef
- selection-sort
title: Selection Sort in Beef
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/selection-sort/beef/how-to-implement-the-solution.md
- sources/programs/selection-sort/beef/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Selection Sort](https://sampleprograms.io/projects/selection-sort) in [Beef](https://sampleprograms.io/languages/beef) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```beef
using System;
using System.Collections;

namespace SelectionSort;

class Program
{
    public static void Usage()
    {
        Console.WriteLine(
            """
            Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"
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

    // Reference: https://en.wikipedia.org/wiki/Selection_sort#Implementations
    public static void SelectionSort<T>(List<T> arr)
    where int : operator T <=> T
    {
        int nMinus1 = arr.Count - 1;
        for (int i < nMinus1)
        {
            int jMin = i;
            for (int j in (i + 1)...nMinus1)
            {
                if (arr[j] < arr[jMin])
                {
                    jMin = j;
                }
            }

            if (jMin != i)
            {
                Swap!(arr[i], arr[jMin]);
            }
        }
    }

    public static void ShowList<T>(List<T> arr)
    {
        String line = scope .();
        for (T val in arr)
        {
            if (!line.IsEmpty)
            {
                line += ", ";
            }

            line.AppendF("{}", val);
        }

        Console.WriteLine(line);
    }

    public static int Main(String[] args)
    {
        if (args.Count < 1)
        {
            Usage();
        }

        List<int32> arr = scope .();
        switch (ParseIntList<int32>(args[0], arr))
        {
            case .Ok:
                if (arr.Count < 2)
                {
                    Usage();
                }
            case .Err:
                Usage();
        }

        SelectionSort<int32>(arr);
        ShowList<int32>(arr);
        return 0;
    }
}

```

{% endraw %}

Selection Sort in [Beef](https://sampleprograms.io/languages/beef) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).