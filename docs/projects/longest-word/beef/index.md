---
authors:
- rzuckerm
date: 2024-01-22
featured-image: longest-word-in-every-language.jpg
last-modified: 2024-01-22
layout: default
tags:
- beef
- longest-word
title: Longest Word in Beef
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/longest-word/beef/how-to-implement-the-solution.md
- sources/programs/longest-word/beef/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Longest Word](https://sampleprograms.io/projects/longest-word) in [Beef](https://sampleprograms.io/languages/beef) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```beef
using System;

namespace LongestWord;

class Program
{
    public static void Usage()
    {
        Console.WriteLine("Usage: please provide a string");
        Environment.Exit(0);
    }

    public static int LongestWord(StringView str)
    {
        int maxLen = 0;
        for (StringView word in str.Split(' ', '\t', '\r', '\n'))
        {
            maxLen = Math.Max<int>(maxLen, word.Length);
        }

        return maxLen;
    }

    public static int Main(String[] args)
    {
        if (args.Count < 1 || args[0].Length < 1)
        {
            Usage();
        }

        int result = LongestWord(args[0]);
        Console.WriteLine(result);
        return 0;
    }
}

```

{% endraw %}

Longest Word in [Beef](https://sampleprograms.io/languages/beef) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).