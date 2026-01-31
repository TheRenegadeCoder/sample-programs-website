---
authors:
- rzuckerm
date: 2026-01-31
featured-image: zeckendorf-in-every-language.png
last-modified: 2026-01-31
layout: default
tags:
- beef
- zeckendorf
title: Zeckendorf in Beef
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/zeckendorf/beef/how-to-implement-the-solution.md
- sources/programs/zeckendorf/beef/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Zeckendorf](https://sampleprograms.io/projects/zeckendorf) in [Beef](https://sampleprograms.io/languages/beef) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```beef
using System;
using System.Collections;

namespace Zeckendorf;

class Program
{
    public static void Usage()
    {
        Console.WriteLine("Usage: please input a non-negative integer");
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

    public static void FibonacciUpTo<T>(T n, List<T> fibs)
    where T : IInteger, operator explicit int, operator T + T, operator T - T
    where int : operator explicit T, operator T <=> T
    {
        T a = (T)1;
        T b = (T)2;
        fibs.Clear();
        while (a <= n) {
            fibs.Add(a);
            b += a;
            a = b - a;
        }
    }

    public static void Zeckendorf<T>(T n, List<T> zecks)
    where T : IInteger, operator explicit int, operator T + T, operator T - T
    where int : operator explicit T, operator T <=> T
    {
        List<T> fibs = scope .();
        FibonacciUpTo<T>(n, fibs);
        zecks.Clear();
        int k = fibs.Count - 1;
        T remaining = n;
        while (k >= 0 && remaining > (T)0) {
            T fib = fibs[k];
            if (fib <= remaining) {
                zecks.Add(fib);
                remaining -= fib;
                k -= 2;
            } else {
                k--;
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

        int32 n = 0;
        switch (ParseInt<int32>(args[0]))
        {
            case .Ok(out n):
                if (n < 0) {
                    Usage();
                }
            case .Err:
                Usage();
        }

        List<int32> zecks = scope .();
        Zeckendorf<int32>(n, zecks);
        ShowList<int32>(zecks);
        return 0;
    }
}

```

{% endraw %}

Zeckendorf in [Beef](https://sampleprograms.io/languages/beef) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).