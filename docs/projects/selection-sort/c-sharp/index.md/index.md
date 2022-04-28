# Selection Sort in C#

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

```C#
using System;
using System.Linq;
using System.Collections.Generic;

public class SelectionSort
{
    public static IEnumerable<int> Selection(List<int> xs)
    {
        while (xs.Any())
        {
            var x = xs.Min();
            xs.Remove(x);
            yield return x;
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
            var sortedXs = Selection(xs);
            Console.WriteLine(string.Join(", ", sortedXs));
        }
        catch
        {
            ErrorAndExit();
        }
    }
}
```

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.