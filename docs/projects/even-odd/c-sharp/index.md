---

title: Even Odd in C#
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Even Odd in C# page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```C#
using System;

namespace SamplePrograms
{
    public class EvenOdd
    {
        public static void Main(string[] args)
        {
            try
            {
                int n = int.Parse(args[0]);
                var result = n % 2 == 0 ? "Even" : "Odd";
                Console.WriteLine(result);
            }
            catch
            {
                Console.WriteLine("Usage: please input a number");
                Environment.Exit(1);
            }
        }
    }
}

```

{% endraw %}

## How to Implement the Solution

No how to implement the solution available. Please consider contributing.

## How to Run the Solution

No how to run the solution available. Please consider contributing.