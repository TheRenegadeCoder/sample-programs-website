---
title: Factorial in C#
layout: default
date: 2018-12-28
featured-image: factorial-in-every-language.jpg
last-modified: 2018-12-28

---

Welcome to the [Factorial](https://sampleprograms.io/projects/factorial) in [C#](https://sampleprograms.io/languages/c-sharp) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c#
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

[Factorial](https://sampleprograms.io/projects/factorial) in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Bharath
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 16 2019 15:14:04. The solution was first committed on Dec 28 2018 17:51:27. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).