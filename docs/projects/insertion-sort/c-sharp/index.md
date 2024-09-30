---
authors:
- Parker Johansen
date: 2018-12-28
featured-image: insertion-sort-in-every-language.jpg
last-modified: 2019-03-26
layout: default
tags:
- c-sharp
- insertion-sort
title: Insertion Sort in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/insertion-sort/c-sharp/how-to-implement-the-solution.md
- sources/programs/insertion-sort/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

Welcome to the [Insertion Sort](https://sampleprograms.io/projects/insertion-sort) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System;
using System.Linq;
using System.Collections.Generic;

public class InsertionSort
{
    public static List<int> Insertion(List<int> xs)
    {
        var sorted = new List<int>();
        foreach (var x in xs)
            sorted = Insert(sorted, x);
        return sorted;
    }

    public static List<int> Insert(List<int> xs, int x)
    {
        var index = 0;
        while (index < xs.Count() && x > xs[index])
            index++;
        xs.Insert(index > 0 ? index : 0, x);
        return xs;
    }

    public static void ErrorAndExit()
    {
        Console.WriteLine("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"");
        Environment.Exit(1);   
    }
    
    public static void Main(string[] args)
    {
        if (args.Length != 1)
            ErrorAndExit();
        try
        {
            var xs = args[0].Split(',').Select(i => Int32.Parse(i.Trim())).ToList();
            if (xs.Count() <= 1)
                ErrorAndExit();
            var sortedXs = Insertion(xs);
            Console.WriteLine(string.Join(", ", sortedXs));
        }
        catch
        {
            ErrorAndExit();
        }
    }
}
```

{% endraw %}

Insertion Sort in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).