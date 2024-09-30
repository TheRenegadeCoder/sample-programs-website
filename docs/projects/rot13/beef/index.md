---
authors:
- rzuckerm
date: 2024-01-22
featured-image: rot13-in-every-language.jpg
last-modified: 2024-01-22
layout: default
tags:
- beef
- rot13
title: Rot13 in Beef
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/rot13/beef/how-to-implement-the-solution.md
- sources/programs/rot13/beef/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Rot13](https://sampleprograms.io/projects/rot13) in [Beef](https://sampleprograms.io/languages/beef) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```beef
using System;

namespace Rot13;

class Program
{
    public static void Usage()
    {
        Console.WriteLine("Usage: please provide a string to encrypt");
        Environment.Exit(0);
    }

    public static void Rot13(StringView str, ref String result)
    {
        result.Clear();
        result.Reserve(str.Length);
        for (char8 ch in str)
        {
            char8 chLower = ch.ToLower;
            if (chLower >= 'a' && chLower <= 'm')
            {
                ch += 13;
            }
            else if (chLower >= 'n' && chLower <= 'z')
            {
                ch -= 13;
            }

            result += ch;
        }
    }

    public static int Main(String[] args)
    {
        if (args.Count < 1 || args[0].Length < 1)
        {
            Usage();
        }

        String result = scope String();
        Rot13(args[0], ref result);
        Console.WriteLine(result);
        return 0;
    }
}
```

{% endraw %}

Rot13 in [Beef](https://sampleprograms.io/languages/beef) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).