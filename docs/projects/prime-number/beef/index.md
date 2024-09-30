---
authors:
- rzuckerm
date: 2024-01-22
featured-image: prime-number-in-every-language.jpg
last-modified: 2024-01-22
layout: default
tags:
- beef
- prime-number
title: Prime Number in Beef
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/prime-number/beef/how-to-implement-the-solution.md
- sources/programs/prime-number/beef/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [Beef](https://sampleprograms.io/languages/beef) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```beef
using System;

namespace PrimeNumber;

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

    public static bool IsPrime<T>(T val)
        where T : IInteger, operator explicit int, operator explicit float, operator T % T, operator T + T
        where int : operator T <=> T
        where float : operator explicit T
    {
        bool isPrime = false;
        if (val == (T)2)
        {
            isPrime = true;
        }
        else if (val >= (T)3 && (val % (T)2) != (T)0)
        {
            isPrime = true;
            T q = (T)Math.Sqrt((float)val);
            for (T k = (T)3; k <= q; k += (T)2)
            {
                if ((val % k) == (T)0)
                {
                    isPrime = false;
                    break;
                }
            }
        }

        return isPrime;
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
                if (val < 0)
                {
                    Usage();
                }
            case .Err:
                Usage();
        }

        bool isPrime = IsPrime<int32>(val);
        Console.WriteLine(isPrime ? "prime" : "composite");
        return 0;
    }
}

```

{% endraw %}

Prime Number in [Beef](https://sampleprograms.io/languages/beef) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).