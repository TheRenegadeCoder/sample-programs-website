---
authors:
- Jeremy Grifski
date: 2024-10-29
featured-image: linear-search-in-every-language.jpg
last-modified: 2024-10-29
layout: default
tags:
- c-sharp
- linear-search
title: Linear Search in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/linear-search/c-sharp/how-to-implement-the-solution.md
- sources/programs/linear-search/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Linear Search](https://sampleprograms.io/projects/linear-search) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System;
using System.Linq;
using System.Collections.Generic;

public class LinearSearch
{
    public static bool Search(List<int> list, int toFind)
    {
        foreach (int value in list) 
        {
            if (value == toFind) 
            {
                return true;
            }
        }
        return false;
    }

    public static void ErrorAndExit()
    {
        Console.WriteLine("Usage: please provide a list of integers (\"1, 4, 5, 11, 12\") and the integer to find (\"11\")");
        Environment.Exit(1);
    }

    public static void Main(string[] args)
    {
        try
        {
            var list = args[0].Split(',').Select(i => Int32.Parse(i.Trim())).ToList();
            var toFind = Int32.Parse(args[1]);
            Console.WriteLine(Search(list, toFind));
        }
        catch
        {
            ErrorAndExit();
        }
    }
}

```

{% endraw %}

Linear Search in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).