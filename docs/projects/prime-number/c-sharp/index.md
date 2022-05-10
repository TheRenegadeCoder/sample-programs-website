---

title: Prime Number in C#
layout: default
date: 2022-04-28
last-modified: 2022-05-10

---

Welcome to the Prime Number in C# page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

**Note**: The solution shown here is the current solution in the Sample Programs repository. Documentation below may be outdated.

{% raw %}

```c#
using System;
using Math = System.Math;

namespace SamplePrograms
{
    public class PrimeNumber
    {
        public static bool IsPrime(ulong x)
        {
            if (x <= 1)
                return false;
            if (x != 2 && x % 2 == 0)
                return false;

            for (ulong i = 3; i <= Convert.ToUInt64(Math.Sqrt(x)); i += 2)
            {
                if (x % i == 0)
                    return false;
            }

            return true;
        }

        public static void Main(string[] args)
        {
            try
            {
                var n = ulong.Parse(args[0]);
                if (n > 18446744073709551615) // Max of a ulong in C#
                {
                    Console.WriteLine(string.Format("{0} is out of the reasonable bounds for calculation.", n));
                    Environment.Exit(1);
                }
                var result = IsPrime(n) ? "Prime" : "Composite";
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

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).