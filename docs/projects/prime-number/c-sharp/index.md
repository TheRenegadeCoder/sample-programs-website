---
title: Prime Number in C#
layout: default
date: 2018-12-30
featured-image: prime-number-in-every-language.jpg
last-modified: 2018-12-30

---

Welcome to the [Prime Number](https://sampleprograms.io/projects/prime-number) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

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

[Prime Number](https://sampleprograms.io/projects/prime-number) in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of May 02 2019 11:43:38. The solution was first committed on Dec 30 2018 01:40:03. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).