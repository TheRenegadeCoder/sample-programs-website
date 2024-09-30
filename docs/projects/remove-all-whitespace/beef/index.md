---
authors:
- rzuckerm
date: 2024-01-18
featured-image: remove-all-whitespace-in-every-language.jpg
last-modified: 2024-01-18
layout: default
tags:
- beef
- remove-all-whitespace
title: Remove All Whitespace in Beef
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/remove-all-whitespace/beef/how-to-implement-the-solution.md
- sources/programs/remove-all-whitespace/beef/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Remove All Whitespace](https://sampleprograms.io/projects/remove-all-whitespace) in [Beef](https://sampleprograms.io/languages/beef) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```beef
using System;

namespace RemoveAllWhitespace;

class Program
{
    public static void Usage()
    {
        Console.WriteLine("Usage: please provide a string");
        Environment.Exit(0);
    }

    public static void RemoveAllWhitespace(StringView str, ref String result)
    {
        result.Clear();
        result.Join("", str.Split(' ', '\t', '\r', '\n'));
    }

    public static int Main(String[] args)
    {
        if (args.Count < 1 || args[0].Length < 1)
        {
            Usage();
        }

        String result = scope .();
        RemoveAllWhitespace(args[0], ref result);
        Console.WriteLine(result);
        return 0;
    }
}

```

{% endraw %}

Remove All Whitespace in [Beef](https://sampleprograms.io/languages/beef) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).