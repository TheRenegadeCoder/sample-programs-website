---
authors:
- rzuckerm
date: 2024-01-22
featured-image: palindromic-number-in-every-language.jpg
last-modified: 2024-01-22
layout: default
tags:
- beef
- palindromic-number
title: Palindromic Number in Beef
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/palindromic-number/beef/how-to-implement-the-solution.md
- sources/programs/palindromic-number/beef/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Palindromic Number](https://sampleprograms.io/projects/palindromic-number) in [Beef](https://sampleprograms.io/languages/beef) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```beef
using System;

namespace PalindromicNumber;

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

    public static bool PalindromicNumber<T>(T val)
    where T: IInteger
    {
        String str = scope String();
        val.ToString(str);
        bool isPalindromic = true;
        for (int left = 0, right = str.Length - 1; left < right; left++, right--)
        {
            if (str[left] != str[right])
            {
                isPalindromic = false;
                break;
            }
        }

        return isPalindromic;
    }

    public static int Main(String[] args)
    {
        if (args.Count < 1 || args[0].Length < 1)
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

        bool result = PalindromicNumber<int32>(val);
        Console.WriteLine(result ? "true" : "false");
        return 0;
    }
}

```

{% endraw %}

Palindromic Number in [Beef](https://sampleprograms.io/languages/beef) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).