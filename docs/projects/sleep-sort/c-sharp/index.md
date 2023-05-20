---
title: Sleep Sort in C#
layout: default
date: 2020-10-05
featured-image: sleep-sort-in-every-language.jpg
last-modified: 2020-10-05

---

Welcome to the [Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
using System;
using System.Linq;
using System.Collections.Generic;
using System.Threading.Tasks;

public class SleepSort
{
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
            if (xs.Count <= 1)
                ErrorAndExit();

            Queue<int> sortedXs = new Queue<int>();

            Task.WaitAll(xs.Select(x =>
                Task.Delay(x * 1000).ContinueWith(_ => sortedXs.Enqueue(x))
            ).ToArray());

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

[Sleep Sort](https://sampleprograms.io/projects/sleep-sort) in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- SirePi

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).