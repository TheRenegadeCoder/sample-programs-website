---

title: Factorial in C#
layout: default
date: 2022-04-28
last-modified: 2022-04-29

---

Welcome to the Factorial in C# page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

Note: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```C#
using System;
using System.Numerics;

namespace SamplePrograms
{
    public class Factorial
    {
        public static BigInteger Fact(BigInteger n)
        {
            if (n <= 0)
                return 1;
            return n * Fact(n - 1);
        }

        public static void Main(string[] args)
        {
            try
            {
                var n = BigInteger.Parse(args[0]);
                if (n > 4550)
                {
                    Console.WriteLine(string.Format("{0}! is out of the reasonable bounds for calculation.", n));
                    Environment.Exit(1);
                }
                else if (n < 0) {
                    Console.WriteLine("Usage: please input a non-negative integer");
                    Environment.Exit(1);
                }
                var result = Fact(n);
                Console.WriteLine(result);
            }
            catch
            {
                Console.WriteLine("Usage: please input a non-negative integer");
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