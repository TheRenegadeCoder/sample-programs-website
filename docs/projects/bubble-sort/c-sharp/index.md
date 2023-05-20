---
title: Bubble Sort in C#
layout: default
date: 2018-12-28
featured-image: bubble-sort-in-every-language.jpg
last-modified: 2018-12-28

---

Welcome to the [Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System;
using System.Linq;
using System.Collections.Generic;

class CSharp
{
    public static List<int> BubbleSort(List<int> xs)
    {
        var acc = xs.ToList();
        var last = acc.ToList();
        do
        {
            last = acc.ToList();
            acc = PassList(last.ToList());
        }
        while(!acc.SequenceEqual(last));
        return acc;
    }

    public static List<int> PassList(List<int> xs)
    {
        if (xs.Count() <= 1)
            return xs;
        var x0 = xs[0];
        var x1 = xs[1];
        if (x1 < x0)
        {
            xs.RemoveAt(1);
            return new List<int>() {x1}.Concat(PassList(xs)).ToList();
        }
        else
        {
            xs.RemoveAt(0);
            return new List<int>() {x0}.Concat(PassList(xs)).ToList();
        }
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
            var sortedXs = BubbleSort(xs);
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

[Bubble Sort](https://sampleprograms.io/projects/bubble-sort) in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Mar 26 2019 00:26:31. The solution was first committed on Dec 28 2018 00:03:37. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).