---

title: Merge Sort in C#
layout: default
date: 2022-04-28
last-modified: 2022-05-11

---

Welcome to the Merge Sort in C# page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```c#
using System;
using System.Linq;
using System.Collections.Generic;

public class MergeSort
{
    public static List<int> Sort(List<int> xs) => Sort(xs.Select(x => new List<int>() {x}).ToList()).First();
    public static List<List<int>> Sort(List<List<int>> xs)
    {
        if (xs.Count <= 1)
            return xs;
        var x0 = xs[0];
        var x1 = xs[1];
        xs.RemoveAt(0);
        xs.RemoveAt(0);
        return Sort(new List<List<int>>()
        {
            Merge(x0, x1)
        }.Concat(Sort(xs).ToList()).ToList());
    }

    public static List<int> Merge(List<int> xs, List<int> ys)
    {
        if (!xs.Any())
            return ys;
        if (!ys.Any())
            return xs;
        if (xs[0] < ys[0])
        {
            var x0 = xs[0];
            xs.RemoveAt(0);
            return new List<int>() {x0}.Concat(Merge(xs, ys)).ToList();
        }
        var y0 = ys[0];
        ys.RemoveAt(0);
        return new List<int>() {y0}.Concat(Merge(xs, ys)).ToList();
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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).