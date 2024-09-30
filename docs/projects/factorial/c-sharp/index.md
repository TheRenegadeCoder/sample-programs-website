---
authors:
- Bharath
- Parker Johansen
date: 2018-12-28
featured-image: factorial-in-every-language.jpg
last-modified: 2019-10-16
layout: default
tags:
- c-sharp
- factorial
title: Factorial in C#
---

<!--
AUTO-GENERATED -- PLEASE DO NOT EDIT!

Instead, please edit the following:

- sources/programs/factorial/c-sharp/how-to-implement-the-solution.md
- sources/programs/factorial/c-sharp/how-to-run-the-solution.md

See .github/CONTRIBUTING.md for further details.
-->

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

Factorial in [C#](https://sampleprograms.io/languages/c-sharp) was written by:

- Bharath
- Parker Johansen

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).