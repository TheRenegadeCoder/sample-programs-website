---

---

Welcome to the Sleep Sort in C# page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```C#
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

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.