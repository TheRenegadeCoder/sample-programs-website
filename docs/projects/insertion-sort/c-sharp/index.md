---

title: Insertion Sort in C#
layout: default
date: 2022-04-28
last-modified: 2022-05-10

---

Welcome to the Insertion Sort in C# page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

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

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).