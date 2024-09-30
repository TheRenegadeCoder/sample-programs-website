---
authors:
- rzuckerm
date: 2024-01-22
featured-image: fibonacci-in-every-language.jpg
last-modified: 2024-01-22
layout: default
tags:
- beef
- fibonacci
title: Fibonacci in Beef
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/fibonacci/beef/how-to-implement-the-solution.md
- sources/programs/fibonacci/beef/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Fibonacci](https://sampleprograms.io/projects/fibonacci) in [Beef](https://sampleprograms.io/languages/beef) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```beef
using System;

namespace Fibonacci;

class Program
{
    public static void Usage()
    {
        Console.WriteLine("Usage: please input the count of fibonacci numbers to output");
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

    public static void Fibonacci(int32 n)
    {
        uint64 first = 0;
        uint64 second = 1;
        for (int i in 1...n)
        {
            second += first;
            first = second - first;
            Console.WriteLine($"{i}: {first}");
        }
    }

    public static int Main(String[] args)
    {
        if (args.Count < 1)
        {
            Usage();
        }

        int32 val = 0;
        switch (ParseInt<int32>(args[0]))
        {
            case .Ok(out val):
            case .Err:
                Usage();
        }

        Fibonacci(val);
        return 0;
    }
}

```

{% endraw %}

Fibonacci in [Beef](https://sampleprograms.io/languages/beef) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).