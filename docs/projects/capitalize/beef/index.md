---
authors:
- rzuckerm
date: 2024-01-18
featured-image: capitalize-in-every-language.jpg
last-modified: 2024-01-18
layout: default
tags:
- beef
- capitalize
title: Capitalize in Beef
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/capitalize/beef/how-to-implement-the-solution.md
- sources/programs/capitalize/beef/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Capitalize](https://sampleprograms.io/projects/capitalize) in [Beef](https://sampleprograms.io/languages/beef) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```beef
using System;

namespace Capitalize;

class Program
{
    public static void Usage()
    {
        Console.WriteLine("Usage: please provide a string");
        Environment.Exit(0);
    }

    public static void Capitalize(StringView str, ref String capitalized)
    {
        capitalized.Set(scope $"{str[0].ToUpper}{str[1...]}");
    }

    public static int Main(String[] args)
    {
        if (args.Count < 1 || args[0].Length == 0)
        {
            Usage();
        }

        String capitalized = scope .();
        Capitalize(args[0], ref capitalized);
        Console.WriteLine(capitalized);
        return 0;
    }
}

```

{% endraw %}

Capitalize in [Beef](https://sampleprograms.io/languages/beef) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).