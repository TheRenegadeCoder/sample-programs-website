---
title: Quick Sort in C#
layout: default
date: 2018-12-30
featured-image: quick-sort-in-every-language.jpg
last-modified: 2018-12-30

---

Welcome to the [Quick Sort](https://sampleprograms.io/projects/quick-sort) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System;
using System.Linq;
using System.Collections.Generic;

public class QuickSort
{
    public static List<int> Sort(List<int> xs)
    {
        if (!xs.Any())
            return xs;

        var index = xs.Count() / 2;
        var x = xs[index];
        xs.RemoveAt(index);
        var left = Sort(xs.Where(v => v <= x).ToList());
        var right = Sort(xs.Where(v => v > x).ToList());
        return left.Append(x).Concat(right).ToList();
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
            var sortedXs = Sort(xs);
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

[Quick Sort](https://sampleprograms.io/projects/quick-sort) in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 26 2019 00:26:31. The solution was first committed on Dec 30 2018 02:07:40. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).