---
authors:
- rzuckerm
date: 2024-01-18
featured-image: duplicate-character-counter-in-every-language.jpg
last-modified: 2024-01-18
layout: default
tags:
- beef
- duplicate-character-counter
title: Duplicate Character Counter in Beef
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/duplicate-character-counter/beef/how-to-implement-the-solution.md
- sources/programs/duplicate-character-counter/beef/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Duplicate Character Counter](https://sampleprograms.io/projects/duplicate-character-counter) in [Beef](https://sampleprograms.io/languages/beef) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```beef
using System;

namespace DuplicateCharacterCounter;

class Program
{
    public static void Usage()
    {
        Console.WriteLine("Usage: please provide a string");
        Environment.Exit(0);
    }

    public static void CountDuplicateCharacters(StringView str, uint[] dupeCounter)
    {
        for (int i < 256)
        {
            dupeCounter[i] = 0;
        }

        for (char8 ch in str)
        {
            dupeCounter[(int)ch]++;
        }
    }

    public static void ShowDuplicateCharacterCounts(StringView str, uint[] dupeCounter)
    {
        bool hasDupes = false;
        for (char8 ch in str)
        {
            uint dupeCount = dupeCounter[(int)ch];
            if (dupeCount > 1)
            {
                Console.WriteLine($"{ch}: {dupeCount}");
                dupeCounter[(int)ch] = 0; // Indicate character already seen
                hasDupes = true;
            }
        }

        if (!hasDupes)
        {
            Console.WriteLine("No duplicate characters");
        }
    }

    public static int Main(String[] args)
    {
        if (args.Count < 1 || args[0].Length < 1)
        {
            Usage();
        }

        uint[] dupeCounter = scope uint[256];
        CountDuplicateCharacters(args[0], dupeCounter);
        ShowDuplicateCharacterCounts(args[0], dupeCounter);
        return 0;
    }
}

```

{% endraw %}

Duplicate Character Counter in [Beef](https://sampleprograms.io/languages/beef) was written by:

- rzuckerm

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).